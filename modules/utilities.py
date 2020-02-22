""" This script contains various helper functions.

The functions in this script help keep the main scripts concise and readable.

    Typical usage:

    from modules import utilies
"""
import pandas

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

def corpus_metadata_file_name():
    """ Return the name of the file containing sentences from the corpus

    This is simply a file name constant that can be resused across modules

    Returns:
        The name of the file containing parsed sentences
    """
    return './output/corpos_metadata.csv'