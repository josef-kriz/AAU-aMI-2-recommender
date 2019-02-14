import csv as csv
import networkx as net
import matplotlib.pyplot as plt

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
graph = create_graph(movies, 'data/ratings.csv', 1000000000)

# net.draw(graph, pos=net.spring_layout(graph), with_labels=True)
# plt.show()

preferences = {
    movies[1].label: 1,
    movies[2].label: 1
}

recommendations = net.pagerank(graph, personalization=preferences)
recommendations = sorted(recommendations.items(), key=lambda p: p[1], reverse=True)

# print(recommendations[0])
# print(recommendations[1])
# print(recommendations[2])
# print(recommendations[3])

get_top_k_movies(30, recommendations)