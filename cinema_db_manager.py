class CinemaDatabaseManager:

    GET_ALL_MOVIES_QUERY = """
        SELECT id, name, rating
        FROM Movies
        ORDER BY rating
    """

    GET_MOVIE_FROM_ID = """
        SELECT name
        FROM Movies
        WHERE id = ?
    """
    GET_ALL_MOVIE_PROJECTION_WITH_DATE = """
         SELECT date_p, time
         FROM Projections
         WHERE id = ? AND date_p = ?
    """
    GET_ALL_MOVIE_PROJECTION = """
         SELECT date_p, time
         FROM Projections
         WHERE id = ?
    """

    GET_ALL_RESERVATIONS = """

    """

    def __init__(self, conn):
        self.__conn = conn

    def get_all_movies(self):
        print("Current movies: ")
        cursor = self.__conn.cursor()
        result = cursor.execute(self.__class__.GET_ALL_MOVIES_QUERY)
        return result.fetchall()

    def get_all_movie_projections(self, movie_id, movie_date=None):
        cursor = self.__conn.cursor()
        result = cursor.execute(self.__class__.GET_MOVIE_FROM_ID, (movie_id,))
        movie = result.fetchone()
        print(movie['name'])


        if movie_date is not None:
            result = cursor.execute(self.__class__.GET_ALL_MOVIE_PROJECTION_WITH_DATE, (movie_id, movie_date))
        else:
            result = cursor.execute(self.__class__.GET_ALL_MOVIE_PROJECTION, (movie_id,))

        return result.fetchall()
