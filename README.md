# gRPC App

gRPC App

## Setup Virtual Environment

- How to set up?
  ```bash
  python3.13 -m venv .venv
  ```

## How to set up?

- How to install dependencies?
  ```bash
  pip install -e ".[automation,sqlite,test]"  # On the Local machine
  ```

## How to build proto files?

- How to build proto files?
  ```bash
  sh scripts/build_proto.sh
  ```

## How to run a development server?

- Run the development server.
  ```bash
  python -m app.grpc
  ```

## Migrations

- Make migration files
  ```bash
  alembic revision --autogenerate -m "Your message here"
  ```
- Migrate
  ```bash
  alembic upgrade head
  ```

## How to build an image for deployment?

- Use the following command to build deployable image.
  ```bash
  docker build -t app:$(python -c "from app import __version__;print(__version__)") .
  ```
