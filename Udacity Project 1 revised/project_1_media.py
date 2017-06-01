import webbrowser
# imports the webbrowser module from PSL(python standard library)


class Movie():
    """This class holds the information
    required to create different instances"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # different ratings that can be applied to movies

    def __init__(
        self, movie_title, movie_story_line,
        poster_image, trailer_youtube_url
    ):
            self.title = movie_title
            self.storyline = movie_story_line
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube_url
"""this function opens the webbrowser to
the youtube url specified in each instance"""


def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
