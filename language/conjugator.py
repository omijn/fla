# coding=utf-8
import strings
import wiki_telecharger_fr as wtf

tenses = [
	{	
		"code": 0,
		"section_code": 0,
		"mode": strings.MODES["IND"],		
		"name": strings.TENSES["IND_PRES"]["name"],
		"shortname": strings.TENSES["IND_PRES"]["shortname"]
	},
	{	
		"code": 1,
		"section_code": 1,
		"mode": strings.MODES["IND"],		
		"name": strings.TENSES["IND_PC"]["name"],
		"shortname": strings.TENSES["IND_PC"]["shortname"]
	},
	{	
		"code": 2,
		"section_code": 2,
		"mode": strings.MODES["IND"],		
		"name": strings.TENSES["IND_IPF"]["name"],
		"shortname": strings.TENSES["IND_IPF"]["shortname"]
	},	
	{	
		"code": 3,
		"section_code": 3,
		"mode": strings.MODES["IND"],		
		"name": strings.TENSES["IND_PQP"]["name"],
		"shortname": strings.TENSES["IND_PQP"]["shortname"]
	},
	{			
		"code": 4,
		"section_code": 4,
		"mode": strings.MODES["IND"],		
		"name": strings.TENSES["IND_PS"]["name"],
		"shortname": strings.TENSES["IND_PS"]["shortname"]
	},
	{	
		"code": 5,
		"section_code": 5,
		"mode": strings.MODES["IND"],		
		"name": strings.TENSES["IND_PA"]["name"],
		"shortname": strings.TENSES["IND_PA"]["shortname"]
	},
	{	
		"code": 6,
		"section_code": 6,
		"mode": strings.MODES["IND"],		
		"name": strings.TENSES["IND_FS"]["name"],
		"shortname": strings.TENSES["IND_FS"]["shortname"]
	},
	{	
		"code": 7,
		"section_code": 7,
		"mode": strings.MODES["IND"],		
		"name": strings.TENSES["IND_FA"]["name"],
		"shortname": strings.TENSES["IND_FA"]["shortname"]
	},
	{	
		"code": 9,
		"section_code": 0,
		"mode": strings.MODES["SUBJ"],
		"name": strings.TENSES["SUBJ_PRES"]["name"],
		"shortname": strings.TENSES["SUBJ_PRES"]["shortname"]
	},
	{	
		"code":  10,
		"section_code": 1,
		"mode": strings.MODES["SUBJ"],
		"name": strings.TENSES["SUBJ_P"]["name"],
		"shortname": strings.TENSES["SUBJ_P"]["shortname"]
	},
	{	
		"code": 11,
		"section_code": 2,
		"mode": strings.MODES["SUBJ"],
		"name": strings.TENSES["SUBJ_IMP"]["name"],
		"shortname": strings.TENSES["SUBJ_IMP"]["shortname"]
	},
	{	
		"code": 12,
		"section_code": 3,
		"mode": strings.MODES["SUBJ"],
		"name": strings.TENSES["SUBJ_PQP"]["name"],
		"shortname": strings.TENSES["SUBJ_PQP"]["shortname"]
	},
	{	
		"code": 14,
		"section_code": 0,
		"mode": strings.MODES["COND"],		
		"name": strings.TENSES["COND_PRES"]["name"],
		"shortname": strings.TENSES["COND_PRES"]["shortname"]
	},
	{	
		"code": 15,
		"section_code": 1,
		"mode": strings.MODES["COND"],		
		"name": strings.TENSES["COND_P"]["name"],
		"shortname": strings.TENSES["COND_P"]["shortname"]
	},
	{	
		"code": 17,
		"section_code": 0,
		"mode": strings.MODES["IMP"],
		"name": strings.TENSES["IMP_PRES"]["name"],
		"shortname": strings.TENSES["IMP_PRES"]["shortname"]
	},
	{	
		"code": 18,
		"section_code": 1,
		"mode": strings.MODES["IMP"],
		"name": strings.TENSES["IMP_P"]["name"],
		"shortname": strings.TENSES["IMP_P"]["shortname"]
	}
]

def conjugate(verb, tense):
	"""Conjugate given verb in given tense.
	
	Returns a string.
	"""

	tense_obj = get_obj_from_name(tense)	
	preamble = u"{}\n{} ({})\n\n".format(verb, tense_obj['shortname'], tense_obj['mode'])
	conjugation = wtf.scrape(verb=verb, mode=tense_obj['mode'], section_code=tense_obj['section_code'], code=tense_obj['code'])
	final_conjugation = preamble + conjugation

	return final_conjugation

def get_obj_from_name(tensename):
	# the object returned by filter() is different in Python 2 and Python 3
	return filter(lambda t: t['name'] == tensename, tenses)[0]	

