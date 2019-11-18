import requests
import urllib.request
import time
from bs4 import BeautifulSoup
url = 'http://vicebienestar.univalle.edu.co/restaurante-universitario'
request= requests.get(url)
