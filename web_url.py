#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def extract_form_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        form_tag = soup.find('form', id='formulario')
        if form_tag:
            form_url = form_tag['action']
            parsed_url = urlparse(form_url)
            base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
            return base_url
        else:
            print("Form tag with ID 'formulario' not found.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error requesting URL: {e}")
        return None

#web_url = "https://www.chavazystem.tech/form.html"
#form_url = extract_form_url(web_url)

#if form_url:
#    print(f"{form_url}")
#else:
#    print("No FORM URL found.")
