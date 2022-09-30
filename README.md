# nasa-cli

Command Line Interface made with Typer and Python for NASA API.

## About NASA API

Go to [NASA API](https://api.nasa.gov/) to get started or read [NASA.md](NASA.md).

## Bashrc file

For Fedora Silverblue and start in a toolbox `pjecz-developer`

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

    if [[ "$TOOLBOX_NAME" == "pjecz-developer" ]]
    then
        echo "-- Ejecutar VSCode conectado al toolbox"
        echo "   code ."
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
    else
        echo "1) De no haberlo hecho, ingrese al toolbox"
        echo "   toolbox enter pjecz-developer"
        echo
        echo "2) Ejecute .bashrc"
        echo "   . .bashrc"
        echo
    fi

In KDE Konsole make a profile with this command

    toolbox run --container pjecz-developer /bin/bash --rcfile .bashrc

## Environment variables

Create a configuration file named `.env` in the root directory of the project.

    # Your API key
    API_KEY=****************************************

    # Requests
    TIMEOUT=12

Requires Python 3.10 or later.

    poetry install

Show help

    poetry run python nasa_api/app.py --help
