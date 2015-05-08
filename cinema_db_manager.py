class CinemaDatabaseManager:

    GET_ALL_MOVIES_QUERY = """
        SELECT id, name, rating
        FROM Movies
    """

    GET_ALL_RESERVATIONS = """

    """

    def __init__(self, conn):
        self.__conn = conn

    def get_all_movies(self):
        cursor = self.__conn.cursor()
        result = cursor.execute(self.__class__.GET_ALL_MOVIES_QUERY)
        return result.fetchall()
