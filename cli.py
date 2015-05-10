from movie import Movie
from reservation import Reservation


class Cli:

    def __init__(self, db_manager):

        self.__movie = Movie(db_manager)
        self.__reservation = Reservation(db_manager, self.__movie)

        self.commands = {
            "show_movies": self.__movie.showmovies,
            "show_movie_projections": self.__movie.showmovieprojections,
            "make_reservation": self.__reservation.make_reservation
        }

    def run_command(self, command):
        command = command.split(' ')
        class_com = self.commands[command[0]]
        if command[0] == "show_movie_projections":
            try:
                class_com(command[1], command[2])
                # print(command[1] + " " + command[2])
            except:
                class_com(command[1])
        else:
            class_com()

    def start(self):
        while True:
            print("\nCommands: show_movies, show_movie_projections id|date , make_reservation")
            command = input("Enter command: ")
            self.run_command(command)


#    def start(self):
#        while True:
#            command = 