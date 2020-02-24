""" This script creates three lists; positive words, negative words, and interesting words.

This script uses the words tagged with part of speech (see TagPartsOfSpeech.py). It will create three different
lists of words. To understand these lists, it is important to define what is meant by "interesting words". For
this exercise, here are how "interesting words" are described ...

    What makes words interesting is their power to influence thoughts or emotions. Of course things (nouns) and actions
    (verbs) can be powerful, but it are descriptions that bring words to life. You can "strike with the hammer" or you
    can "firmly strike with a heavy iron hammer". This study will determine the words used most frequently to evoke a
    a positive or negative sentiment.

This process starts by filtering out the neutral sentences from our corpus. The words will be broken into two groups, one
positive and the other negative. Word counts from their respective sentences will be computed. The top fifty words in each
group are saved. (These will be used later to create Word Clouds of influencial words.) The two lists are merged to 
determine a final list of top ten (or twenty?) "interesting words".

Note. It is possible, and probable, that some words will appear in both lists. It is also possible that a word may appear
low in boths lists but when merged becomes one of the top words.

To obtain the data necessary for the reports as requested in the project requirements, the interesting words will be
joined with the original corpus to obtain full word counts. Because of this, it is probable that many neutral sentences
will be included in the final report.

    Typical usage:

    $ python InterestingWords.py

Note. The input data for this script is located int the ./output folder.
"""
import pandas

from modules import utilities
from modules import nlp

def main():

    corpus = pandas.read_csv(utilities.corpus_pos(), index_col = 'id')   # read the POS tagged sentences
    words = corpus[corpus.label != 'neutral']                            # filter out the neutral sentences
    words = ( words.drop(['sentence'], axis = 1)                         # drop columns not needed for this part of the analysis
                    .drop(['file_name'], axis = 1)
                    .drop(['location'], axis = 1)
                    .drop(['negative'], axis = 1)
                    .drop(['positive'], axis = 1)
                    .drop(['neutral'], axis = 1) )

    words['parts_of_speech'] = words.apply(lambda row: nlp.filter_descriptive_words(row['parts_of_speech']), axis = 1)
    words = words[words.parts_of_speech != '[]']                       # remove sentences without adjectives nor adverbs

    positive_words = utilities.word_frequency(words, 'pos')
    negative_words = utilities.word_frequency(words, 'neg')
    all_words      = utilities.word_frequency(corpus)

    interesting_words = ( pandas.concat([positive_words, negative_words])
                            .groupby('word')
                            .agg( count = pandas.NamedAgg(column = 'count', aggfunc = sum) )
                            .sort_values(by = ['count'], ascending = False) )

    positive_words.to_csv(utilities.positive_words())
    negative_words.to_csv(utilities.negative_words())
    all_words.to_csv(utilities.all_words())
    interesting_words.to_csv(utilities.interesting_words())

if __name__ == '__main__':
    main()