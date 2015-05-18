import os
import json

from lib.apis import google_plus_api


def is_dev_server():
    return os.environ['SERVER_SOFTWARE'].startswith('Dev')


def get_api_keys():
    file_handler = os.path.join(os.path.dirname(__file__), 'api_keys_dev.json') \
        if is_dev_server() \
        else os.path.join(os.path.dirname(__file__), 'api_keys.json')
    try:
        with open(file_handler) as json_file:
            return json.load(json_file)
    except Exception as e:
        return False


def get_client_secrets_filename():
    return os.path.join(os.path.dirname(__file__), 'client_secrets_dev.json') \
        if is_dev_server() \
        else os.path.join(os.path.dirname(__file__), 'client_secrets.json')


def get_meta_og_image():
    # returns the background in 500w
    pass


project = {
    'title': 'Dimitrios Kanellopoulos',
    'domain': 'dimitrioskanellopoulos.com',
    'meta': {
        'description': 'Personal website of Dimitrios Kanellopoulos',
        'keywords': 'Dimitrios Kanellopoulos, Dimitrios, Kanellopoulos, dimitrios, kanellopoulos, dimitrioskanellopoulos.com',
        'author': 'Dimitrios Kanellopoulos',
        'theme_color': '#3FC3FF',
        'og': {
            'title': 'Personal website of Dimitrios Kanellopoulos',
            'description': 'Personal website of Dimitrios Kanellopoulos',
            'type': 'website',
            'url': 'http://dimitrioskanellopoulos.com',
            'image': get_meta_og_image()
        },
    },
    'google_analytics': 'UA-61188889-1'
}

config = {
    'project': project,
    # Hardcode some id's
    'google_plus_api_user_id': '102445631084043565507',
    'runkeeper_user_id': '29509824'
}