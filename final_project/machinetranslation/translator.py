import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#auth
authenticator = IAMAuthenticator(apikey)

#service setup
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    if englishText is None: 
        return None

    frenchText = language_translator.translate(text=englishText, model_id='en-fr').get_result()
    return frenchText['translations'][0]['translation']

def frenchToEnglish(frenchText):
    if frenchText is None: 
        return None

    englishText = language_translator.translate(text=frenchText, model_id='fr-en').get_result()
    return englishText['translations'][0]['translation']
