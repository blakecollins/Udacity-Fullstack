import fresh_tomatoes
import media

# entertainment_center.py holds all of our variables pertaining
# to our movie posters. Each variable holds a title, a description
# a url to a movie poster, a url to a trailer, and a reason to watch.
# All of this gets stored in an array called movies. 

labyrinth = media.Movie("Labyrinth", 
						"A day in the life of David Bowie",
						"https://upload.wikimedia.org/wikipedia/en/6/6b/Labyrinth_ver2.jpg",
						"https://www.youtube.com/watch?v=XRcOZZDvMv4",
						"Jim Henson was a genius and David Bowie has something crazy going on with his pants.")

dark_crystal = media.Movie("The Dark Crystal", 
						   "Mutant turkeys try to stop a boy from fixing their magic stone.",
						   "https://upload.wikimedia.org/wikipedia/en/7/77/The_Dark_Crystal_Film_Poster.jpg",
						   "https://www.youtube.com/watch?v=wW23YcaBHUg",
						   "It's weird, dark, and another Jim Henson masterpiece")

dredd = media.Movie("Dredd", 
					"Judge, jury, and executioner - he brings to law to a giant apartment complex.",
					"https://upload.wikimedia.org/wikipedia/en/1/16/Dredd2012Poster.jpg",
					"https://www.youtube.com/watch?v=G-eI5oLlIeY",
					"Intense action set in a dystopia future. Karl Urban's best role.")

willy_wonka_chocolate_factory = media.Movie("Willy Wonka and the Chocolate Factory", 
											"Like Saw but with a chocolate factory and children.",
											"https://upload.wikimedia.org/wikipedia/en/7/7f/WillyWonkaMoviePoster.jpg",
											"https://www.youtube.com/watch?v=GNarV_3P4oM",
											"Whimsical and imaginative. Roald Dahl not approved, though.")

star_wars = media.Movie("Star Wars", 
						"A boy kisses his sister then goes off to kill his dad with his gang of robots",
						"https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
						"https://www.youtube.com/watch?v=9gvqpFbRKtQ",
						"Episodes 4-6 are classics. Han shot first too.")

life_aquatic = media.Movie("The Life Aquatic with Steve Zissou", 
						   "Bill Murry hunts down a shark with his kind-of-son and a pretty cool pregnant lady. Pirates.",
						   "https://upload.wikimedia.org/wikipedia/en/7/7c/Lifeaquaticposter.jpg",
						   "https://www.youtube.com/watch?v=yh401Rmkq0o",
						   "Colorful, weird, and full of sweet headgear.")

crouching_tiger = media.Movie("Crouching Tiger, Hidden Dragon", 
							  "Flying ninjas fight over a sword.",
							  "https://upload.wikimedia.org/wikipedia/en/9/97/Crouching_tiger_hidden_dragon_poster.jpg",
							  "https://www.youtube.com/watch?v=oEaGsdiA0y0",
							  "Beautiful music, lush environments, fun action.")

walle = media.Movie("Wall-e", 
					"An iphone 10 cleans up Earth, redeems humanity.",
					"https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
					"https://www.youtube.com/watch?v=alIq_wG9FNk",
					"A feel good movie worth watching over and over. Weirdly works with Pink Floyd's Dark Side of the Moon too.")

nightmare_before_christmas = media.Movie("Nightmare Before Christmas", 
										 "Making Christmas, making Christmas. Just kidding, it's Halloween.",
										 "https://upload.wikimedia.org/wikipedia/en/9/9a/The_nightmare_before_christmas_poster.jpg",
										 "https://www.youtube.com/watch?v=8qrB9I3DM80",
										 "Tim Burton's best.")

movies = [labyrinth, dark_crystal, dredd, willy_wonka_chocolate_factory, star_wars, life_aquatic, crouching_tiger, walle, nightmare_before_christmas]
fresh_tomatoes.open_movies_page(movies)