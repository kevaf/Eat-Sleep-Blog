import requests

def get_blogQuotes():
    """
    function to get json response to url requests
    """
    get_response = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    return get_response