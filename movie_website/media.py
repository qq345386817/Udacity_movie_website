import webbrowser

"""
    Class Video is the super class of Movie.
    Class Movie will store the information for each movie created in
    entertainment center.
"""

class Video():
    """Video contains title and duration."""
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    '''Movie store the storyline, poster_image_url and trailer_youtube_url.'''
    def __init__(self, title, duration, storyline, poster_image_url, trailer_youtube_url):
        Video.__init__(self, title, duration)
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
