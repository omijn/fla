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
	"IND_PRES": u"Présent",
	"IND_PC": u"Passé Composé",
	"IND_IPF": u"Imparfait",
	"IND_PQP": u"Plus-que-parfait",
	"IND_PS": u"Passé Simple",
	"IND_PA": u"Passé Antérieur",
	"IND_FS": u"Futur Simple",
	"IND_FA": u"Futur Antérieur",
	"SUBJ_PRES": u"Présent: subj.",
	"SUBJ_P": u"Passé: subj.",
	"SUBJ_IMP": u"Imparfait: subj.",
	"SUBJ_PQP": u"Plus-que-parfait:sub",
	"COND_PRES": u"Présent: cond.",
	"COND_P": u"Passé: cond.",
	"IMP_PRES": u"Présent: imp.",
	"IMP_P": u"Passé: imp."
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