#librarie pentru a face request sa vedem conexiunea la internet
import requests


def conexiune():
    try:
        requests.get('https://google.com/')
        return True
    except:
        return False




