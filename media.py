class Movie:
    ''' Class to hold the information of each movie

    Attributes:
        title: A string containing the name of the movie
        poster_image_url: a string containing the url of the movie image
        trailer_youtube_url: a string containing the url of the movie trailer
        (mainly youtube url)
    '''

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
