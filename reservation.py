class Reservation:

    def __init__(self, db_man, movies):
        self.__db_man = db_man
        self.__movies = movies

    def get_projection_seats(self, res):
        reservations = res
        seats = []
        for i in range(0, 11):
            # pr_str = str(i)
            curr_row = []
            for j in range(0, 11):
                if i == 0:
                    if j == 0:
                        curr_row.append(' ')
                    else:
                        curr_row.append(str(j))
                elif i != 0 and j == 0:
                    curr_row.append(str(i))
                else:
                    curr_row.append('.')
                # pr_str += " " + str(j) + " "
            seats.append(curr_row)

        for res in reservations:
            seats[res['row']][res['col']] = 'X'

        return seats

    def make_tuple_from_str(self, tuple_str):

        strip_tuple = tuple_str.strip('(')
        strip_tuple = strip_tuple.strip(')')

        seat_list = strip_tuple.split(',')
        return seat_list

    def is_seat_free(self, seat_tup, seats):
        # wanted_seat = seats[seat_tup[0]][seat_tup[1]]
        if seats[int(seat_tup[0])][int(seat_tup[1])] == 'X':
            return False
        else:
            return True

    def print_seats(self, seats):
        for i in range(0, 11):
            print_str = ""
            for j in range(0, 11):
                print_str += str(seats[i][j]) + ' '
            print(print_str)

    def reserve_seat(self, seat, name, proj_id):
        self.__db_man.insert_reservation(name, proj_id, seat[0], seat[1])
        # print("You get it")
        # print (seat)

    def make_reservation(self):
        name = input("Step 1 (User): Choose name ")
        num_of_tickets = input("Choose number of tickets ")
        print(name + " " + str(num_of_tickets))
        self.__movies.showmovies()

        mov_id = input("Step 2 (Movie): Choose a movie ")
        movie = self.__db_man.get_movie_by_id(mov_id)
        print(movie['name'])
        self.__movies.showmovieprojections(mov_id)

        proj_id = input("Step 3 (Projections):Choose a projection ")
        res = self.__db_man.get_proj_reservations(proj_id)
        seats = self.get_projection_seats(res)
        self.print_seats(seats)

        reserved_seats = []
        for i in range(0, int(num_of_tickets)):
            while True:
                seat = input("Choose seat {}> ".format(str(i+1)))
                seat = self.make_tuple_from_str(seat)

                if int(seat[0]) <1 or int(seat[0])>10 or int(seat[1])<1 or int(seat[1])>10:
                    print("Lol...NO!")
                elif self.is_seat_free(seat, seats) and seat not in reserved_seats:
                    reserved_seats.append(seat)
                    break
                else:
                    print('This seat is already taken!')

        print("This is your reservation:")
        print("Movie: {} ({})".format(movie['name'], movie['rating']))
        proj = self.__db_man.get_proj_by_id(proj_id)

        print("Date and Time: {} {} ({})".format(proj['date_p'], proj['time'], proj['type']))

        seats_str = "Seats: "
        for r_seat in reserved_seats:
            seats_str += "({},{}) ".format(r_seat[0], r_seat[1])
        print(seats_str)

        confirm = input("Step 5 (Confirm - type 'finalize') ")
        if confirm == 'finalize':
            for res_seat in reserved_seats:
                self.reserve_seat(res_seat, name, proj_id)
            print('Thanks!')
        else:
            print('Your reservation was cancelled!')
