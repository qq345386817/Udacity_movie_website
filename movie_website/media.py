import webbrowser

class Video():
    """docstring for video"""
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    '''docstring for Movie'''
    def __init__(self, title, duration, storyline, poster_image_url, trailer_youtube_url):
        Video.__init__(self, title, duration)
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
