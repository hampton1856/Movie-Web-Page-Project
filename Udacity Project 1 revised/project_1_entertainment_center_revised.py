import fresh_tomatoes  # imports fresh_tomatoes file from folder
import project_1_media   # imports project_1_media file from folder

'''Below you can see all of the different instances of the
class Movie located in project_1_media file'''
iron_man = project_1_media.Movie(
    "Iron Man",
    "Tony Stark billionare playboy builds a super suit to fight crime",
    "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
    "https://www.youtube.com/watch?v=8hYlB38asDY")

incredible_hulk = project_1_media.Movie(
    "The Incredible Hulk",
    "Bruce Banner transforms into the big green monster",
    "https://goo.gl/1nR6cg", "https://www.youtube.com/watch?v=xbqNb2PFKKA")

iron_man_two = project_1_media.Movie(
    "Iron Man II",
    "Iron Man must protect the world once more",
    "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
    "https://www.youtube.com/watch?v=BoohRoVA9WQ")

thor = project_1_media.Movie(
    "Thor",
    "An ancient god is brought to earth to find himself",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
    "https://www.youtube.com/watch?v=JOddp-nlNvQ")

captain_america = project_1_media.Movie(
    "Captain America: The First Avenger",
    "A small soldier is trasnformed into Captain America by science",
    "https://goo.gl/BdbNlM",
    "https://www.youtube.com/watch?v=JerVrbLldXw")

avengers = project_1_media.Movie(
    "Marvel's The Avengers",
    "A team of super heros join forces to save earth",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
    "https://www.youtube.com/watch?v=eOrNdBpGMv8")


movies = (
    [iron_man, incredible_hulk, iron_man_two, thor, captain_america, avengers])
# above is an array of all the instances that belong to the class Movie
fresh_tomatoes.open_movies_page(movies)
"""above python is utilizing the imported fresh_tomatoes file
and calling the function .open_movies_page
located with in it. The array movies is being fed into the function
to create the webpage via the files HTML and CSS"""
