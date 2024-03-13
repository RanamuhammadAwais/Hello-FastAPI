# FastAPI Hello World

This is a simple "Hello, World!" project using FastAPI and managed with Poetry.

## Prerequisites

- Python 3.7 or higher
- Poetry (installed globally)

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/fastapi-hello-world.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Hello_fastAPI
    ```

3. Install dependencies using Poetry:

    ```bash
    poetry install
    ```

4. Run the FastAPI application:

    ```bash
    poetry run uvicorn main:app --reload
    ```

5. Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000) to see the Swagger documentation.

## Project Structure

- `main.py`: FastAPI application code.
- `pyproject.toml`: Poetry configuration file.
- `poetry.lock`: Poetry lock file.
- `tests/`: Directory for tests.
