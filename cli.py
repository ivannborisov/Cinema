from movie import Movie
from reservation import Reservation


class Cli:

    def __init__(self, db_manager):

        self.__movie = Movie(db_manager)
        self.__reservation = Reservation()

        self.commands = {
            "showmovies": self.__movie.showmovies,
            "showmovieprojections": self.__movie.showmovieprojections,
            "make_reservation": self.__reservation
        }

    def run_command(self, command):
        class_com = self.commands[command]
        class_com(1)


#    def start(self):
#        while True:
#            command = 