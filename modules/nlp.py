""" These are a collection of NLP helper functions

These are a few helper functions for simple NLP. I'm not going to go crazy here
as this is a tech test and not a commercial project. In most cases default models
are used.

    Typical usage:

    from modules import nlp
"""
import json
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
INTERESTING_WORDS = ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']

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

def tag_parts_of_speech(sentence):
    """ Use NLTK to tag parts of speech

    Call nltk word_tokenize to tag POS. Also filter out stop words. I am using
    the nltk default English stop words.

    Args:
        sentence: a sentence or phrase to tag POS

    Returns:
        list of tagged words
    """
    words = word_tokenize(sentence)
    words = [w for w in words if not w in stop_words]
    return json.dumps(pos_tag(words))

def filter_descriptive_words(parts_of_speech):
    """ Filter out words that are not interesting

    Check the tags on the words to verify that they are adjectives or adverbs.
    The list of appropriate tags is contained in the constant INTERESTING_WORDS.

    Args:
        parts_of_speech: A serialized json string containing the list of tagged words.

    Returns:
        A serialized json string of adjectives and adverbs.
    """
    words = json.loads(parts_of_speech)
    words = [ word for word in words if word[1] in INTERESTING_WORDS ]
    return json.dumps(words)