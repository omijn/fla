# coding=utf-8
from google.cloud import translate

translate_client = translate.Client()

def translate(text, source, target):
	translation = translate_client.translate(text, source_language=source, target_language=target, format_="text")
	
	return translation['translatedText']

def detect(text):
	result = translate_client.detect_language(text)
	return result['language']