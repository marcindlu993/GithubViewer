import urllib
import json


def set_format(fmt=None):
    if fmt is None:
        return '%d-%m-%Y'
    else:
        return fmt


def find_git_user(name):
    request_query = "https://api.github.com/users/" + name
    response = urllib.urlopen(request_query)
    data = json.dumps(json.loads(response.read().decode("utf-8")))
    return data