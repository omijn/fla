import strings
import requests
from bs4 import BeautifulSoup

def scrape(verb, tense):
	verb_url = strings.WIKI_FR_CJGTR + verb.lower()
	res = requests.get(verb_url)
	html_doc = res.text
	soup = BeautifulSoup(html_doc, 'html.parser')
