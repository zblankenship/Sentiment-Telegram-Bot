import os
from dotenv import load_dotenv
import paralleldots
from sentiment_errors import error_check
import operator
import random
load_dotenv('key.env')
paralleldots.set_api_key(os.getenv('paralleldots'))

def sentiment_check(text):
    lang_code="en"
    response=paralleldots.sentiment(text,lang_code)
    response = error_check(response)
    return(response)

def get_largest(text):
    sentiment_dict = text.get('sentiment')
    largest = max(sentiment_dict.items(), key=operator.itemgetter(1))[0]
    return largest
    


if __name__ == "__main__":
    text = "This is a test"
    results = sentiment_check(text)
    largest = get_largest(results)
    to_send = pick_message(largest)