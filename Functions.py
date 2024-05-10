import sqlite3
import string
import secrets
import time


# Creating strong password
def create_password(password_lenght):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(password_lenght))
        if ((any(ch.islower() for ch in password)) and (any(ch.isupper() for ch in password)) and
                (any(ch.isdigit for ch in password)) and (any(ch in string.punctuation for ch in password))):
            break
    return password


# Inserting into database.
def add_to_database(website, password, iv):
    conn = sqlite3.connect("login_info.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Website FROM Login_info WHERE Website = :value", {'value': website})
    if len(cursor.fetchall()) == 0:
        cursor.execute("INSERT INTO Login_info (Website, Password, iv) VALUES (?, ?, ?)", (website, password, iv))
    conn.commit()


