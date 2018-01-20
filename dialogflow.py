import json

import strings
import language.conjugator
import language.gender.gender_fr

from num2words import num2words

# import .language.pronouncer
# import .language.translator
# import .language.examples


class Parser():
    """Parse incoming requests from Dialogflow"""

    def __init__(self):
        
        self.formatter = Formatter()

    def parse(self, data):
        lang = data['lang']
        intent = data['result']['metadata']['intentName']
        response = ""        

        if intent == strings.CONJUGATE_INTENT:
            verb = data['result']['parameters']['word']
            response = self.formatter.ask_verb_tense(verb)
        
        elif intent == strings.GENDER_INTENT:
            word = data['result']['parameters']['word']
            g = language.gender.gender_fr.get_gender(word)
            response = self.formatter.display_gender(word, g)            

        elif intent == strings.NUMERIC_INTENT:
            number = data['result']['parameters']['number']
            word_form_en = num2words(number, lang='en')
            word_form_fr = num2words(number, lang='fr')
            response = self.formatter.display_number(word_form_en, word_form_fr)

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
            if 'quick_reply' in data['originalRequest']['data']['message']:
                payload = data['originalRequest']['data']['message']['quick_reply']['payload']
                parts = payload.split(strings.PAYLOAD_DELIMITER)

                if parts[0] == strings.PAYLOAD_CONJUGATE:
                    conjugation = language.conjugator.conjugate(verb=parts[1], tense_code=parts[2])
                    response = self.formatter.conjugate_verb(conjugation)
                    
        return response     

class Formatter:
    """Format outgoing responses to Dialogflow"""

    def __init__(self):
        pass

    def ask_verb_tense(self, verb):
        """Ask the user what tense to conjugate the given verb in.
            Facebook: Use quick replies
        """

        response = {
            "speech": strings.HOW_TO_CONJ,
            "displayText": strings.HOW_TO_CONJ,
            "data": {
                "facebook": {
                    "text": strings.HOW_TO_CONJ,
                    "quick_replies":[]
                }
            },
            "contextOut": [],
            "source": strings.DATA_SOURCE,
            "followupEvent": {}
        }

        quick_replies = [{"content_type":"text", "title": tense['name'], "payload": "{}{}{}{}{}".format(strings.PAYLOAD_CONJUGATE, strings.PAYLOAD_DELIMITER, verb, strings.PAYLOAD_DELIMITER, tense['code'])} for tense in language.conjugator.tenses]
        response['data']['facebook']['quick_replies'].extend(quick_replies)

        return json.dumps(response)

    def conjugate_verb(self, conjugation):
        response = {
            "speech": conjugation,
            "displayText": conjugation,
            "data": {},
            "contextOut": [],
            "source": strings.DATA_SOURCE,
            "followupEvent": {}
        }

        return json.dumps(response)

    def display_gender(self, word, gender_code):
        if gender_code in language.gender.gender_fr.genders:
            msg = u"{} is {}".format(word, language.gender.gender_fr.genders[gender_code])
        else:
            msg = strings.WORD_NOT_FOUND

        response = {
            "speech": msg,
            "displayText": msg,
            "data": {},
            "contextOut": [],
            "source": strings.DATA_SOURCE,
            "followupEvent": {}
        }

        return json.dumps(response)

    def display_number(self, num_en, num_fr):

        word_form = u"FR: {}\n\nEN: {}".format(num_fr, num_en)
        response = {
            "speech": word_form,
            "displayText": word_form,
            "data": {},
            "contextOut": [],
            "source": strings.DATA_SOURCE,
            "followupEvent": {}
        }

        return json.dumps(response)