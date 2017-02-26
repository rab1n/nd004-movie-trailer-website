import media
import fresh_tomatoes

# Creating multiple instances of that Python Class to represent my favorite movies.

la_la_land = media.Movie("La La Land",
                         "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_(film).png",
                         "https://youtu.be/0pdqf4P9MB8",
                         "The story of an aspiring actress and a jazz musician pursuing their dreams.")

captain_america = media.Movie("Captain America: Civil War",
                              "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
                              "https://youtu.be/dKrVegVI0Us",
                              "An American superhero film based on the Marvel Comics character Captain America."
                              )

star_wars = media.Movie("Rogue One: A Star Wars Story",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",
                        "https://youtu.be/frdj1zb9sMY",
                        "Rogue One follows a group of rebels on a mission to steal the plans for the Death Star.")

#  Grouping all the instances together in a list.
movies = [la_la_land, captain_america, star_wars]

# This function call opens a page of movies generated from the input, an array of movie instances.
fresh_tomatoes.open_movies_page(movies)