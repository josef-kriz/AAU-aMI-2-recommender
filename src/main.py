import csv as csv
import networkx as net
import matplotlib.pyplot as plt

file = open('data/ratings.csv', 'r')
movieReader = csv.reader(file, delimiter=',')

G = net.Graph()

for row in movieReader:
    # print(', '.join(row))
    # according to readme the format of the row is userID, movieID, rating, timestamp
    # creating graph with nodes for each item, edges between user and item are through rating (substituting play from
    # the paper) and timestamp is connected to play
    # userID
    G.add_node(row[0], type='user')
    # itemID
    G.add_node(row[1], type='item')
    # rating/playing
    G.add_node(row[2], type='activity')
    # timestamp
    G.add_node(row[3], type='time')
    # user - rating
    G.add_edge(row[0], row[2])
    # item - rating
    G.add_edge(row[1], row[2])
    # rating - time
    G.add_edge(row[3], row[2])

# print(G.nodes)

# net.draw(G, pos=net.spring_layout(G))
# plt.show()
