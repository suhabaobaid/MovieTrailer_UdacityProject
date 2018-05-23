import fresh_tomatoes
from media import Movie

mulan = Movie(
    "Mulan",
    "https://i.ytimg.com/vi/TjEREWejqic/movieposter.jpg",
    "https://youtu.be/RCKMhc_f1rg")

titanic = Movie(
    "Titanic",
    """https://images-na.ssl-images-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@.
    _V1_UX182_CR0,0,182,268_AL_.jpg""",
    "https://youtu.be/zCy5WQ9S4c0")

everything = Movie(
    "The theory of everything",
    """"https://images-na.ssl-images-amazon.com/images/M/MV5BMTAwMTU4MDA3NDNeQTJeQWpwZ15BbWU4MDk4NTMxNTIx.
    _V1_UX182_CR0,0,182,268_AL_.jpg""",
    "https://youtu.be/Salz7uGp72c")

beautiful_mind = Movie(
    "Beautiful Mind",
    "https://images.gr-assets.com/books/1347807703l/13912.jpg",
    "https://www.youtube.com/watch?v=aS_d0Ayjw4o")


movies = [mulan, titanic, everything, beautiful_mind]

# to start the program, use the main function in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
