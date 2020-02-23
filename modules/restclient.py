""" These are the helper functions for calling the restful API to retrieve sentiment scores.

For expediency sake, url and header values are hard coded. Since I am only calling one
restful endpoint, there is no need to write general purpose POST methods.

    Typical usage:

    from modules import restclient
"""
import json
import requests

def get_sentiment_scores(sentence):
    """ Call an API to retrieve sentiment scores for a sentence

    This function formats an http post call to an API to retrieve sentiment
    scores. The API works by including form data in the request body. This
    form data is provided as a raw string.

    Args:
        sentence: The sentence to check against the API

    Returns:
        The response body as a dictionary

    Raises:
        A general exception if the API returns a status code other than 200
    """
    url = 'http://text-processing.com/api/sentiment/'
    body = 'text={}'.format(sentence).encode('utf-8')    # utf-8 encoding to support apostrophies
    content_length = str(len(body))
    headers = { 'User-Agent' : 'Python/3.6.8',
                'Accept' : '*/*',
                'Cache-Control' : 'no-cache',
                'Python-Token' : 'c3903cfb-dd36-4fda-9b28-c46be24baa71',
                'Host' : 'text-processing.com',
                'Accept-Encoding' : 'gzip, deflate, br',
                'Content-Length' : content_length,
                'Connection' : 'keep-alive'
     }

    response = requests.post(url = url, headers = headers, data = body)
    if response.status_code != 200:
        raise Exception('The API returned an error. The http status code is {}'.format(response.status_code))

    return response.json()