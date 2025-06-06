import typer
from utils.api import Tmdb
from .models import json_to_movies

"""
Fetch and display a list of movies from the TMDB based non the specified type.
Supported types: popular, playing, top, upcoming, or all (if no type is provided)
"""

# Initialize the TMDB API client and the Typer CLI app
tmdb = Tmdb()
tmdb_api = typer.Typer()

@tmdb_api.command()
def movies(type: str = typer.Option(None, help="Movie according to TMDB")):

    # Fetch movies based on the given type
    if type == "popular":
        movies = json_to_movies(tmdb.get_popular_movies())
    
    if type == "playing":
        movies = json_to_movies(tmdb.get_now_playing_movies())

    if type == "top":
        movies = json_to_movies(tmdb.get_top_rated_movies())
    
    if type == "upcoming":
        movies = json_to_movies(tmdb.get_upcoming_movies())
    
    if not type:
        # Default case: fetch a general list of movies
        movies = json_to_movies(tmdb.get_movies())
    
    for movie in movies:
        print(f"-> {movie}")
