#!/usr/bin/env python3

from database import execute_db_operation
from datetime import datetime


def detect_status_false():
	try:
		insert_query = 'SELECT * FROM url_status ORDER BY DATE DESC LIMIT 1;'
		connection, result = execute_db_operation(insert_query)
		return True, result
	except Exception as e:
		return False, None


if __name__ == "__main__":
	status, result = detect_status_false()
	(id_value, date_value, url_ngrok, url_web, url_match) = result[0]
	if not url_match:
		print(f'{status}\n{id_value}\n{date_value}\n{url_ngrok}\n{url_web}\n{url_match}')
	else:
		print(f'Nothing to do!')


#insert_query = 'SELECT * FROM url_status ORDER BY DATE DESC LIMIT 1;'
#connection, result = execute_db_operation(insert_query) #, insert_values)
#print(connection, result)
#[(48, datetime.datetime(2023, 8, 30, 17, 22, 3), 'https://40ed-69-157-250-11.ngrok-free.app', 'https://40ed-69-157-250-11.ngrok-free.app', 1)]
