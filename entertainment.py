import media
import fresh_tomatoes

# instantiates 3 movies
la_la_land = media.Movie("La La Land",
                         "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_(film).png",
                         "https://youtu.be/0pdqf4P9MB8")

captain_america = media.Movie("Captain America: Civil War",
                              "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
                              "https://youtu.be/dKrVegVI0Us")

star_wars = media.Movie("Rogue One: A Star Wars Story",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",
                        "https://youtu.be/frdj1zb9sMY")

# adds the movies to an array
movies = [la_la_land, captain_america, star_wars]

# calls function on fresh_tomatoes.py to render the movies
fresh_tomatoes.open_movies_page(movies)