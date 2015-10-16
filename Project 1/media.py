import webbrowser

class Movie(): 	 
	"""Movie() is the blueprint for our movie posters.
    Attributes:
       show_trailer: uses the import webbrowser to open 
       our youtube url. 
    """
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, reason):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.reason_to_watch = reason

	def show_trailer(self): 
		webbrowser.open(self.trailer_youtube_url)