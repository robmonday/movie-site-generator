import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life","http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4")

#print toy_story.storyline
#toy_story.show_trailer()

avatar = media.Movie("Avatar","A marine on an alien planet","http://imgs.abduzeedo.com/files/articles/Avatar/4154691413_a695e033a8_o.jpg","https://www.youtube.com/watch?v=d1_JBMrrYw8")

#print avatar.storyline
#avatar.show_trailer()

back_to_the_future = media.Movie("Back to the Future","A boy and his crazy scientist companion travel through time","https://c1.staticflickr.com/3/2363/2054915970_1d8aa51863.jpg","https://www.youtube.com/watch?v=JWyOC4n4qSc")
#print back_to_the_future.storyline
#back_to_the_future.show_trailer()

movies = [toy_story, avatar, back_to_the_future]
#fresh_tomatoes.open_movies_page(movies)

#print media.Movie.VALID_RATINGS
print (media.Movie.__doc__)
print (media.Movie.__name__)
print (media.Movie.__module__)