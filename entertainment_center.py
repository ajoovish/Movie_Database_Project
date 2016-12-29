import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","A Story of a boy and his toy that come to life","https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("avatar", "A movie based on a utopia", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print (avatar.storyline)
#avatar.show_trailer()

dk = media.Movie("The Dark Knight","Sequel to the Batman Begins", "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", "https://www.youtube.com/watch?v=kmJLuwP3MbY")

#dk.show_trailer()

movies = [toy_story, avatar, dk]
fresh_tomatoes.open_movies_page(movies)
