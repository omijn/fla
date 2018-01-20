import strings
import requests
from conjugator import tenses
from bs4 import BeautifulSoup

"""
EXPLANATION OF TABLE OFFSET:
the table element on the html page corresponds to the 1st tense (tense code 0)

tense 0 - table 5
tense 1 - table 6
...
tense 15 - table 20
"""
TABLE_OFFSET = 5

def scrape(verb, tense_code):

	verb_url = strings.WIKI_FR_CJGTR + verb.lower()
	
	res = requests.get(verb_url)
	if res.status_code == 404:
		return strings.VERB_NOT_FOUND

	html_doc = res.text
	soup = BeautifulSoup(html_doc, 'html.parser')	

	scraped_conjugation = ""

	# find the right table on the page, and loop through all the rows after the 0th row
	for tr in soup.select("table:nth-of-type(" + str(int(TABLE_OFFSET) + int(tense_code)) + ")")[0].find_all('tr')[1:]:
		subject = tr.td.string
		verb = tr.td.next_sibling.next_sibling.string
		scraped_conjugation += "{} {}\n".format(subject, verb)

	return scraped_conjugation