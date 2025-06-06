from decouple import config
import requests

TMDB_API_KEY = config("TMDB_API_KEY")

# Class to interact with TMDB API 
class Tmdb():
    def __init__(self):
        # Base URL for TMDB and headers for API authentication
        self.url = "https://www.themoviedb.org"
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {TMDB_API_KEY}"
        }
    
    def get_movies(self) -> dict:
        # Fetch a list of trending movies
        url = f"{self.url}/3/trending/movie/day?language=es-ES"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_popular_movies(self, page: int = 1) -> dict:
        # Fetch a list of popular movies
        url = f"{self.url}/3/trending/popular/day?language=es-ES&page={page}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_now_playing_movies(self, page: int = 1) -> dict:
        url = f"{self.url}/3/movie/now_playing?language=es-ES&page={page}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_top_rated_movies(self, page: int = 1) -> dict:
        url = f"{self.url}/3/movie/top_rated?language=es-ES&page={page}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_upcoming_movies(self, page: int = 1) -> dict:
        url = f"{self.url}/3/movie/upcoming?language=es-ES&page={page}"
        response = requests.get(url, headers=self.headers)
        return response.json()
