# README

## Installation

### Prerequisites on Windows

1. Install `uv` 
`powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

2. Specifying --python 3.12 ensures uv automatically downloads the correct, stable Python version for Pygame even if you don't have Python installed at all.
`uv venv --python 3.12` 

3. Install the dependencies
`uv pip install -r requirements.txt`

### How to run the game
`uv run pong2.py`

## About activating your environment
- If you use `uv run main.py` ➡️ No activation needed. uv handles it instantly
- If you use `python main.py` ➡️ Activation is required first, otherwise your computer will look for pygame in the global system path and fail.

## If you ever add new requirements or Python libraries
Run `uv pip freeze > requirements.txt`