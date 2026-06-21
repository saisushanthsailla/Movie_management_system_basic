from fastapi import FastAPI,Body,Query

app = FastAPI()

movies = [
    {"id": 1, "movie_name": "Inception", "genre": "Sci-Fi", "language": "English", "rating": 9},
    {"id": 2, "movie_name": "RRR", "genre": "Action", "language": "Telugu", "rating": 8},
    {"id": 3, "movie_name": "Interstellar", "genre": "Sci-Fi", "language": "English", "rating": 9},
    {"id": 4, "movie_name": "Baahubali", "genre": "Action", "language": "Telugu", "rating": 9},
    {"id": 5, "movie_name": "3 Idiots", "genre": "Comedy", "language": "Hindi", "rating": 9},
]



@app.get("/Movies")
def View_All_Movies():
    return movies

@app.get("/filter")
def filter_movies(
    genre : str = Query(None),
    language : str = Query(None),
    rating : int = Query(None)
    ):
    filtered_movies = movies
    if genre :
        filter_movies = [movie for movie in filtered_movies  if movie["genre"] == genre]
        
    if language :
        filter_movies = [movie for movie in filtered_movies  if movie["language"] == language]
        
    if rating :
        filter_movies = [movie for movie in filtered_movies  if movie["rating"] >= rating]
    return filter_movies


@app.post("/addmovie")
def add_movie(new_movie_details = Body()) :
    movies.append(new_movie_details)
    return {"message" : "New movie added"}

@app.put("/updatemovie/{id}")
def update_movie(id : int,updated_body = Body()) :
    for movie in movies :
        if movie["id"] == id :
            movie.update(updated_body)
            return {"message" : "Movie Updated Sucessfully"}
    return {"message" : "Movie Not Found"}


@app.delete("/deletemovie/{id}")
def delete_movie(id : int) :
    for index,movie in enumerate(movies) :
        if movie["id"] == id :
            movies.pop(index)
            return {"message" : "Movie Deleted Sucessfully"}
    
    return {"message" : "Movie Not Found"}

    
    