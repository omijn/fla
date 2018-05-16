# coding=utf-8

import json

import strings
import language.conjugator
import language.gender.gender_fr
from language import translator

from num2words import num2words

# import .language.pronouncer
# import .language.examples


class Parser():
    """Parse incoming requests from Dialogflow"""

    def __init__(self):
        self.formatter = Formatter()

    def parse(self, data):
        lang = data['queryResult']['languageCode']
        intent = data['queryResult']['intent']['displayName']
        response = ""

        if intent == strings.CONJUGATE_INTENT:
            # verb = data['queryResult']['parameters']['frenchVerb']
            response = self.formatter.ask_verb_tense()

        elif intent == strings.CONJUGATE_MORE_INTENT:
            response = self.formatter.ask_verb_tense(userWantsMoreOptions=True)

        elif intent == strings.CONJUGATE_VERB_INTENT:
            verb = data['queryResult']['outputContexts'][0]['parameters']['frenchVerb']
            tense = data['queryResult']['queryText']
            conjugation = language.conjugator.conjugate(verb, tense)
            response = self.formatter.display_conjugation(conjugation)

        elif intent == strings.GENDER_INTENT:
            word = data['queryResult']['parameters']['word']
            g = language.gender.gender_fr.get_gender(word)
            response = self.formatter.display_gender(word, g)

        elif intent == strings.NUMERIC_INTENT:
            number = data['queryResult']['parameters']['number']
            word_form_en = num2words(number, lang='en')
            word_form_fr = num2words(number, lang='fr')
            response = self.formatter.display_number(
                word_form_en, word_form_fr)

        elif intent == strings.PRONOUNCE_INTENT:
            pass
            # response = pronouncer.pronounce()

        elif intent == strings.TRANSLATE_INTENT:
            pass
            # response = translator.translate_sentence()

        elif intent == strings.SENTENCE_INTENT:
            pass
            # response = examplestrings.get_example()

        elif intent == strings.WORD_INTENT:
            # response = translator.translate_word()
            pass

        elif intent == strings.FALLBACK_INTENT:
            # assume the user wants to translate something
            text = data['queryResult']['queryText']
            source = translator.detect(text)
            if source == strings.ISO_639_1_ENGLISH:
                target = strings.ISO_639_1_FRENCH
            else:
                target = strings.ISO_639_1_ENGLISH

            translation = translator.translate(text, source, target)

            try:
                source = strings.LANGUAGES[source]
                target = strings.LANGUAGES[target]
            except KeyError:
                pass

            response = self.formatter.display_translation(
                translation, source, target)

        return response


class Formatter:
    """Format outgoing responses to Dialogflow"""

    def __init__(self):
        pass

    def ask_verb_tense(self, userWantsMoreOptions=False):
        """Ask the user what tense to conjugate the given verb in.
            Facebook: Use quick replies
        """

        if userWantsMoreOptions:
            quick_replies = [tense['name']
                             for tense in language.conjugator.tenses[9:]]
        else:
            quick_replies = [tense['name']
                             for tense in language.conjugator.tenses[:9]]
            quick_replies.append(strings.SHOW_MORE_TENSES)

        print(quick_replies)

        response = {
            "fulfillmentText": strings.HOW_TO_CONJ,
            "fulfillmentMessages": [
                {
                    "quickReplies": {
                        "title": strings.HOW_TO_CONJ,
                        "quickReplies": quick_replies
                    },
                    "platform": "FACEBOOK"
                }
            ],
            "outputContexts": [],
            "source": strings.DATA_SOURCE,
            "followupEventInput": {}
        }

        return json.dumps(response)

    def display_conjugation(self, conjugation):
        response = {
            "fulfillmentText": conjugation,
            "payload": {},
            "outputContexts": [],
            "source": strings.DATA_SOURCE,
            "followupEventInput": {}
        }

        return json.dumps(response)

    def display_gender(self, word, gender_code):
        if gender_code in language.gender.gender_fr.genders:
            msg = u"{} is {}".format(
                word, language.gender.gender_fr.genders[gender_code])
        else:
            msg = strings.WORD_NOT_FOUND

        response = {
            "fulfillmentText": msg,
            "payload": {},
            "outputContexts": [],
            "source": strings.DATA_SOURCE,
            "followupEventInput": {}
        }

        return json.dumps(response)

    def display_number(self, num_en, num_fr):

        word_form = u"FR: {}\n\nEN: {}".format(num_fr, num_en)
        response = {
            "fulfillmentText": word_form,
            "payload": {},
            "outputContexts": [],
            "source": strings.DATA_SOURCE,
            "followupEventInput": {}
        }

        return json.dumps(response)

    def display_translation(self, translation, source, target):

        trans = u"{}\n\n(translated from {} to {})".format(
            translation, source, target)
        response = {
            "fulfillmentText": trans,
            "payload": {},
            "outputContexts": [],
            "source": strings.DATA_SOURCES["translation"],
            "followupEventInput": {}
        }

        return json.dumps(response)
