class Movie():

    def __init__(self, db_man):
        self.__db_man = db_man

    def showmovies(self):
        movies = self.__db_man.get_all_movies()
        for mov in movies:
            print(mov['name'])

    def showmovieprojections(self, id, date=None):
        self.__db_man.get_all_movie_projections(id, date)
