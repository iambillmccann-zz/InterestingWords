""" This script is the first step of the data pipeline for analyzing "Interesting Words"

This program will read files from the corpus, will break the content into sentences
and will score the sentences for sentiment (positive or negative). The results are
written to a file for processing by the next step.

    Typical usage example:

    $ python ParseSentences.py

Note: It is presumed that the data files are in a folder named "corpus". The corpus
folder is in the same folder as this script.
"""
import pandas

from modules import utilities
from modules import nlp

DATA_FOLDER = "./corpus"

def main():

    the_files = utilities.get_file_names(DATA_FOLDER)
    corpus = pandas.DataFrame(columns = ['sentence', 'file_name', 'location'])

    for file_name in the_files:
        corpus = corpus.append(                                      # append new data
            (utilities.make_dataframe(                               # make a data from from sentences
                (nlp.get_sentences(                                  # use nltk to get sentences
                    utilities.get_content(DATA_FOLDER, file_name))), # obtain the content from the file                 
                file_name)
            ), 
            ignore_index = True)                                     # end of the .append function call

    corpus.to_csv(utilities.corpus_metadata_file_name())

if __name__ == '__main__':
    main()