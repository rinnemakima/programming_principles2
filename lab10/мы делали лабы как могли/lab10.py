import psycopg2
import csv

conn = psycopg2.connect(
    database = "postgres",
    user = "postgres",
    host = 'localhost',
    password = "L@remIpsum228",
    port = 5432
)

def create_table():
    command = """CREATE TABLE PhoneBook(
                id SERIAL PRIMARY KEY,
                user_name VARCHAR(255),
                phone_number INTEGER
            )"""
    with conn.cursor() as cur:
        cur.execute(command)
        conn.commit()

def insert_student(user_name, phone_number):

    command = """INSERT INTO PhoneBook(user_name, phone_number) VALUES(%s, %s)"""

    with conn.cursor() as cur:
        cur.execute(command, (user_name, phone_number))
        conn.commit()
    
IMYA = str(input())
TELEPHONE = int(input())

def insert_student_from_csv(csv_file_name):

    command = """INSERT INTO PhoneBook(user_name, phone_number) VALUES(%s, %s)"""

    with conn.cursor() as cur:
        # execute the command
        with open(csv_file_name, "r") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            _ = next(csvreader) # getting rid of the headers
            for row in csvreader:
                # print(row)
                user_name, phone_number = row
                # print(name, major, gpa, year)
                cur.execute(command, (user_name, phone_number))
        conn.commit()

insert_student(IMYA, TELEPHONE)