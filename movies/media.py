import webbrowser


class Movie():
    """ This class provides a way to store movie related information"""

    # valid ratings constants.  will be used in future ratings functionality
    VALID_RATINGS = ["G", "PG", "PG-13", "R", "XXX"]

    # constructor for this class.  creates an instance of a movie
    def __init__(self, title, storyline, poster_image_url, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_url
    
    # function to open the trailer assigned to this movie
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
