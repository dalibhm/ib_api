import requests


def get_url_content(url):
    response = requests.get(url)
    if response:
        return response.text








