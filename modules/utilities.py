from os import listdir
from os.path import isfile, join

def get_file_names(the_path):
    return [f for f in listdir(the_path) if isfile(join(the_path, f))]
