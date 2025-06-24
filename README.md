# Astana-Energia Technical Docs API

This project is a FastAPI-based REST API for managing technical maintenance documentation at TPP-2 site of Astana-Energia.

## Features

- Add new maintenance records
- Retrieve all records
- Search records by ID
- Delete outdated entries

## Tech Stack

- Python + FastAPI
- SQLite
- Swagger UI for docs

## Getting Started

```bash
pip install -r requirements.txt
uvicorn main:app --reload
