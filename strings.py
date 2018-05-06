# coding=utf-8

#dialogflow

CONJUGATE_INTENT = "conjugate"
CONJUGATE_MORE_INTENT = "conjugateMore"
CONJUGATE_VERB_INTENT = "conjugateVerb"
GENDER_INTENT    = "genderWord"
NUMERIC_INTENT   = "numbers"
PRONOUNCE_INTENT = "pronounce"
TRANSLATE_INTENT = "translate"
SENTENCE_INTENT  = "useInSentence"
WORD_INTENT      = "defineWord"
FALLBACK_INTENT  = "fallback"

DATA_SOURCE = "Google/Wiktionary/Other"

# FB quick reply payloads
PAYLOAD_CONJUGATE = "conj"
PAYLOAD_DELIMITER = "<::>"

SHOW_MORE_TENSES = "More"
HOW_TO_CONJ = "How do you want to conjugate the verb?"


# genders
WORD_NOT_FOUND = "Sorry, that word was not found."

# conjugation
VERB_NOT_FOUND = "Sorry, that verb was not found."

# API endpoints and data sources

	# google translate
GT_DETECT = "https://translation.googleapis.com/language/translate/v2/detect"
GT_TRANSLATE = "https://translation.googleapis.com/language/translate/v2"

	# wiktionary
WIKI_FR_CJGTR = "https://fr.wiktionary.org/wiki/Annexe:Conjugaison_en_français/"