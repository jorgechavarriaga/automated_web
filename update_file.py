#!/usr/bin/env python3

import re
from urllib.parse import urlparse
from form_url import extract_form_url


def replace_form_url(html_content, new_url):
    match = re.search(r'<form id="formulario" action="([^"]+)"', html_content, re.DOTALL)
    if match:
        old_url = match.group(1)
        updated_html_content = html_content.replace(old_url, new_url)
        return updated_html_content
    else:
        return None


def update_form_file(new_url):
    try:
        with open('/home/pi/personal/cvjchavar.github.io/form.html', 'r') as html_file:
            content = html_file.read()
            form_url = extract_form_url()
            if form_url:
                updated_content = replace_form_url(content, new_url)
                if updated_content:
                    with open('/home/pi/personal/cvjchavar.github.io/form.html', 'w') as updated_html_file:
                        updated_html_file.write(updated_content)
                    return True
                else:
                    return False
            else:
                return False
    except FileNotFoundError:
        return False

