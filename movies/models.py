# Class representing a movie with basic details
class Movie():
    def __init__(self):
        # Initialize default values for a movie
        self.title = ""
        self.release_date = ""
    
    def set_title(self, title):
        # Set the movie's title
        self.title = title
        return self

    def set_release_date(self, release_date):
        # Set the movie's release date
        self.release_date = release_date
        return self
    
    def __str__(self):
        # String representation of the movie
        return f"{self.title} [{self.release_date}]"

# Convert a JSON response into a list of Movie Objects
def json_to_movies(json):
    movies = []
    for movie in json["results"]:
        # Create a Movie object using data from each result
        m = Movie().set_title(movie["title"]).set_release_date(movie["release_date"])
        movies.append(m)
    return movies