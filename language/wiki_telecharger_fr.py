# coding=utf-8
import strings
import requests
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

# def scrape_by_code(verb, tense_code):

# 	verb_url = strings.WIKI_FR_CJGTR + verb.lower()
	
# 	res = requests.get(verb_url)
# 	if res.status_code == 404:
# 		return strings.VERB_NOT_FOUND

# 	html_doc = res.text
# 	soup = BeautifulSoup(html_doc, 'html.parser')	

# 	scraped_conjugation = u""

# 	# find the right table on the page, and loop through all the rows after the 0th row
# 	for tr in soup.select("table:nth-of-type(" + str(int(TABLE_OFFSET) + int(tense_code)) + ")")[0].find_all('tr')[1:]:
# 		if tense_code == 17 or tense_code == 18:
# 			subject = u""
# 		else:
# 			subject = tr.td.get_text().replace(u'\xa0', u' ')
# 		verb = tr.td.next_sibling.next_sibling.get_text()
# 		scraped_conjugation += u"{}{}\n".format(subject, verb)

# 	return scraped_conjugation

def scrape(verb, mode, section_code, code):
	verb_url = strings.WIKI_FR_CJGTR + verb.lower()
	
	res = requests.get(verb_url)
	if res.status_code == 404:
		return strings.VERB_NOT_FOUND

	html_doc = res.text
	soup = BeautifulSoup(html_doc, 'html.parser')	

	scraped_conjugation = u""
	for tr in soup.find(id=mode).find_all_next("table")[section_code + 1].find_all("tr")[1:]:
		if code == 17 or code == 18:
			subject = u""
		else:
			subject = tr.td.get_text().replace(u'\xa0', u' ')
		verb = tr.td.next_sibling.next_sibling.get_text()
		scraped_conjugation += u"{}{}\n".format(subject, verb)
	
	return scraped_conjugation