#!/usr/bin/env python2.7
import webbrowser


# Movie class being passed as input the movie_title,
# movie_storyline, launch_date,
# poster_image_url, and trailer_youtube_url
class Movie():
    # initialization
    def __init__(self, movie_title, movie_storyline, launch_date,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.launch_date = launch_date
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # opens trailer on youtube website
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
