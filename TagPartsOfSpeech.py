""" This script is the third step of the data pipeline, it marks sentences with POS (Parts of Speech) tags

This program will tag the sentences that have been classified by sentiment for parts of speech. Again, for
expediency, NLTK default models are used.

    Typical usage:

    $ python TagPartsOfSpeech.py

Note: Input and output files are found in the /output folder.
"""
import pandas

from modules import nlp
from modules import utilities

def main():

    corpus = pandas.read_csv(utilities.CORPUS_WITH_SENTIMENT, index_col = 'id')
    corpus['parts_of_speech'] = corpus.apply(lambda row: nlp.tag_parts_of_speech(row['sentence']), axis=1)
    corpus.to_csv(utilities.CORPUS_POS)

if __name__ == '__main__':
    main()