# 🎬 Movie Collection API

A simple Movie Collection Management API built using FastAPI.

## Features

- Get all movies
- Get movie by ID
- Add a new movie
- Update movie details
- Delete a movie
- Filter movies by genre
- Get available movies
- Get movies by minimum rating
- Get latest movies (sorted by year)

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home |
| GET | /movies | Get all movies |
| GET | /movies/{movie_id} | Get movie by ID |
| POST | /movies | Add a new movie |
| PUT | /movies/{movie_id} | Update a movie |
| DELETE | /movies/{movie_id} | Delete a movie |
| GET | /movies/genre/{genre} | Get movies by genre |
| GET | /movies/available | Get available movies |
| GET | /movies/rating/{rating} | Get movies by rating |
| GET | /movies/latest | Get latest movies |

## Run the Project

#### pip install fastapi uvicorn

#### uvicorn Online_main:app --reload
