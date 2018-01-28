#!/usr/bin/env python2.7

import media
import fresh_tomatoes


# create instances of movies for each favorite
# movie to be displayed on website
aliens = media.Movie('Aliens',
                     'Woman takes on aliens to save child.',
                     'July 18, 1986',
                     'http://bit.ly/2rLOGif',
                     'https://www.youtube.com/watch?v=XKSQmYUaIyE')

princess_bride = media.Movie('The Princess Bride',
                             'Classic love story with a twist.',
                             'September 25, 1987',
                             'http://bit.ly/2ByMkCY',
                             'https://www.youtube.com/watch?v=VYgcrny2hRs')

the_matrix = media.Movie('The Matrix',
                         'Future world with humans as batteries.',
                         'March 31, 1999',
                         'http://bit.ly/2rOWCzi',
                         'https://www.youtube.com/watch?v=m8e-FF8MsqU')

holy_grail = media.Movie('Monty Python and the Holy Grail',
	                     'Monty Python take on the King Arthur legend.',
                         'March 14, 1975',
                         'http://bit.ly/2nhD95D',
                         'https://www.youtube.com/watch?v=LG1PlkURjxE')

iron_man = media.Movie('Iron Man',
                       'Genius in suit saves the world.',
                       'May 2, 2008',
                       'http://bit.ly/2rLG8b8',
                       'https://www.youtube.com/watch?v=8hYlB38asDY')

conan = media.Movie('Conan the Barbarian',
                    'Barbarian takes on sorcerer.',
                    'May 14, 1982',
                    'http://bit.ly/2DJlNow',
                    'https://www.youtube.com/watch?v=xwdYd_RdLCQ')

#create list of movies information based on instances created above
favorite_movies = [aliens, princess_bride, the_matrix,
                   holy_grail, iron_man, conan]

#execute code to create html web page based on list of movies
fresh_tomatoes.open_movies_page(favorite_movies)
