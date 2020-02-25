#! /bin/bash -x
echo Starting!

echo Activate the Python virtual environment
source ./venv/bin/activate

echo Parse the raw data into sentences
python ParseSentences.py

echo Mark each sentence with sentiment scores
python DetermineSentiment.py

echo Tag each word with parts of speech
python TagPartsOfSpeech.py

echo Make the list of intersting words
python InterestingWords.py

echo Build the table for the final report
python PrepareTable.py

echo Finished!