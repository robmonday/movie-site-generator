import media
import fresh_tomatoes

# Create movie instances

toy_story = media.Movie("Toy Story", 5, "A story of a boy and his toys that come to life, and the adventures they find","http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4")
#print toy_story.storyline
#toy_story.show_trailer()

avatar = media.Movie("Avatar", 10, "A marine on an alien planet, learns how to survive and fights for his way of life","http://imgs.abduzeedo.com/files/articles/Avatar/4154691413_a695e033a8_o.jpg","https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print avatar.storyline
#avatar.show_trailer()

back_to_the_future = media.Movie("Back to the Future", 30, "A boy and his crazy scientist companion travel through time","https://c1.staticflickr.com/3/2363/2054915970_1d8aa51863.jpg","https://www.youtube.com/watch?v=JWyOC4n4qSc")
#print back_to_the_future.storyline
#back_to_the_future.show_trailer()

monty_python = media.Movie("Monty Python and the Holy Grail", 60, "This is a crazy movie about the inquisition and a bunch of blithering idiots.","http://lsc.mit.edu/schedule/2014.2q/poster-montypythonandtheholygrail.jpg","https://www.youtube.com/watch?v=LG1PlkURjxE")

indiana_jones = media.Movie("Indian Jones and the Temple of Doom", 60, "Adventurer archaeologist Indiana Jones gets more than he bargained for","http://www.gstatic.com/tv/thumb/movieposters/9614/p9614_p_v8_ae.jpg","https://www.youtube.com/watch?v=HOwWfns4qqw")

fresh_tomatoes.open_movies_page([toy_story, avatar, back_to_the_future, monty_python, indiana_jones]) # generate webpage using movie objects created

# Code for TV shows - left over from exercises but not needed for project

# seinfeld = media.TvShow("Seinfeld", 30, 1, 1, 13)
# sesame_street = media.TvShow("Sesame Street", 28, 2, 3, 23)
# tv_shows = [seinfeld, sesame_street]

# print media.Movie.VALID_RATINGS
# print (media2.Movie.__doc__)
# print (media2.Movie.__name__)
# print (media2.Movie.__module__)

# toy_story.display_info()
# sesame_street.display_info()
