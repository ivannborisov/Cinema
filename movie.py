class Movie():

    def __init__(self, db_man):
        self.__db_man = db_man

    def showmovies(self, id=None):

        if id is None:
            movies = self.__db_man.get_all_movies()
            for mov in movies:
                print(mov['name'])
        else:
            print("Movies id")
