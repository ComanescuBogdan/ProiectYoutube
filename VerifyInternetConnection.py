#librarie pentru a face request sa vedem conexiunea la internet
import requests
import time


def conexiune():
    try:
        requests.get('https://google.com/')
        return True
    except:
        return False

