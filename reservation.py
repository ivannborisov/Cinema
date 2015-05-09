class Reservation:

    def __init__(self, db_man, movies):
        self.__db_man = db_man
        self.__movies = movies

    def make_reservation(self):
        name = input("Step 1 (User): Choose name ")
        num_of_tickets = input("Choose number of tickets ")
        print(name + " " + str(num_of_tickets))
        self.__movies.showmovies()
