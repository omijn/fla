# coding=utf-8

import wiki_telecharger_fr as wtf

tenses = [
	{	
		"code": 0,
		"mode": "Indicatif",		
		"name": "Présent"
	},
	{	
		"code": 1,
		"mode": "Indicatif",		
		"name": "Passé Composé"
	},
	{	
		"code": 2,
		"mode": "Indicatif",		
		"name": "Imparfait"
	},
	{	
		"code": 3,
		"mode": "Indicatif",		
		"name": "Plus-que-parfait"
	},
	{			
		"code": 4,
		"mode": "Indicatif",		
		"name": "Passé Simple"
	},
	{	
		"code": 5,
		"mode": "Indicatif",		
		"name": "Passé Antérieur"
	},
	{	
		"code": 6,
		"mode": "Indicatif",		
		"name": "Futur Simple"
	},
	{	
		"code": 7,
		"mode": "Indicatif",		
		"name": "Futur Antérieur"
	},
	{	
		"code": 8,
		"mode": "Subjonctif",		
		"name": "Présent"
	},
	{	
		"code":  9,
		"mode": "Subjonctif",		
		"name": "Passé"
	},
	{	
		"code": 10,
		"mode": "Subjonctif",		
		"name": "Imparfait"
	},
	{	
		"code": 11,
		"mode": "Subjonctif",		
		"name": "Plus-que-parfait"
	},
	{	
		"code": 12,
		"mode": "Conditionnel",		
		"name": "Présent"
	},
	{	
		"code": 13,
		"mode": "Conditionnel",		
		"name": "Passé"
	},
	{	
		"code": 14,
		"mode": "Impératif",		
		"name": "Présent"
	},
	{	
		"code": 15,
		"mode": "Impératif",		
		"name": "Passé"
	}
]

def conjugate(verb, tense_code):
	"""Conjugate given verb in given tense.
	
	Returns a string.
	"""

	preamble = "{}\n{}{}\n\n".format(verb, tenses[tense_code].mode, tenses[tense_code].name)
	conjugation = wtf.scrape(verb, tense_code)
	final_conjugation = preamble + conjugation

	return final_conjugation
