""" This script add the sentiment score to each sentence in the corpus.

This file reads a csv/dataframe created by a previous step in the data pipeline.
Each sentence is marked with three scores ... positive, neutral, and negative. The
scores are real numbers between 0 and 1. These numbers are probabilities. As this is
a programming exercise, and not a data science exercise, I am using a "cheat" and
calling an API that is a sentiment model based on NLTK.

The results are returned as JSON. The json contains the following ...

    label: A classifier of "pos", "neg" or "neutral"
    probability: A list of three probabilities described as ...
    neg: The probability that the sentence is negative
    pos: The probability that the sentence is positive
    neutral: The probability that the sentence is neither positive nor negative

    Typical usage:

    $ python DetermineSentiment.py

Note: Input and output files are presumed to be in the /output folder.
"""
import pandas

from modules import utilities
from modules import restclient

def main():

    corpus = pandas.read_csv(utilities.CORPUS_METADATA_FILE_NAME, index_col = 'id')
    
    # make the API calls
    try:
        corpus['result'] = corpus.apply(lambda row: restclient.get_sentiment_scores(row['sentence']), axis = 1)
    except Exception as api_error:
        print(api_error)
        exit(-1)

    # parse the values out of the http response
    corpus['label'] = corpus.apply(lambda row: row['result']['label'], axis = 1)
    corpus['negative'] = corpus.apply(lambda row: row['result']['probability']['neg'], axis = 1)
    corpus['positive'] = corpus.apply(lambda row: row['result']['probability']['pos'], axis = 1)
    corpus['neutral'] = corpus.apply(lambda row: row['result']['probability']['neutral'], axis = 1)
    
    # drop the http response and write the dataframe to disk
    ( corpus.drop(['result'], axis = 1)
        .to_csv(utilities.CORPUS_WITH_SENTIMENT) )

if __name__ == '__main__':
    main()