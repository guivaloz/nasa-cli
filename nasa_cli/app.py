"""
NASA CLI

Command Line Interface made with Typer and Python for NASA API.
"""
import typer

app = typer.Typer()


@app.command()
def main():
    print("Hola Mundo")


if __name__ == "__main__":
    app()
