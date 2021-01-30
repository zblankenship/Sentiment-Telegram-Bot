import os
from dotenv import load_dotenv
import paralleldots
load_dotenv('key.env')
paralleldots.set_api_key(os.getenv('paralleldots'))

def sentiment_check(text):
    lang_code="en"
    response=paralleldots.sentiment(text,lang_code)
    return(response)