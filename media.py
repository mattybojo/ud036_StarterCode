import webbrowser

class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ Initialize the movie class """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Opens the movie trailer in a browser """
        webbrowser.open(self.trailer_youtube_url)