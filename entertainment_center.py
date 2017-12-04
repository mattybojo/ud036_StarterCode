""" This module will generate a webpage based on the movies defined within """

import fresh_tomatoes
import media

# create instance of Movie class for each movie
# Movie consists of title, storyline, poster link, and youtube trailer link

super_troopers = media.Movie(
    "Super Troopers",
    "You dont mess with the law. The law messes with you.",
    "https://upload.wikimedia.org/wikipedia/en/1/19/Supertrooper.jpg",
    "https://www.youtube.com/watch?v=2-9D2qUHN-E")

shawshank_redemption = media.Movie(
    "Shawshank Redemption",
    "Fear can hold you prisoner. Hope can set you free.",
    "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg", # noqa
    "https://www.youtube.com/watch?v=6hB3S9bIaco")

forrest_gump = media.Movie(
    "Forrest Gump",
    "Life is like a box of chocolates...you never know what you're gonna get.",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
    "https://www.youtube.com/watch?v=bLvqoHBptjg")

the_matrix = media.Movie(
    "The Matrix",
    "In a world of 1s and 0s... are you a zero, or The One?",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

saving_private_ryan = media.Movie(
    "Saving Private Ryan",
    """There was only one man left in the family, 
    and the mission was to save him.""",
    "https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg", # noqa
    "https://www.youtube.com/watch?v=zwhP5b4tD6g")

the_green_mile = media.Movie(
    "The Green Mile",
    "Paul Edgecomb didn't believe in miracles. Until the day he met one.",
    "https://upload.wikimedia.org/wikipedia/en/e/e2/The_Green_Mile_%28movie_poster%29.jpg", # noqa
    "https://www.youtube.com/watch?v=ctRK-4Vt7dA")

# array of class Movie that is used in creating the web page
movies = [
    super_troopers,
    shawshank_redemption,
    forrest_gump,
    the_matrix,
    saving_private_ryan,
    the_green_mile
]

# create the html file which will contain the movies listed in the movies array
fresh_tomatoes.open_movies_page(movies)
