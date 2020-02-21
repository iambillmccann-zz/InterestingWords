""" This script is the first step of the data pipeline for analyzing "Interesting Words"

This program will read files from the corpus, will break the content into sentences
and will score the sentences for sentiment (positive or negative). The results are
written to a file for processing by the next step.

    Typical usage example:

    $ python ParseSentences.py

Note: It is presumed that the data files are in a folder named "corpus". The corpus
folder is in the same folder as this script.
"""
from modules import utilities
from modules import nlp

DATA_FOLDER = "./corpus"

def main():

    the_files = utilities.get_file_names(DATA_FOLDER)
    for file_name in the_files:
        content = utilities.get_content(DATA_FOLDER, file_name)
        sentences = nlp.get_sentences(content)
        print(len(sentences))

if __name__ == '__main__':
    main()