# coding=utf-8

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
		"code": 8,
		"mode": strings.MODES["SUBJ"],
		"name": strings.TENSES["SUBJ_PRES"]
	},
	{	
		"code":  9,
		"mode": strings.MODES["SUBJ"],
		"name": strings.TENSES["SUBJ_P"]
	},
	{	
		"code": 10,
		"mode": strings.MODES["SUBJ"],
		"name": strings.TENSES["SUBJ_IMP"]
	},
	{	
		"code": 11,
		"mode": strings.MODES["SUBJ"],
		"name": strings.TENSES["SUBJ_PQP"]
	},
	{	
		"code": 12,
		"mode": strings.MODES["COND"],		
		"name": strings.TENSES["COND_PRES"]
	},
	{	
		"code": 13,
		"mode": strings.MODES["COND"],		
		"name": strings.TENSES["COND_P"]
	},
	{	
		"code": 14,
		"mode": strings.MODES["IMP"],
		"name": strings.TENSES["IMP_PRES"]
	},
	{	
		"code": 15,
		"mode": strings.MODES["IMP"],
		"name": strings.TENSES["IMP_P"]
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
