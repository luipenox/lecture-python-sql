import sqlite3
from sqlite3 import Error

import sys


def create_connection(db_file):
    """
    create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e, file=sys.stderr)

    return connection


def create_tables(conn, query_file, encoding='utf-8'):
    """
    create a table(s) from the sql statement
    :param conn: Connection object
    :param query_file: a file with sql code
    :param encoding: file encoding (default utf-8)
    :return: True if executed was correct else False
    """

    with open(query_file, mode='r', encoding=encoding) as f:
        statements = f.read()

    for code in statements.split(';'):
        try:
            c = conn.cursor()
            c.execute(code)
        except Error as e:
            print(e, file=sys.stderr)
            return False

    return True


def insert_data(conn, query_file, encoding='utf-8'):
    """
    execute an insert query - data are in SQL for now
    :param conn: Connection object
    :param query_file: a file with sql code
    :param encoding: file encoding (default utf-8)
    :return: True if executed was correct else False
    """

    with open(query_file, mode='r', encoding=encoding) as f:
        code = f.read()

    try:
        c = conn.cursor()
        c.execute(code)
        conn.commit()
        return True
    except Error as e:
        print(e, file=sys.stderr)

    return False


def select_data(conn, query_file, encoding='utf-8'):
    """
    select from the table
    :param conn: Connection object
    :param query_file: a file with sql code
    :param encoding: file encoding (default utf-8)
    :return: True if executed was correct else False
    """

    with open(query_file, mode='r', encoding=encoding) as f:
        code = f.read()

    try:
        c = conn.cursor()
        c.execute(code)
        if c:
            return c.fetchall()
        else:
            return None
    except Error as e:
        print(e, file=sys.stderr)

    return False


if __name__ == '__main__':
    pass
