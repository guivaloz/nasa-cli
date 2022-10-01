"""
Mars Rover Photos
"""
import os

from dotenv import load_dotenv
import rich
import typer

load_dotenv()

API_KEY = os.getenv("API_KEY", "")
TIMEOUT = int(os.getenv("TIMEOUT", 12))

app = typer.Typer()

BASE_URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"


@app.command()
def bajar():
    """Bajar fotos del Mars Rover"""
    rich.print("[green]Bajar fotos del Mars Rover[/green]")
