# We use the psycopg2 library to help us connec to the Postgres SQL database
# This library is already installed on stearns.mathcs.carleton.edu
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="parkern2",
        user="parkern2",
        password="python336spam")


def create_tables():
    cur = conn.cursor()
    commands = (
        """
        CREATE TABLE States (
            code text,
            state text,
            pop real
        );
        """,
        """
        CREATE TABLE Cities (
            city text,
            state text,
            pop real,
            lat real,
            lon real
        );
        """
        )
    cur.execute(commands[0])
    cur.execute(commands[1])
    conn.commit()
       

if __name__ == '__main__':
    create_tables()