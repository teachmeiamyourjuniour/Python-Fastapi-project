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
    {"id":1,"title":"Interstellar","director":"Christopher Nolan","genre":"Sci-Fi","year":2014,"rating":8.7,"status":"Available"},
    {"id":2,"title":"Inception","director":"Christopher Nolan","genre":"Sci-Fi","year":2010,"rating":8.8,"status":"Available"},
    {"id":3,"title":"The Dark Knight","director":"Christopher Nolan","genre":"Action","year":2008,"rating":9.0,"status":"Available"},
    {"id":4,"title":"Batman Begins","director":"Christopher Nolan","genre":"Action","year":2005,"rating":8.2,"status":"Available"},
    {"id":5,"title":"Dunkirk","director":"Christopher Nolan","genre":"War","year":2017,"rating":7.8,"status":"Not Available"},
    {"id":6,"title":"Oppenheimer","director":"Christopher Nolan","genre":"Biography","year":2023,"rating":8.5,"status":"Available"},
    {"id":7,"title":"Tenet","director":"Christopher Nolan","genre":"Sci-Fi","year":2020,"rating":7.4,"status":"Available"},
    {"id":8,"title":"Memento","director":"Christopher Nolan","genre":"Mystery","year":2000,"rating":8.4,"status":"Available"},
    {"id":9,"title":"The Prestige","director":"Christopher Nolan","genre":"Drama","year":2006,"rating":8.5,"status":"Available"},
    {"id":10,"title":"Avatar","director":"James Cameron","genre":"Sci-Fi","year":2009,"rating":7.9,"status":"Available"},
    {"id":11,"title":"Avatar: The Way of Water","director":"James Cameron","genre":"Sci-Fi","year":2022,"rating":7.6,"status":"Available"},
    {"id":12,"title":"Titanic","director":"James Cameron","genre":"Romance","year":1997,"rating":7.9,"status":"Available"},
    {"id":13,"title":"The Terminator","director":"James Cameron","genre":"Action","year":1984,"rating":8.1,"status":"Available"},
    {"id":14,"title":"Terminator 2","director":"James Cameron","genre":"Action","year":1991,"rating":8.6,"status":"Available"},
    {"id":15,"title":"John Wick","director":"Chad Stahelski","genre":"Action","year":2014,"rating":7.5,"status":"Available"},
    {"id":16,"title":"John Wick Chapter 2","director":"Chad Stahelski","genre":"Action","year":2017,"rating":7.4,"status":"Available"},
    {"id":17,"title":"John Wick Chapter 3","director":"Chad Stahelski","genre":"Action","year":2019,"rating":7.8,"status":"Available"},
    {"id":18,"title":"John Wick Chapter 4","director":"Chad Stahelski","genre":"Action","year":2023,"rating":8.2,"status":"Available"},
    {"id":19,"title":"Mad Max: Fury Road","director":"George Miller","genre":"Action","year":2015,"rating":8.1,"status":"Available"},
    {"id":20,"title":"Top Gun: Maverick","director":"Joseph Kosinski","genre":"Action","year":2022,"rating":8.3,"status":"Available"},
    {"id":21,"title":"Avengers Endgame","director":"Anthony Russo","genre":"Superhero","year":2019,"rating":8.4,"status":"Available"},
    {"id":22,"title":"Avengers Infinity War","director":"Anthony Russo","genre":"Superhero","year":2018,"rating":8.4,"status":"Available"},
    {"id":23,"title":"Iron Man","director":"Jon Favreau","genre":"Superhero","year":2008,"rating":7.9,"status":"Available"},
    {"id":24,"title":"Captain America Civil War","director":"Anthony Russo","genre":"Superhero","year":2016,"rating":7.8,"status":"Available"},
    {"id":25,"title":"Spider-Man No Way Home","director":"Jon Watts","genre":"Superhero","year":2021,"rating":8.2,"status":"Available"},
    {"id":26,"title":"Black Panther","director":"Ryan Coogler","genre":"Superhero","year":2018,"rating":7.3,"status":"Available"},
    {"id":27,"title":"Doctor Strange","director":"Scott Derrickson","genre":"Fantasy","year":2016,"rating":7.5,"status":"Available"},
    {"id":28,"title":"Thor Ragnarok","director":"Taika Waititi","genre":"Comedy","year":2017,"rating":7.9,"status":"Available"},
    {"id":29,"title":"Guardians of the Galaxy","director":"James Gunn","genre":"Comedy","year":2014,"rating":8.0,"status":"Available"},
    {"id":30,"title":"The Batman","director":"Matt Reeves","genre":"Action","year":2022,"rating":7.8,"status":"Available"},
    {"id":31,"title":"3 Idiots","director":"Rajkumar Hirani","genre":"Comedy","year":2009,"rating":8.4,"status":"Available"},
    {"id":32,"title":"PK","director":"Rajkumar Hirani","genre":"Comedy","year":2014,"rating":8.1,"status":"Available"},
    {"id":33,"title":"Munna Bhai MBBS","director":"Rajkumar Hirani","genre":"Comedy","year":2003,"rating":8.1,"status":"Available"},
    {"id":34,"title":"Dangal","director":"Nitesh Tiwari","genre":"Sports","year":2016,"rating":8.3,"status":"Available"},
    {"id":35,"title":"Lagaan","director":"Ashutosh Gowariker","genre":"Drama","year":2001,"rating":8.1,"status":"Available"},
    {"id":36,"title":"Taare Zameen Par","director":"Aamir Khan","genre":"Drama","year":2007,"rating":8.3,"status":"Available"},
    {"id":37,"title":"Zindagi Na Milegi Dobara","director":"Zoya Akhtar","genre":"Drama","year":2011,"rating":8.2,"status":"Available"},
    {"id":38,"title":"Bajrangi Bhaijaan","director":"Kabir Khan","genre":"Drama","year":2015,"rating":8.1,"status":"Available"},
    {"id":39,"title":"Sholay","director":"Ramesh Sippy","genre":"Action","year":1975,"rating":8.2,"status":"Available"},
    {"id":40,"title":"Swades","director":"Ashutosh Gowariker","genre":"Drama","year":2004,"rating":8.2,"status":"Available"},
    {"id":41,"title":"The Shawshank Redemption","director":"Frank Darabont","genre":"Drama","year":1994,"rating":9.3,"status":"Available"},
    {"id":42,"title":"The Godfather","director":"Francis Ford Coppola","genre":"Crime","year":1972,"rating":9.2,"status":"Available"},
    {"id":43,"title":"The Godfather Part II","director":"Francis Ford Coppola","genre":"Crime","year":1974,"rating":9.0,"status":"Available"},
    {"id":44,"title":"Pulp Fiction","director":"Quentin Tarantino","genre":"Crime","year":1994,"rating":8.9,"status":"Available"},
    {"id":45,"title":"Fight Club","director":"David Fincher","genre":"Drama","year":1999,"rating":8.8,"status":"Available"},
    {"id":46,"title":"Forrest Gump","director":"Robert Zemeckis","genre":"Drama","year":1994,"rating":8.8,"status":"Available"},
    {"id":47,"title":"The Matrix","director":"The Wachowskis","genre":"Sci-Fi","year":1999,"rating":8.7,"status":"Available"},
    {"id":48,"title":"Gladiator","director":"Ridley Scott","genre":"Action","year":2000,"rating":8.5,"status":"Available"},
    {"id":49,"title":"The Lord of the Rings: The Fellowship of the Ring","director":"Peter Jackson","genre":"Fantasy","year":2001,"rating":8.9,"status":"Available"},
    {"id":50,"title":"The Lord of the Rings: The Two Towers","director":"Peter Jackson","genre":"Fantasy","year":2002,"rating":8.8,"status":"Available"},
    {"id":51,"title":"The Lord of the Rings: The Return of the King","director":"Peter Jackson","genre":"Fantasy","year":2003,"rating":9.0,"status":"Available"},
    {"id":52,"title":"The Silence of the Lambs","director":"Jonathan Demme","genre":"Thriller","year":1991,"rating":8.6,"status":"Available"},
    {"id":53,"title":"Se7en","director":"David Fincher","genre":"Thriller","year":1995,"rating":8.6,"status":"Available"},
    {"id":54,"title":"Parasite","director":"Bong Joon-ho","genre":"Thriller","year":2019,"rating":8.5,"status":"Available"},
    {"id":55,"title":"Joker","director":"Todd Phillips","genre":"Drama","year":2019,"rating":8.4,"status":"Available"},
    {"id":56,"title":"Whiplash","director":"Damien Chazelle","genre":"Drama","year":2014,"rating":8.5,"status":"Available"},
    {"id":57,"title":"The Social Network","director":"David Fincher","genre":"Biography","year":2010,"rating":7.8,"status":"Available"},
    {"id":58,"title":"The Wolf of Wall Street","director":"Martin Scorsese","genre":"Biography","year":2013,"rating":8.2,"status":"Available"},
    {"id":59,"title":"The Green Mile","director":"Frank Darabont","genre":"Drama","year":1999,"rating":8.6,"status":"Available"},
    {"id":60,"title":"Saving Private Ryan","director":"Steven Spielberg","genre":"War","year":1998,"rating":8.6,"status":"Not Available"},
    {"id":61,"title":"Schindler's List","director":"Steven Spielberg","genre":"Biography","year":1993,"rating":9.0,"status":"Available"},
    {"id":62,"title":"Jurassic Park","director":"Steven Spielberg","genre":"Adventure","year":1993,"rating":8.2,"status":"Available"},
    {"id":63,"title":"Jaws","director":"Steven Spielberg","genre":"Thriller","year":1975,"rating":8.1,"status":"Available"},
    {"id":64,"title":"The Lion King","director":"Roger Allers","genre":"Animation","year":1994,"rating":8.5,"status":"Available"},
    {"id":65,"title":"Toy Story","director":"John Lasseter","genre":"Animation","year":1995,"rating":8.3,"status":"Available"},
    {"id":66,"title":"Finding Nemo","director":"Andrew Stanton","genre":"Animation","year":2003,"rating":8.2,"status":"Available"},
    {"id":67,"title":"Coco","director":"Lee Unkrich","genre":"Animation","year":2017,"rating":8.4,"status":"Available"},
    {"id":68,"title":"Inside Out","director":"Pete Docter","genre":"Animation","year":2015,"rating":8.1,"status":"Available"},
    {"id":69,"title":"Up","director":"Pete Docter","genre":"Animation","year":2009,"rating":8.3,"status":"Available"},
    {"id":70,"title":"Soul","director":"Pete Docter","genre":"Animation","year":2020,"rating":8.0,"status":"Available"},
    {"id":71,"title":"The Conjuring","director":"James Wan","genre":"Horror","year":2013,"rating":7.5,"status":"Available"},
    {"id":72,"title":"Insidious","director":"James Wan","genre":"Horror","year":2010,"rating":6.8,"status":"Available"},
    {"id":73,"title":"A Quiet Place","director":"John Krasinski","genre":"Horror","year":2018,"rating":7.5,"status":"Available"},
    {"id":74,"title":"Get Out","director":"Jordan Peele","genre":"Horror","year":2017,"rating":7.8,"status":"Available"},
    {"id":75,"title":"The Exorcist","director":"William Friedkin","genre":"Horror","year":1973,"rating":8.1,"status":"Available"},
    {"id":76,"title":"RRR","director":"S. S. Rajamouli","genre":"Action","year":2022,"rating":7.8,"status":"Available"},
    {"id":77,"title":"Baahubali: The Beginning","director":"S. S. Rajamouli","genre":"Action","year":2015,"rating":8.0,"status":"Available"},
    {"id":78,"title":"Baahubali 2: The Conclusion","director":"S. S. Rajamouli","genre":"Action","year":2017,"rating":8.2,"status":"Available"},
    {"id":79,"title":"Pushpa: The Rise","director":"Sukumar","genre":"Action","year":2021,"rating":7.6,"status":"Available"},
    {"id":80,"title":"Pushpa 2: The Rule","director":"Sukumar","genre":"Action","year":2024,"rating":7.8,"status":"Available"},
    {"id":81,"title":"Kantara","director":"Rishab Shetty","genre":"Action","year":2022,"rating":8.3,"status":"Available"},
    {"id":82,"title":"Vikram","director":"Lokesh Kanagaraj","genre":"Action","year":2022,"rating":8.3,"status":"Available"},
    {"id":83,"title":"Leo","director":"Lokesh Kanagaraj","genre":"Action","year":2023,"rating":7.2,"status":"Available"},
    {"id":84,"title":"Jailer","director":"Nelson Dilipkumar","genre":"Action","year":2023,"rating":7.1,"status":"Available"},
    {"id":85,"title":"Master","director":"Lokesh Kanagaraj","genre":"Action","year":2021,"rating":7.4,"status":"Available"},
    {"id":86,"title":"Drishyam","director":"Nishikant Kamat","genre":"Thriller","year":2015,"rating":8.2,"status":"Available"},
    {"id":87,"title":"Drishyam 2","director":"Abhishek Pathak","genre":"Thriller","year":2022,"rating":8.2,"status":"Available"},
    {"id":88,"title":"Andhadhun","director":"Sriram Raghavan","genre":"Thriller","year":2018,"rating":8.2,"status":"Available"},
    {"id":89,"title":"Article 15","director":"Anubhav Sinha","genre":"Crime","year":2019,"rating":8.1,"status":"Available"},
    {"id":90,"title":"Gangs of Wasseypur","director":"Anurag Kashyap","genre":"Crime","year":2012,"rating":8.2,"status":"Available"},
    {"id":91,"title":"Rockstar","director":"Imtiaz Ali","genre":"Romance","year":2011,"rating":7.7,"status":"Available"},
    {"id":92,"title":"Barfi!","director":"Anurag Basu","genre":"Romance","year":2012,"rating":8.1,"status":"Available"},
    {"id":93,"title":"Chhichhore","director":"Nitesh Tiwari","genre":"Comedy","year":2019,"rating":8.3,"status":"Available"},
    {"id":94,"title":"Bhool Bhulaiyaa","director":"Priyadarshan","genre":"Comedy","year":2007,"rating":7.5,"status":"Available"},
    {"id":95,"title":"Hera Pheri","director":"Priyadarshan","genre":"Comedy","year":2000,"rating":8.2,"status":"Available"},
    {"id":96,"title":"Phir Hera Pheri","director":"Neeraj Vora","genre":"Comedy","year":2006,"rating":7.3,"status":"Available"},
    {"id":97,"title":"The Kashmir Files","director":"Vivek Agnihotri","genre":"Drama","year":2022,"rating":8.3,"status":"Available"},
    {"id":98,"title":"Sita Ramam","director":"Hanu Raghavapudi","genre":"Romance","year":2022,"rating":8.5,"status":"Available"},
    {"id":99,"title":"K.G.F: Chapter 1","director":"Prashanth Neel","genre":"Action","year":2018,"rating":8.2,"status":"Available"},
    {"id":100,"title":"12th Fail","director":"Vidhu Vinod Chopra","genre":"Biography","year":2023,"rating":9.0,"status":"Available"}
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