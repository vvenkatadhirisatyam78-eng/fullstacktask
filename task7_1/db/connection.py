import mysql.connector


def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vishnusai@456",   
        database="university_db"
    )

    return conn