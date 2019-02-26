import csv as csv
import networkx as net
import matplotlib.pyplot as plt

from src.aggregate import aggregate
from src.parser import read_movies, create_graph

def get_top_k_movies(k, recommendations):
    cnt = 0
    for node in recommendations:
        if cnt == k:
            return
        if 'Movie' in node[0]:
            print(node)
            cnt = cnt + 1

movies = read_movies('data/movies.csv')
graph = create_graph(movies, 'data/ratings.csv', 10000000000)

graph = aggregate(graph)

# net.draw(graph, pos=net.spring_layout(graph), with_labels=True)
# plt.show()
preferences = {
    'Movie - #2 Jumanji (1995) Genre - Adventure': 1,
    'Movie - #2 Jumanji (1995) Genre - Children': 1,
    'Movie - #2 Jumanji (1995) Genre - Fantasy': 1,
    'Movie - #1 Toy Story (1995) Genre - Adventure': 1,
    'Movie - #1 Toy Story (1995) Genre - Children': 1,
    'Movie - #1 Toy Story (1995) Genre - Fantasy': 1,
    'Movie - #1 Toy Story (1995) Genre - Comedy': 1,
    'Movie - #1 Toy Story (1995) Genre - Animation': 1,
}
    # movies[1].label: 1,
    # movies[2].label: 1

recommendations = net.pagerank(graph, personalization=preferences, alpha=0.6)
recommendations = sorted(recommendations.items(), key=lambda p: p[1], reverse=True)

get_top_k_movies(80, recommendations)