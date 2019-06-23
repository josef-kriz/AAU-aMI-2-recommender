import csv as csv
import networkx as net
import matplotlib.pyplot as plt
from src.aggregate import aggregate
from src.parser import read_movies, create_graph

# NOTES:
# - recommendation is between information retrieval and information retrieval
# - both content and queries do vary but quite slowly
# - recommender system helps to match users with items (books, movies, products, ...)
# - given the profile of a user and list of items (with description) compute ranking score for each item
# - content based system, collaborative systems, hybrid systems
# - represent products and users as nodes in graph
# - add edges if user rates/buys a product
# - add edges between similar products
# - construct adjacency matrix -> transition probability matrix
# - employ personalized page rank, personalization vector

# LIMITATIONS:
# - scalability - usually huge graphs
# - we did not implement aggregation technique in general, instead we have hardcoded aggregation of user and day part
# - we did not implement aggregation techniques, instead we did the aggregation while creating graph
# - we add edge from event to genre to increase genre importance, other way would be adding weights to different factors

# AGGREGATION:
# - makes graph smaller, may also improve results if subgraph fits the user needs
# - two operations - node-edge aggregate and graphs merge

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
    movies[1].label: 1,
    movies[2].label: 1
}

# run page rank
# damping factor is the default: 0.85
recommendations = net.pagerank(graph, personalization=preferences)
# sort nodes according to page rank
recommendations = sorted(recommendations.items(), key=lambda p: p[1], reverse=True)

get_top_k_movies(30, recommendations)