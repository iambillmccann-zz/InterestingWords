#! /bin/bash -x
echo Starting!

source ./venv/bin/activate
python ParseSentences.py
python DetermineSentiment.py
python TagPartsOfSpeech.py
python InterestingWords.py
python PrepareTable.py

echo Finished!