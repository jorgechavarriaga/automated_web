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
#        print("FORM URL not found in HTML content.")
        return None


def update_form_file(new_url):
    try:
        with open('/home/pi/personal/cvjchavar.github.io/form.html', 'r') as html_file:
            content = html_file.read()
            form_url = extract_form_url()
            if form_url:
                updated_content = replace_form_url(content, new_url)
                if updated_content:
                    with open('/home/pi/personal/cvjchavar.github.io/form_test.html', 'w') as updated_html_file:
                        updated_html_file.write(updated_content)
#                    print(f"URL updated successfully to: {new_url}")
                    return True
                else:
#                    print("URL replacement failed.")
                    return False
            else:
#                print("No FORM URL found.")
                return False
    except FileNotFoundError:
#        print("form.html not found.")
        return False


#if __name__ == "__main__":
#	new_url = 'https://www.chavazystem.tech'+'/cgi-bin/procesar_formulario.py'
#	status =update_form_file(new_url)
#	print(status)
