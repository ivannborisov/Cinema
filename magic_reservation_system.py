from cli import Cli
from cinema_db_manager import CinemaDatabaseManager
from settings import DB_NAME
import sqlite3


def main():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row

    cinema_db_manager = CinemaDatabaseManager(conn)
    client_interface = Cli(cinema_db_manager)

    client_interface.start()

if __name__ == "__main__":
    main()
