import csv as csv
import networkx as net
from .movie import Movie
from datetime import datetime


def create_graph(movie_dict, ratings_path, n):
    file = open(ratings_path, 'r')
    ratings_reader = csv.reader(file, delimiter=',')

    # skip the header of the csv file
    next(ratings_reader)

    G = net.Graph()

    i = 0
    for row in ratings_reader:
        if i == n + 1:
            break
        i = i + 1
        user = 'User - ' + row[0]
        movie = movie_dict[int(row[1])]
        movie_label = 'Movie - #' + str(movie.id) + ' ' + movie.name
        rating = 'Rating - ' + row[2]
        day_phase = 'Day phase - ' + get_day_phase(int(row[3]))

        G.add_node(user, type='user')
        G.add_node(movie_label, type='item')
        for genre in movie_dict[int(row[1])].genres:
            G.add_node('Genre - ' + genre, type='genre')
            G.add_edge(movie_label, genre)
        G.add_node(rating, type='rating')
        G.add_node(day_phase, type='time')

        G.add_edge(user, rating)
        G.add_edge(movie_label, rating)
        G.add_edge(rating, day_phase)

    return G


def read_movies(movies_path):
    file = open(movies_path, 'r')
    movie_reader = csv.reader(file, delimiter=',')

    next(movie_reader)

    movies = dict()
    for row in movie_reader:
        genres = row[2].split("|")
        movies[int(row[0])] = Movie(int(row[0]), row[1], genres)

    return movies

def get_day_phase(timestamp):
    dt = datetime.utcfromtimestamp(timestamp)
    if dt.hour <= 4:
        return "night"
    if dt.hour <= 9:
        return "morning"
    if dt.hour <= 12:
        return "before_noon"
    if dt.hour <= 17:
        return "afternoon"
    if dt.hour <= 23:
        return "evening"
    return "night"
