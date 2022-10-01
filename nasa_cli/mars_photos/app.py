"""
Mars Rover Photos
"""
import rich
import typer

app = typer.Typer()


@app.command()
def bajar():
    """Bajar fotos del Mars Rover"""
    rich.print("[green]Bajar fotos del Mars Rover[/green]")
