class Movie:
    def __init__(self, id, name, genres):
        self.id = id
        self.name = name
        self.genres = genres
        self.label = 'Movie - #' + str(self.id) + ' ' + self.name
