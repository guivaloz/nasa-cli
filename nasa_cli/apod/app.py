"""
APOD: Astronomy Picture of the Day
"""
from datetime import date, datetime, timedelta
import os

from dotenv import load_dotenv
import rich
import typer

load_dotenv()

API_KEY = os.getenv("API_KEY", "")
TIMEOUT = int(os.getenv("TIMEOUT", 12))

app = typer.Typer()

BASE_URL = "https://api.nasa.gov/planetary/apod"
HOY = date.today().strftime("%Y-%m-%d")


@app.command()
def bajar(
    fecha: str = typer.Option(HOY, help="Fecha de la foto"),
):
    """Bajar el Astronomy Picture of the Day"""
    rich.print(f"[green]Bajar el Astronomy Picture of the Day[/green] de [blue]{fecha}[/blue]")

    # Mostrar la URL a solicitar
    url = f"{BASE_URL}?api_key={API_KEY}&date={fecha}"
    rich.print(f"[blue]{url}[/blue]")


@app.command()
def bajar_rango(
    desde: str = typer.Option(HOY, help="Fecha de inicio AAAA-MM-DD"),
    hasta: str = typer.Option(HOY, help="Fecha de termino AAAA-MM-DD"),
):
    """Bajar un rango de imagenes del Astronomy Picture of the Day"""
    rich.print("[green]Bajar un rango de imagenes Astronomy Picture of the Day[/green]")

    # Convertir las fechas a datetime
    desde_dt = datetime.strptime(desde, "%Y-%m-%d")
    hasta_dt = datetime.strptime(hasta, "%Y-%m-%d")

    # Elaborar tabla
    tabla = rich.table.Table()
    tabla.add_column("Fecha", justify="center")
    tabla.add_column("Titulo", justify="left")
    tabla.add_column("Media", justify="left")
    tabla.add_column("URL", justify="left")

    # Agregar datos a la tabla
    tiempo = desde_dt
    while tiempo <= hasta_dt:
        fecha = tiempo.strftime("%Y-%m-%d")
        tabla.add_row(
            fecha,
            f"Foto del {fecha}",
            "text/html",
            f"{BASE_URL}?api_key={API_KEY}&date={fecha}",
        )
        tiempo += timedelta(days=1)

    # Mostrar tabla
    consola = rich.console.Console()
    consola.print(tabla)
