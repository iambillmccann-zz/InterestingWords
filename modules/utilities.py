""" This script contains various helper functions.

The functions in this script help keep the main scripts concise and readable.

    Typical usage:

    from modules import utilies
"""
import pandas
import json

from os import listdir
from os.path import isfile, join

def get_file_names(the_path):
    """ Retrieve a list of file names for a folder

    Use the listdir function to retrieve the objects in the folder,
    then iterate over each using isfile to determine if the object
    is a file or folder. Only files are returned.

    Args:
        the_path: the name of the folder to search

    Returns:
        a list containing the names of the files
    """
    return [f for f in listdir(the_path) if isfile(join(the_path, f))]

def get_content(the_path, the_file):
    """ Retrieve the content of a file into a single string variable

    Use the simple read() method to retrieve the contents of a file.
    Note: This only works for small text files.

    Args:
        the_path: the folder containing the file
        the_file: the name of the file

    Returns:
        the content of the file
    """
    full_path = '{}/{}'.format(the_path, the_file)
    file_handle = open(full_path, "r")
    content = file_handle.read()
    file_handle.close()

    return content

def make_dataframe(sentences, file_name):
    """ Transform the list of sentences into a dataframe

    Make a dataframe that adds some metadata to the list of
    sentences. Each row will contain one sentence, the name of the
    source file and a zero based index of the sentence.

    Args:
        sentences: a list of sentences from a document
        file_name: the name of the document containing the sentences

    Returns:
        A dataframe of the sentences and meta data.
    """
    return (pandas.DataFrame(data = { 'sentence': sentences })
                  .assign(file_name = file_name, 
                          location = lambda x: x.index))

def word_frequency(df_words, type = 'all'):
    """ Return a list of words of a given type

    This function works using brute force methods; i.e. looping through
    the dataframe and then through the words from each sentence. I can
    get away with this method because the amount of data is very small.

    Args:
        df_words: the dataframe from the corpus. The label and parts_of_speech
                  columns must be present.
        type:     "pos" for positive, "neg" for negative, or "all"

    Returns:
        a list of words of the given type
    """
    df = df_words if type == 'all' else df_words[df_words.label == type]
    words = []
    for index, row in df.iterrows():                                 # iterate over all sentences
        word_list = json.loads(row['parts_of_speech'])
        for word in word_list:                                       # iterate over the words in the sentence
            the_word = "not" if word[0] == "n't" else word[0]
            words.append(the_word)                                   # add the word to the full list

    df = pandas.DataFrame(words, columns = ['word'])
    freq_dict = ( df.assign(count = 1)
                    .groupby('word')['count'].count() )
    df = pandas.DataFrame.from_dict(freq_dict).sort_values(by = ['count'], ascending = False)
    return df

def rowIndex(row):
    return row.name

def corpus_metadata_file_name():
    return './output/corpus_metadata.csv'

def corpus_with_sentiment():
    return './output/corpus_sentiment.csv'

def corpus_pos():
    return './output/corpus_pos.csv'

def negative_words():
    return './output/negative_words.csv'

def positive_words():
    return './output/positive_words.csv'

def all_words():
    return './output/all_words.csv'

def interesting_words():
    return './output/interesting_words.csv'