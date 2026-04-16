import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password= "Vishnusai@456",
        database="feedback_db"
    )