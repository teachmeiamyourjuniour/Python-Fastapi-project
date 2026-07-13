from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Movie(BaseModel):
    id: int 
    title: str
    director: str
    genre: str
    year: int
    rating: float
    status: str

movies = [
    {
        "id": 1,
        "title": "Interstellar",
        "director": "Christopher Nolan",
        "genre": "Sci-Fi",
        "year": 2014,
        "rating": 8.7,
        "status": "Available"
    },
    {
        "id": 2,
        "title": "3 Idiots",
        "director": "Rajkumar Hirani",
        "genre": "Comedy",
        "year": 2009,
        "rating": 8.4,
        "status": "Available"
    },
    {
        "id": 3,
        "title": "John Wick",
        "director": "Chad Stahelski",
        "genre": "Action",
        "year": 2014,
        "rating": 7.5,
        "status": "Not Available"
    },
    {
        "id": 4,
        "title": "KGF Chapter 2",
        "director": "Prashanth Neel",
        "genre": "Action",
        "year": 2022,
        "rating": 8.3,
        "status": "Available"
    },
    {
        "id": 5,
        "title": "Inception",
        "director": "Christopher Nolan",
        "genre": "Sci-Fi",
        "year": 2010,
        "rating": 8.8,
        "status": "Available"
    }
]

@app.get(
    "/",
    summary="Home Page",
    description="Displays a welcome message for the Movie Collection API."
)
def home():
    return {"message": "Welcome to Movie Collection API"}

@app.get("/movies",
    summary="Get all movies",
    description="Returns a list of all movies available in the collection.")
def get_movies():
    return movies

@app.get(
    "/movies/{movie_id}",
    summary="Get movie by ID",
    description="Returns the details of a movie using its unique ID."
)
def get_movie(movie_id: int):
    for movie in movies:
        if movie["id"]==movie_id:
            return movie
    return{"message": "Movie not found"}

@app.post(
    "/movies",
    summary="Add a new movie",
    description="Adds a new movie to the movie collection."
)
def add_movie(movie: Movie):
    movies.append(movie.dict())
    return{
        "message": "Movie Added Successfully",
        "movie": movie
    }

@app.put(
    "/movies/{movie_id}",
    summary="Update movie",
    description="Updates the information of an existing movie."
)
def update_movie(movie_id: int,updated_movie: Movie):
    for index, movie in enumerate(movies):
        movies[index] = updated_movie.dict()
        return{
            "message":"Movie Updated Successfully",
            "movie": updated_movie
        }
    return{"message":"Movie Not Found"}

@app.delete(
    "/movies/{movie_id}",
    summary="Delete movie",
    description="Deletes a movie from the collection using its ID."
)
def delete_movie(movie_id: int):
    for movie in movies:
        if movie["id"]==movie_id:
            movie.remove(movie)
            return{
                "message":"Movie deleted sucessfully"
            }
    return{
        "message":"Movie Not Found (>_<)!!"
    }

@app.get(
    "/movies/genre/{genre}",
    summary="Get movies by genre",
    description="Returns a list of movies belonging to a specific genre."
)
def get_movies_by_genre(genre: str):
    genre_movies = [movie for movie in movies if movie["genre"].lower() == genre.lower()]
    if genre_movies:
        return genre_movies
    return {"message": "No movies found in this genre."}

@app.get(
    "/movies/available",
    summary="Get available movies",
    description="Returns a list of all available movies in the collection."
)
def get_available_movies():
    available_movies = [movie for movie in movies if movie["status"].lower() == "available"]
    if available_movies:
        return available_movies
    return {"message": "No available movies found."}

@app.get(
    "/movies/rating/{rating}",
    summary="Get movies by rating",
    description="Returns a list of movies with a rating equal to or higher than the specified value."
)
def get_movies_by_rating(rating: float):
    rating_movies = [movie for movie in movies if movie["rating"] >= rating]
    if rating_movies:
        return rating_movies
    return {"message": "No movies found with this rating or higher."}

@app.get(
    "/movies/latest",
    summary="Get latest movies",
    description="Returns a list of the latest movies in the collection."
)
def get_latest_movies():
    latest_movies = sorted(movies, key=lambda x: x["year"], reverse=True)
    return latest_movies

@app.get(
    "/movies/director/{director}",
    summary="Get movies by director",
    description="Returns a list of movies directed by a specific director."
)
def get_movies_by_director(director: str):
    director_movies = [movie for movie in movies if movie["director"].lower() == director.lower()]
    if director_movies:
        return director_movies
    return {"message": "No movies found by this director."}