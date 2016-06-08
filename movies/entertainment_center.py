import media
import fresh_tomatoes

silence_of_the_lambs = media.Movie("Silence of the Lambs",
                                   "A young F.B.I. cadet must confide in an incarcerated and manipulative killer to receive his help on catching another serial killer who skins his victims.",
                                   "http://ia.media-imdb.com/images/M/MV5BMTQ2NzkzMDI4OF5BMl5BanBnXkFtZTcwMDA0NzE1NA@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                   "https://www.youtube.com/watch?v=RuX2MQeb8UM")

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

forrest_gump = media.Movie("Forest Gump",
                           "A man with a low IQ has accomplished great things in his life and been present during significant historic events - in each case, far exceeding what anyone imagined he could do. Yet, despite all the things he has attained, his one true love eludes him. 'Forrest Gump' is the story of a man who rose above his challenges, and who proved that determination, courage, and love are more important than ability.",
                           "https://image.tmdb.org/t/p/w185/z4ROnCrL77ZMzT0MsNXY5j25wS2.jpg",
                           "https://www.youtube.com/watch?v=uPIEn0M8su0")

school_of_rock = media.Movie("School of Rock",
                             "This is the storyline",
                             "https://image.tmdb.org/t/p/w185/cREN222Yw78zvSQ9bg17Y9QZS0c.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc") 

ratatouille = media.Movie("Ratatouille",
                          "This is the storyline",
                          "https://image.tmdb.org/t/p/w185/y8y6Fv0k068OnHBZtu949A1t6pj.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "This is the storyline",
                                "https://image.tmdb.org/t/p/w185/xxSopLYATHXSepXcEaBh9Gazv6p.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                           "This is the storyline",
                           "https://image.tmdb.org/t/p/w185/tAhSyLxpaZJCr1oc2a3flvC2B7x.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [silence_of_the_lambs, toy_story, avatar, forrest_gump, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)

