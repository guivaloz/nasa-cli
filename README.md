# nasa-cli

Command Line Interface made with Typer and Python for NASA API.

## About NASA API

Go to [NASA API](https://api.nasa.gov/) to get started or read [NASA.md](NASA.md).

## Bashrc file

Create a configuration file named `.bashrc` in the root directory of the project

```bash
if [ -f ~/.bashrc ]
then
    . ~/.bashrc
fi

if command -v figlet &> /dev/null
then
    figlet NASA CLI
else
    echo "== NASA CLI"
fi
echo

if [ -f .env ]
then
    echo "-- Variables de entorno"
    export $(grep -v '^#' .env | xargs)
    echo "   API_KEY: ${API_KEY}"
    echo "   TIMEOUT: ${TIMEOUT}"
    echo
fi

if [ -d .venv ]
then
    echo "-- Activando el entorno virtual"
    source .venv/bin/activate
    python --version
    echo
    alias nasa="python3 ${PWD}/nasa_cli/app.py"
    echo "-- Ejecutar el CLI hecho con Typer"
    echo "   nasa --help"
    echo
fi
```

## Environment variables

Create a configuration file named `.env` in the root directory of the project.

```ini
# Your API key
API_KEY=****************************************

# Requests
TIMEOUT=12
```

## Installation

Create a virtual environment

```bash
python3 -m venv .venv
```

Use poetry to install dependencies

```bash
poetry install
```

Show help

```bash
poetry run python nasa_api/app.py --help
```

## Usage

Retrieve the Astronomy Picture of the Day

```bash
nasa apod bajar
```
