#!/usr/bin/env python3

import os
from ngrok_url import extract_ngrok_url
from web_url import extract_form_url
from database import execute_db_operation
from update_file import update_form_file
from update_git import update_github_repo
from datetime import datetime

FORM_STRING = '/cgi-bin/procesar_formulario.py'
REPO_PATH = '/home/pi/personal/cvjchavar.github.io'


def retrieve_url():
	web_url = "https://www.chavazystem.tech/form.html"
	form_url = extract_form_url(web_url)
	ngrok_url = extract_ngrok_url()
	if ngrok_url == form_url:
		return True, ngrok_url, form_url
	else:
		return False, ngrok_url, form_url


def update_db():
	try:
		status, ngrok_url, form_url = retrieve_url()
		insert_query = 'INSERT INTO url_status (date, url_ngrok, url_web, url_match ) VALUES (%s, %s, %s, %s);'
		insert_values = (datetime.now(), ngrok_url, form_url, status)
		connection, _ = execute_db_operation(insert_query, insert_values)
		return True
	except Exception as e:
		return False


def check_url_match():
	try:
		select_query = 'SELECT * FROM url_status ORDER BY DATE DESC LIMIT 1;'
		connection, result = execute_db_operation(select_query)
		return connection, result[0]
	except Exception as e:
		print(f'Error: {e}')
		return False, None

def update_file_url():
	connection, result = check_url_match()
	if connection:
		id_value = result[0]
		date_value = result[1]
		url_ngrok = result[2]
		url_web = result[3]
		url_match = result[4]
		if not url_match:
			update_form_file(url_ngrok + FORM_STRING)
			return True, url_ngrok
		else:
			return False, None


if __name__ == "__main__":
	result = update_db()
	print(f'[+] {datetime.now()} - DB Updated:   {result}') if result else print(f'[-] {datetime.now()} - DB Updated: {result}')
	update_result, url_ngrok =update_file_url()
	print(f'[+] {datetime.now()} - File Updated: {update_result}') if result else print(f'[-] {datetime.now()} - File Updated: {update_result}')
	if not update_result:
		print(f'[+] {datetime.now()} - Not need to update git.')
	else:
		update_repo = update_github_repo(repo_path=REPO_PATH, commit_message=f'form.html updated with url: {url_ngrok} - [Automated process]')
		if update_repo:
			print(f'[+] {datetime.now()} - Git Updated:  {update_result}')
		else:
			print(f'[-] {datetime.now()} - Git Updated:  {update_result}')
