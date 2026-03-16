import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="admin",
        password="1234",
        database="women_safety"
    )
