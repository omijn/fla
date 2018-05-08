# coding=utf-8

#dialogflow

CONJUGATE_INTENT = "conjugate"
CONJUGATE_MORE_INTENT = "conjugateMore"
CONJUGATE_VERB_INTENT = "conjugateVerbFallback"
GENDER_INTENT    = "genderWord"
NUMERIC_INTENT   = "numbers"
PRONOUNCE_INTENT = "pronounce"
TRANSLATE_INTENT = "translate"
SENTENCE_INTENT  = "useInSentence"
WORD_INTENT      = "defineWord"
FALLBACK_INTENT  = "fallback"

DATA_SOURCE = "Google/Wiktionary/Other"

# conjugations
SHOW_MORE_TENSES = "More"
HOW_TO_CONJ = "How do you want to conjugate the verb?"

TENSES = {
	"IND_PRES": "Présent",
	"IND_PC": "Passé Composé",
	"IND_IPF": "Imparfait",
	"IND_PQP": "Plus-que-parfait",
	"IND_PS": "Passé Simple",
	"IND_PA": "Passé Antérieur",
	"IND_FS": "Futur Simple",
	"IND_FA": "Futur Antérieur",
	"SUBJ_PRES": "Présent: subj.",
	"SUBJ_P": "Passé: subj.",
	"SUBJ_IMP": "Imparfait: subj.",
	"SUBJ_PQP": "Plus-que-parfait:sub",
	"COND_PRES": "Présent: cond.",
	"COND_P": "Passé: cond.",
	"IMP_PRES": "Présent: imp.",
	"IMP_P": "Passé: imp."
}

MODES = {
	"IND": "Indicatif",
	"SUBJ": "Subjonctif",
	"COND": "Conditionnel",
	"IMP": "Impératif"
}

VERB_NOT_FOUND = "Sorry, that verb was not found."

# genders
WORD_NOT_FOUND = "Sorry, that word was not found."

# API endpoints and data sources

## google translate
GT_DETECT = "https://translation.googleapis.com/language/translate/v2/detect"
GT_TRANSLATE = "https://translation.googleapis.com/language/translate/v2"

## wiktionary
WIKI_FR_CJGTR = "https://fr.wiktionary.org/wiki/Annexe:Conjugaison_en_français/"