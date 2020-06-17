from db_functions import create_connection, create_tables


def main():
    database = r"..\..\databases\warehouse.db"

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        state = create_tables(conn, '../../queries/warehouse/warehouse_create_tables.sql')
        if state:
            print('Table(s) (re)created')
    else:
        print("Error! Cannot create the database connection.")


if __name__ == '__main__':
    main()
