import networkx as net


def aggregate(graph):
    G = net.Graph()

    atts = net.get_node_attributes(graph, 'type')

    for node, type in atts.items():
        if type == 'rating':
            G.add_node(node, type='rating')
        if type != 'genre':
            continue
        genre = node
        genre_movies = graph[genre]
        for movie in genre_movies.keys():
            if graph.nodes[movie]['type'] == 'item':
                G.add_node(movie + ' ' + genre, type='movie-genre')

    for event, event_type in atts.items():
        if event_type != 'event':
            continue
        G.add_node(event, type='event')
        event_neighbors = graph[event]
        user = None
        time = None
        genres = []
        movie = None
        for node in event_neighbors.keys():
            type = graph.nodes[node]['type']
            if type == 'user':
                user = node
            if type == 'time':
                time = node
            if type == 'item':
                movie = node
            if type == 'genre':
                genres.append(node)
            if type == 'rating':
                G.add_edge(event, node)
        for genre in genres:
            G.add_edge(event, movie + ' ' + genre)
        user_time = user + ' ' + time
        G.add_node(user_time, type='user-time')
        G.add_edge(event, user_time)

    return G
