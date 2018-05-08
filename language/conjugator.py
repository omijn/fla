# coding=utf-8
import strings
import wiki_telecharger_fr as wtf

tenses = [
	{	
		"code": 0,
		"mode": strings.MODES["IND"],		
		"name": strings.TENSES["IND_PRES"]
	},
	{	
		"code": 1,
		"mode": strings.MODES["IND"],		
		"name": strings.TENSES["IND_PC"]
	},
	{	
		"code": 2,
		"mode": strings.MODES["IND"],		
		"name": strings.TENSES["IND_IPF"]
	},	
	{	
		"code": 3,
		"mode": strings.MODES["IND"],		
		"name": strings.TENSES["IND_PQP"]
	},
	{			
		"code": 4,
		"mode": strings.MODES["IND"],		
		"name": strings.TENSES["IND_PS"]
	},
	{	
		"code": 5,
		"mode": strings.MODES["IND"],		
		"name": strings.TENSES["IND_PA"]
	},
	{	
		"code": 6,
		"mode": strings.MODES["IND"],		
		"name": strings.TENSES["IND_FS"]
	},
	{	
		"code": 7,
		"mode": strings.MODES["IND"],		
		"name": strings.TENSES["IND_FA"]
	},
	{	
		"code": 9,
		"mode": strings.MODES["SUBJ"],
		"name": strings.TENSES["SUBJ_PRES"]
	},
	{	
		"code":  10,
		"mode": strings.MODES["SUBJ"],
		"name": strings.TENSES["SUBJ_P"]
	},
	{	
		"code": 11,
		"mode": strings.MODES["SUBJ"],
		"name": strings.TENSES["SUBJ_IMP"]
	},
	{	
		"code": 12,
		"mode": strings.MODES["SUBJ"],
		"name": strings.TENSES["SUBJ_PQP"]
	},
	{	
		"code": 14,
		"mode": strings.MODES["COND"],		
		"name": strings.TENSES["COND_PRES"]
	},
	{	
		"code": 15,
		"mode": strings.MODES["COND"],		
		"name": strings.TENSES["COND_P"]
	},
	{	
		"code": 17,
		"mode": strings.MODES["IMP"],
		"name": strings.TENSES["IMP_PRES"]
	},
	{	
		"code": 18,
		"mode": strings.MODES["IMP"],
		"name": strings.TENSES["IMP_P"]
	}
]

def conjugate(verb, tense):
	"""Conjugate given verb in given tense.
	
	Returns a string.
	"""

	tense_obj = get_obj_from_name(tense)	
	preamble = u"{}\n{} {}\n\n".format(verb, tense_obj['mode'], tense_obj['name'])
	conjugation = wtf.scrape(verb, tense_obj['code'])
	final_conjugation = preamble + conjugation

	return final_conjugation

def get_obj_from_name(tensename):
	return filter(lambda t: t['name'] == tensename, tenses)[0]

def get_code_from_name(tensename):
	return filter(lambda t: t['name'] == tense, tenses)[0]['code']

def get_mode_from_code(tensecode):
	return filter(lambda t: t['code'] == tensecode, tenses)[0]['mode']

def get_name_from_code(tensecode):
	return filter(lambda t: t['code'] == tensecode, tenses)[0]['name']
