#!/usr/bin/env python3

import re
from urllib.parse import urlparse

def extract_form_url():
    try:
        with open('/home/pi/personal/cvjchavar.github.io/form.html', 'r') as html_file:
            content = html_file.read()
            match = re.search(r'<form id="formulario" action="([^"]+)"', content, re.DOTALL)
            if match:
                form_url = match.group(1)
                parsed_url = urlparse(form_url)
                base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
                return base_url
            else:
                print("FORM URL not found in form.html.")
                return None
    except FileNotFoundError:
        print("form.html not found.")
        return None

#form_url = extract_form_url()

#if form_url:
#    print(f"{form_url}")
#else:
#    print("No FORM URL found.")

