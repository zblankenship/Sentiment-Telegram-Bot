import os
from dotenv import load_dotenv
import paralleldots
from sentiment_errors import error_check
load_dotenv('key.env')
paralleldots.set_api_key(os.getenv('paralleldots'))

def sentiment_check(text):
    lang_code="en"
    response=paralleldots.sentiment(text,lang_code)
    response = error_check(response)
    return(response)

if __name__ == "__main__":
    text = "This is a test"
    print(sentiment_check(text))