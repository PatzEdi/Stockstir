# A file to test out Stockstir builds.
from stockstir import Stockstir
from urllib.request import Request, urlopen
from urllib.request import urlopen
import urllib
import requests

def get_source(url):
    req = Request(
        url=url,
        headers={'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0"}
    )
    return str(urlopen(req).read())

price = Stockstir().tools.get_single_price("TSLA")

print(price)