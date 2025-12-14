"""
Mars Rover Photos
"""

import requests
from rich.console import Console
from rich.json import JSON
from typer import Typer

from .settings import get_settings

app = Typer()


@app.command()
def mostrar(
    page: int = 1,
    sol: int = 0,
):
    """Mostrar imagenes del Mars Rover"""
    console = Console()
    console.print("Mostrar imagenes del [blue]Mars Rover[/blue]")

    # Cargar configuración
    settings = get_settings()

    # Definir los parametros para la solicitud
    parametros = {
        "api_key": settings.API_KEY,
        "page": page,
        "sol": sol,
    }

    # Solicitar a la API las imagenes
    try:
        respuesta = requests.get(settings.BASE_URL, params=parametros, timeout=settings.TIMEOUT)
        respuesta.raise_for_status()
        datos = respuesta.json()
    except requests.exceptions.HTTPError as error:
        console.print(f"[red]Error {error.response.status_code}[/red]")
        console.print(error.response.text)
    except requests.exceptions.RequestException as error:
        console.print("[red]Error[/red]")
        console.print(error)

    # Mostrar los datos
    datos_json = JSON.from_data(datos)
    console.print(datos_json)
