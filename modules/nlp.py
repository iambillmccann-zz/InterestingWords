""" These are a collection of NLP helper functions

These are a few helper functions for simple NLP. I'm not going to go crazy here
as this is a tech test and not a commercial project. In most cases default models
are used.

    Typical usage:

    from modules import nlp
"""
from nltk import sent_tokenize

def get_sentences(content):
    """ Retrieve the sentences from a string of text
    
    Use the default sent_tokenizer to parse the content into sentences.
    NOTE: If the results are poor, then train a new model of PunkSentenceTokenizer.
    Funny thing, after reviewing the results, a simple "content.split('.') is
    probably sufficient.

    Args:
        content: A string containing the text to break into sentences

    Return:
        A list of sentences
    """
    return sent_tokenize(content)