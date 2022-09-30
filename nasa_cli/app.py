"""
NASA CLI

Command Line Interface made with Typer and Python for NASA API.
"""
import typer

from apod.app import app as apod_app
from mars_photos.app import app as mars_photos_app

app = typer.Typer()
app.add_typer(apod_app, name="apod")
app.add_typer(mars_photos_app, name="mars-photos")

if __name__ == "__main__":
    app()
