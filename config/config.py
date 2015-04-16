import os
import json


project = {
    'title': 'Dimitrios Kanellopoulos',
    'domain': 'dimitrioskanellopoulos.com',
    'meta': {
        'description': 'My personal website',
        'keywords': 'Dimitrios Kanellopoulos, Dimitrios, Kanellopoulos',
        'author': 'Dimitrios Kanellopoulos',
        'og': {
            'title': 'Dimitrios Kanellopoulos',
            'description': 'My personal website',
            'type': 'website',
            'url': 'http://dimitrioskanellopoulos.com',
            'image': 'https://www.gravatar.com/avatar/50eda10b9e16333f9e9cd3b8f1e0918a?s=500&d=identicon&r=PG'
        },
    },
    'google_analytics': 'UA-61188889-1'
}


config = {
    'project': project,
}


def is_dev_server():
    return os.environ['SERVER_SOFTWARE'].startswith('Dev')


def get_api_keys():
    file_handler = os.path.join(os.path.dirname(__file__), 'api_keys_dev.json') \
        if is_dev_server() \
        else os.path.join('.', 'api_keys.json')
    try:
        with open(file_handler) as json_file:
            return json.load(json_file)
    except Exception as e:
        return False
