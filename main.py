import requests

def gethtml(url):
        print((requests.get(url).content))
