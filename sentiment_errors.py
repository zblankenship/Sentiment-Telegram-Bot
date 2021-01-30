def error_check(response):
    if response == 304:
        response = "There is no new text to return"
    elif response == 500:
        response = "Backend Error."
    elif response == 400:
        response = "Please provide valid input parameter."
    elif response == 401:
        response = "Invalid Credentials. Invalid API key"
    elif response == 403:
        response = "Daily/Monthy Limit Exceeded."
    elif response == 429:
        response = "Please slow down"
    elif response == 406:
        response = "Invalid Format for any of the parameters. For e.g.:sending api_key as integer instead of string."
    else:
        pass
    return(response)