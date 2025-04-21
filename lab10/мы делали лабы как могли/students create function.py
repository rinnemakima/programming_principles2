import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="L@remIpsum228"
)

def create_table():
    command = """CREATE TABLE students(
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                major VARCHAR(10),
                gpa NUMERIC,
                year INTEGER
            )"""
    with conn.cursor() as cur:
        cur.execute(command)
        conn.commit()

conn.close()