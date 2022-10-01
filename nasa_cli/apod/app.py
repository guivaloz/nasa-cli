"""
APOD: Astronomy Picture of the Day
"""
import rich
import typer

app = typer.Typer()


@app.command()
def bajar():
    """Bajar el Astronomy Picture of the Day"""
    rich.print("[green]Bajar el Astronomy Picture of the Day[/green]")


@app.command()
def bajar_rango():
    """Bajar un rango de imagenes del Astronomy Picture of the Day"""
    rich.print("[green]Bajar un rango de imagenes Astronomy Picture of the Day[/green]")

    # Definir muestra de datos
    datos = [
        {"fecha": "2021-01-01", "titulo": "Titulo 1", "url": "https://url1.com"},
        {"fecha": "2021-01-02", "titulo": "Titulo 2", "url": "https://url2.com"},
        {"fecha": "2021-01-03", "titulo": "Titulo 3", "url": "https://url3.com"},
    ]

    # Elaborar tabla
    tabla = rich.table.Table()
    tabla.add_column("Fecha", justify="center")
    tabla.add_column("Titulo", justify="left")
    tabla.add_column("Media", justify="left")
    tabla.add_column("URL", justify="left")
    for item in datos:
        tabla.add_row(item["fecha"], item["titulo"], "Imagen", item["url"])

    # Mostrar tabla
    consola = rich.console.Console()
    consola.print(tabla)
