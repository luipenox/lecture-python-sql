import sqlite3
from sqlite3 import Error

import sys


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e, file=sys.stderr)

    return connection


def execute_query(conn, query):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param query: a CREATE TABLE statement
    :return: True if executed was correct else False
    """
    try:
        c = conn.cursor()
        c.execute(query)
        return True
    except Error as e:
        print(e, file=sys.stderr)

    return False


if __name__ == '__main__':
    pass
