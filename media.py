import webbrowser

class Video():
	"""This class provides a way of storing basic video information including title and duration"""
	def __init__(self, video_title, video_duration):
		self.video_title = video_title
		self.video_duration = video_duration

	def display_info(self):
		print "Video title:  " + self.video_title
		print "Video duration:  " + str(self.video_duration)

class TvShow(Video):
	"""This class provides a way to store TV show information"""
	VALID_RATINGS = ['TV-G','TV-PG','TV-14','TV-MA'] # class variable reflecting valid ratings for TV shows

	def __init__(self, video_title, video_duration, tv_season, tv_episode, tv_station):
		self.tv_season = tv_season
		self.tv_episode = tv_episode
		self.tv_station = tv_station
		Video.__init__(self,video_title, video_duration)

	def get_local_listing(self,):
		print("getting local listing now...")


class Movie(Video):
	"""This class provides a way to store movie related information"""
	VALID_RATINGS = ['G','PG','PG-13','R'] # class variable reflecting valid ratings for movies

	def __init__(self, video_title, video_duration, movie_storyline, poster_image_url, trailer_youtube_url):
		self.movie_storyline = movie_storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		Video.__init__(self,video_title, video_duration)

	def show_trailer(self,):
		webbrowser.open(self.trailer_youtube_url)

	def display_info(self):
		print "Video title:  " + self.video_title
		print "Video duration:  " + str(self.video_duration)
		print "Movie storyline:  " + str(self.movie_storyline)




