# coding=utf-8

#dialogflow

CONJUGATE_INTENT = u"conjugate"
CONJUGATE_MORE_INTENT = u"conjugateMore"
CONJUGATE_VERB_INTENT = u"conjugateVerbFallback"
GENDER_INTENT    = u"genderWord"
NUMERIC_INTENT   = u"numbers"
PRONOUNCE_INTENT = u"pronounce"
TRANSLATE_INTENT = u"translate"
SENTENCE_INTENT  = u"useInSentence"
WORD_INTENT      = u"defineWord"
FALLBACK_INTENT  = u"fallback"

DATA_SOURCE = u"Google/Wiktionary/Other"

# conjugations
SHOW_MORE_TENSES = u"More"
HOW_TO_CONJ = u"How do you want to conjugate the verb?"

TENSES = {
	"IND_PRES" : {"name": u"Présent",              "shortname": u"Présent"},
	"IND_PC"   : {"name": u"Passé Composé",        "shortname": u"Passé Composé"},
	"IND_IPF"  : {"name": u"Imparfait",            "shortname": u"Imparfait"},
	"IND_PQP"  : {"name": u"Plus-que-parfait",     "shortname": u"Plus-que-parfait"},
	"IND_PS"   : {"name": u"Passé Simple",         "shortname": u"Passé Simple"},
	"IND_PA"   : {"name": u"Passé Antérieur",      "shortname": u"Passé Antérieur"},
	"IND_FS"   : {"name": u"Futur Simple",         "shortname": u"Futur Simple"},
	"IND_FA"   : {"name": u"Futur Antérieur",      "shortname": u"Futur Antérieur"},
	"SUBJ_PRES": {"name": u"Présent: subj.",       "shortname": u"Présent"},
	"SUBJ_P"   : {"name": u"Passé: subj.",         "shortname": u"Passé"},
	"SUBJ_IMP" : {"name": u"Imparfait: subj.",     "shortname": u"Imparfait"},
	"SUBJ_PQP" : {"name": u"Plus-que-parfait:sub", "shortname": u"Plus-que-parfait"},
	"COND_PRES": {"name": u"Présent: cond.",       "shortname": u"Présent"},
	"COND_P"   : {"name": u"Passé: cond.",         "shortname": u"Passé"},
	"IMP_PRES" : {"name": u"Présent: imp.",        "shortname": u"Présent"},
	"IMP_P"    : {"name": u"Passé: imp.",          "shortname": u"Passé"}
}

MODES = {
	"IND": u"Indicatif",
	"SUBJ": u"Subjonctif",
	"COND": u"Conditionnel",
	"IMP": u"Impératif"
}

VERB_NOT_FOUND = u"Sorry, that verb was not found."

# genders
WORD_NOT_FOUND = u"Sorry, that word was not found."

# API endpoints and data sources

## google translate
GT_DETECT = u"https://translation.googleapis.com/language/translate/v2/detect"
GT_TRANSLATE = u"https://translation.googleapis.com/language/translate/v2"

## wiktionary
WIKI_FR_CJGTR = u"https://fr.wiktionary.org/wiki/Annexe:Conjugaison_en_français/"