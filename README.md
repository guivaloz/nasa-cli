# nasa-cli

Command Line Interface made with Typer and Python for NASA API.

## About NASA API

Go to [NASA API](https://api.nasa.gov/).

## Installation

Create a virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

Install the required packages:

```bash
pip install poetry
poetry install
```

## Usage

Activate the virtual environment if not already activated:

```bash
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate
```

Download APOD (Astronomy Picture of the Day):

```bash
nasa_cli apod bajar
```

Download a date range of APODs:

```bash
nasa_cli apod bajar-rango --desde 2025-11-01 --hasta 2025-11-30
```
