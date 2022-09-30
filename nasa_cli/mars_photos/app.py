"""
Mars Rover Photos
"""
import typer

app = typer.Typer()


@app.command()
def bajar():
    """Bajar fotos del Mars Rover"""
    print("Bajar fotos del Mars Rover")
