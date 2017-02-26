import webbrowser


class Movie():
    """This class serves as a data structure to store one's favorite movies, including movie title, poster URL,
     YouTube link to the movie trailer and it's storyline."""

    def __init__(self, title, poster_image_url, trailer_youtube_url, storyline):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.storyline = storyline