#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv('/home/pi/personal/automated_web/.db')

host = os.environ.get('host')
user = os.environ.get('user')
password = os.environ.get('password')
database = os.environ.get('database')


def execute_db_operation(query, values=None):
    try:
        db_connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = db_connection.cursor()

        if values is None:
            cursor.execute(query)
        else:
            cursor.execute(query, values)

        if query.lower().startswith("select"):
            result = cursor.fetchall()
            cursor.close()
            db_connection.close()
            return True, result
        else:
            db_connection.commit()
            cursor.close()
            db_connection.close()
            return True, None

    except Exception as e:
        return False, str(e)



# Ejemplo de uso para INSERT
#insert_query = 'INSERT INTO url_status (date, url_ngrok, url_web, url_match ) VALUES (%s, %s, %s, %s);'
#insert_values = ("2023-08-30 10:00:00", "https://07ae-69-157-250-11.ngrok-free.app", "https://07ae-69-157-250-11.ngrok-free.app", True)
#connection, _ = execute_db_operation(insert_query, insert_values)
#if connection:
#    print("Insert exitoso.")
#else:
#    print("Error en el insert.")



# Ejemplo de uso para SELECT
#select_query = 'SELECT * FROM url_status;'
#connection, result = execute_db_operation(select_query)
#if connection:
#    for data in result:
#        print(data)
#else:
#    print("Error:", result)

