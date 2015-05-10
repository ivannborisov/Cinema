class CinemaDatabaseManager:

    GET_ALL_MOVIES_QUERY = """
        SELECT id, name, rating
        FROM Movies
        ORDER BY rating DESC
    """

    GET_MOVIE_FROM_ID = """
        SELECT name, rating
        FROM Movies
        WHERE id = ?
    """
    GET_ALL_MOVIE_PROJECTION_WITH_DATE = """
         SELECT id,type,date_p, time
         FROM Projections
         WHERE movie_id = ? AND date_p = ?
    """
    GET_ALL_MOVIE_PROJECTION = """
         SELECT id,type,date_p, time
         FROM Projections
         WHERE movie_id = ?
    """

    GET_ALL_PROJ_RESERVATIONS = """
        SELECT row, col
        FROM Reservations
        WHERE projection_id = ?
    """

    GET_PROJECTION_FROM_ID = """
        SELECT type, date_p, time
        FROM Projections
        WHERE id = ?
    """

    INSERT_RESERVATION_QUERY = """
        INSERT INTO Reservations(username,projection_id,row,col)
        VALUES (?,?,?,?)
    """

    def __init__(self, conn):
        self.__conn = conn

    def get_all_movies(self):
        cursor = self.__conn.cursor()
        result = cursor.execute(self.__class__.GET_ALL_MOVIES_QUERY)
        return result.fetchall()

    def get_movie_by_id(self, movie_id):
        cursor = self.__conn.cursor()
        result = cursor.execute(self.__class__.GET_MOVIE_FROM_ID, (movie_id,))
        return result.fetchone()

    def get_all_movie_projections(self, movie_id, movie_date=None):
        cursor = self.__conn.cursor()

        if movie_date is not None:
            result = cursor.execute(self.__class__.GET_ALL_MOVIE_PROJECTION_WITH_DATE, (movie_id, movie_date))
        else:
            result = cursor.execute(self.__class__.GET_ALL_MOVIE_PROJECTION, (movie_id,))

        return result.fetchall()

    def get_proj_by_id(self, proj_id):
        cursor = self.__conn.cursor()
        result = cursor.execute(self.__class__.GET_PROJECTION_FROM_ID, (proj_id,))
        return result.fetchone()

    def get_proj_reservations(self, proj_id):
        cursor = self.__conn.cursor()
        result = cursor.execute(self.__class__.GET_ALL_PROJ_RESERVATIONS, (proj_id,))
        return result.fetchall()

    def insert_reservation(self, name, proj_id, row, col):
        cursor = self.__conn.cursor()
        query = self.__class__.INSERT_RESERVATION_QUERY
        cursor.execute(query, (name, proj_id, row, col))
        self.__conn.commit()
