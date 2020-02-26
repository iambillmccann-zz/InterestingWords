""" This script contains various helper functions.

The functions in this script help keep the main scripts concise and readable.

    Typical usage:

    from modules import utilies
"""
import pandas
import json

from os import listdir
from os.path import isfile, join

# File location constants
CORPUS_METADATA_FILE_NAME = './output/corpus_metadata.csv'
CORPUS_WITH_SENTIMENT = './output/corpus_sentiment.csv'
CORPUS_POS = './output/corpus_pos.csv'
NEGATIVE_WORDS = './output/negative_words.csv'
POSITIVE_WORDS = './output/positive_words.csv'
ALL_WORDS = './output/all_words.csv'
INTERESTING_WORDS = './output/interesting_words.csv'
FINAL_REPORT = './output/final_report.csv'

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
    return ( pandas.DataFrame(data = { 'sentence': sentences })
                .assign(file_name = file_name, 
                        location = lambda x: x.index) )

def word_frequency(df_words, type = 'all'):
    """ Return a list of words of a given type

    This function works using brute force methods; i.e. looping through
    the dataframe and then through the words from each sentence. I can
    get away with this method because the amount of data is very small.

    Args:
        df_words:   the dataframe from the corpus. The label and parts_of_speech
                    columns must be present.
        type:       "pos" for positive, "neg" for negative, or "all"

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

def str_of_file_name(files):
    """ Construct a string of file names

    Using a pandas series that contains file names that a word shows up in, transform it into
    a string that can be displayed on a report. This uses a brute force method of de-duping
    the list.

    Args:
        files:  A pandas series containing file names.

    Returns:
        A string of file names delimited by a space
    """
    file_name_str = ''
    previous = ''
    for index, value in files.items():
        if value != previous:
            file_name_str += value.split('.')[0] + ' '
        previous = value
    return file_name_str

def str_of_sentences(sentences):
    """ Construct a string of sentences

    Using a pandas series that contains sentences containing a word, transform it into a string
    that can be displayed on a report.

    Args:
        sentences: A pandas series containing sentences.

    Returns:
        A string of sentences delimited by \n\n (two new lines)
    """
    sentence_str = ''
    for index, value in sentences.items():
        sentence_str += value + '\n\n'
    return sentence_str

def map_words(corpus_pos):
    """ This function returns a mapping between a word and the sentences it appears in

    This uses a brute for method (for loops) to transpose the word/POS pairs into a
    mapping.

    Args:
        The full corpus including POS tagged words

    Returns:
        A dataframe of two columns; the word and a list of ids of the sentence
    """
    words = []
    for index, row in corpus_pos.iterrows():
        word_list = json.loads(row['parts_of_speech'])
        for word in word_list:
            the_word = "not" if word[0] == "n't" else word[0]
            words.append([the_word, row['file_name'], row['sentence']])

    df = pandas.DataFrame(words, columns = ['word', 'file_name', 'sentence'])           # make a dataframe with a word on each row
    df_counts = pandas.DataFrame.from_dict( df.groupby('word')['sentence'].count() )    # count words
    df_files = df.groupby('word').agg( files = ('file_name', str_of_file_name))         # list of containing files
    df_sentences = df.groupby('word').agg( sentences = ('sentence', str_of_sentences) ) # list of containing sentences

    return df_counts.join(df_files).join(df_sentences).rename(columns = {"sentence" : "count"})

def rowIndex(row):
    return row.name