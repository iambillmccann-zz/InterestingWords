from modules import utilities

DATA_FOLDER = "./corpus"

def main():

    the_files = utilities.get_file_names(DATA_FOLDER)
    print(DATA_FOLDER)

if __name__ == '__main__':
    main()