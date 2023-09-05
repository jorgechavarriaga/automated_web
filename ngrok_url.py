#!/usr/bin/env python3

import json
import requests


def extract_ngrok_url():
        response = requests.get("http://127.0.0.1:4040/api/tunnels")
        data = response.json()
        if "tunnels" in data:
                tunnels = data["tunnels"]
                for tunnel in tunnels:
                        if "public_url" in tunnel:
                                public_url = tunnel["public_url"]
                                return public_url
        else:
                print("No tunnels found in the response.")
                return None

#url = extract_ngrok_url()
#if url:
#	print(url)
#else:
#	print("No Url")

