import sqlite3
import pandas as pd

from config import DB_NAME


def write_to_db():
    conn = get_connection(DB_NAME)
    cursor = get_cursor(conn)
    cursor.executemany()
    conn.commit()
    conn.close()


def get_connection(db_name):
    return sqlite3.connect(db_name)


def get_cursor(connection):
    return connection.cursor()


def is_table_exist(name):
    conn = get_connection(DB_NAME)
    c = get_cursor(conn)
    c.execute(f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{name}'")
    if c.fetchone()[0] == 1:
        state = True
    else:
        state = False
    conn.commit()
    conn.close()
    return state


def create_table(name):
    conn = get_connection(DB_NAME)
    c = get_cursor(conn)
    c.execute(f"CREATE TABLE {name} (timestamp date, height int, txhash text, object_from text, object_to text, subject text, karma int)")
    conn.commit()
    conn.close()


def insert_to_db(links, table):
    conn = get_connection(DB_NAME)
    c = get_cursor(conn)
    c.executemany(f"INSERT INTO {table} VALUES (?, ?, ?, ?, ?, ?, ?)", links)
    conn.commit()
    conn.close()


def fix_karma(table):
    conn = get_connection(DB_NAME)
    c = get_cursor(conn)
    c.execute(f'UPDATE {table} SET karma = 1 where karma = 0')
    conn.commit()
    conn.close()


def karma_grouped_to_df(table):
    conn = get_connection(DB_NAME)
    c = get_cursor(conn)
    df = pd.read_sql_query(f"SELECT subject, sum(karma) as karma FROM {table} GROUP BY subject ORDER by karma DESC", conn)
    return df
