#!/usr/bin/env python2.7

import media
import fresh_tomatoes


# create instances of movies for each favorite
# movie to be displayed on website
aliens = media.Movie('Aliens',
    'Woman takes on aliens to save child.',
    'July 18, 1986',
    'https://upload.wikimedia.org/wikipedia/en/f/fb/Aliens_poster.jpg',
    'https://www.youtube.com/watch?v=XKSQmYUaIyE')

princess_bride = media.Movie('The Princess Bride',
    'Classic love story with a twist.',
    'September 25, 1987',
    'https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg',
    'https://www.youtube.com/watch?v=njZBYfNpWoE')

the_matrix = media.Movie('The Matrix',
    'Future world with humans as batteries.',
    'March 31, 1999',
    'https://upload.wikimedia.org/wikipedia/sco/c/c1/The_Matrix_Poster.jpg',                      
    'https://www.youtube.com/watch?v=vKQi3bBA1y8')

holy_grail = media.Movie('Monty Python and the Holy Grail',
	'Monty Python take on the King Arthur legend.',
	'March 14, 1975',
	'http://bit.ly/2nhD95D',
	'https://www.youtube.com/watch?v=LG1PlkURjxE')

iron_man = media.Movie('Iron Man',
	'Genius in suit saves the world.',
	'May 2, 2008',
	'https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG',
	'https://www.youtube.com/watch?v=8hYlB38asDY')

conan = media.Movie('Conan the Barbarian',
	'Barbarian takes on sorcerer.',
	'May 14, 1982',
	'http://bit.ly/2DJlNow',
	'https://www.youtube.com/watch?v=xwdYd_RdLCQ')

favorite_movies = [aliens, princess_bride, the_matrix, holy_grail, iron_man, conan]

fresh_tomatoes.open_movies_pages(favorite_movies)
