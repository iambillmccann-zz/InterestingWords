""" This script formats the data from the interesting_words (see InterestingWords.py) into a table for reporting

    Typical usage:

    $ python PrepareTable.py

Note. The files needed to product the file table are in the ./output folder.
"""
import pandas

from modules import utilities

def main():

    interesting_words = pandas.read_csv(utilities.INTERESTING_WORDS, index_col = 'word')
    corpus_pos = pandas.read_csv(utilities.CORPUS_POS, index_col = 'id')

    FinalReport = ( interesting_words.drop(['count'], axis = 1)
        .join( utilities.map_words(corpus_pos) )
        .rename(columns = { "file_name" : "files" })
        .sort_values(by = ['count'], ascending = False)
        .head(20) )

    FinalReport.to_csv(utilities.FINAL_REPORT)

if __name__ == '__main__':
    main()