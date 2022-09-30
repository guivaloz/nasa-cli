"""
APOD: Astronomy Picture of the Day
"""
import typer

app = typer.Typer()


@app.command()
def bajar():
    """Bajar el Astronomy Picture of the Day"""
    print("Bajar el Astronomy Picture of the Day")
