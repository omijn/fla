# coding=utf-8

import wiki_telecharger_fr as wtf

tenses = [
	{
		"code": "present",
		"title": "Présent",		
	},

	{
		"code": "simple_past",
		"title": "Passé Simple"
	},

	{
		"code": "past",
		"title": "Passé Composé"
	}
]

def conjugate(verb, tense):
	"""Conjugate given verb in given tense.
	
	Returns a string.
	"""

	conjugation = wtf.scrape(verb, tense)

	return "sample conjugation"
