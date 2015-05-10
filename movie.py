class Movie():

    def __init__(self, db_man):
        self.__db_man = db_man

    def showmovies(self):
        print("Current movies: ")
        movies = self.__db_man.get_all_movies()
        for mov in movies:
            print(str(mov['id']) + " " + mov['name'] + ' ' + '(' + str(mov['rating'])+ ')')

    def showmovieprojections(self, mov_id, date=None):
        projections = self.__db_man.get_all_movie_projections(mov_id, date)
        for proj in projections:
            print_str = "[{}] - {} - {} ({})".format(str(proj['id']), proj['date_p'], proj['time'], proj['type'])
            print(print_str)
