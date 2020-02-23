""" This script add the sentiment score to each sentence in the corpus.

This file reads a csv/dataframe created by a previous step in the data pipeline.
Each sentence is marked with three scores ... positive, neutral, and negative. The
scores are real numbers between 0 and 1. These numbers are probabilities. As this is
a programming exercise, and not a data science exercise, I am using a "cheat" and
calling an API that is a sentiment model based on NLTK.

    Typical usage:

    $ python DetermineSentiment.py

Note: Input and output files are presumed to be in the /output folder.
"""
import json
import csv

from modules import utilities
from modules import restclient

def main():

    with open(utilities.corpus_metadata_file_name()) as corpus_file:
        reader = csv.DictReader(corpus_file)

        with open(utilities.corpus_with_sentiment(), mode = 'w') as sentiment_file:
            columns = ['id', 'sentence', 'file_name', 'location', 'label', 'negative', 'positive', 'neutral']
            writer = csv.DictWriter(sentiment_file, fieldnames = columns)
            writer.writeheader()

            for data in reader:

                try:
                    result = restclient.get_sentiment_scores(data['sentence'])
                except Exception as api_error:
                    print(api_error)
                    exit()

                data['label'] = result['label']
                data['negative'] = result['probability']['neg']
                data['positive'] = result['probability']['pos']
                data['neutral'] = result['probability']['neutral']

                writer.writerow(data)
                if int(data['id']) + 1 % 50 == 0:
                    print('Computed sentiment on {} sentences.'.format(data['id']))

if __name__ == '__main__':
    main()