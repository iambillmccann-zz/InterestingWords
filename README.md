# Interesting Words
### Coding Task

**Bill McCann** -
25 February 2020 -
bill.mccann@gmail.com

## Summary
This repository is the result of a coding task. The requirements of the task state that from a few documents which have lots of words and sentences produce a list of the most frequent interesting words, along with a summary table showing where those words appear. The key phrase here is "interesting words". There is no guidance regarding what makes a word interesting other than the challenge may be tackled in any way that best solves the problem.

What makes words interesting is their power to influence thoughts and emotions. Of course, things (nouns) and actions (verbs) can be powerful, but it is description that bring statements to life. For example, you can "strike with the hammer" or you can "firmly strike with the heavy iron hammer". This study determines the words used most frequently to evoke a positive or negative sentiment.
## Findings
The [final report](https://github.com/iambillmccann/InterestingWords/blob/master/docs/Final%20Report.xlsx) is provided in a spreadsheet. The list of the most powerful descriptive words from the entire corpus of documents are: Not, America, also, many, new, enough, together, last, even, great, right, long, better, still, hard, military, clear, best, political, next. From this list I make a couple of observations. First, the powerful words are common words. And second, some words (“not” for example) can be powerful both positively and negatively.
## Setup and Execute
Use the following steps to set up and run this code. **Note.** This code was developed on a Windows 10 laptop running Ubuntu Linux on the WSL (Windows Subsystem for Linux). The code editor was VS Code.

1. Clone this repository onto your device;
2. Create a Python virtual environment;

    Because I have both Python 2.7 and Python 3.6 on my device, I used the following command for this purpose:
    ```
    $ python3 -m venv venv
    ```
3. Install the project's dependencies. The exact command will vary depending on your environment, I used the following:

    ```
    $ pip install  --target ./venv/lib --requirement requirements.txt
    ```

4. If you are running on Linux, you can run the entire pipeline using the runall.sh bash script. I used the following:

    ```
    $ bash runall.sh
    ```
    **Note.** If are not running on Linux, you can run the pipeline one script at a time. Here are commands that will 
    accomplish this:

    ```
    $ source ./venv/bin/activate
    $ python ParseSentences.py
    $ python DetermineSentiment.py
    $ python TagPartOfSpeech.py
    $ python InterestingWords.py
    $ python PrepareTable.py
    ```

    **Note.** All the intermediate files are source managed on this repository. Therefore it is not necessary to run the entire pipeline unless you intend to analyze new documents. The pipeline can be rerun from any step, but the steps
    must be run in the proper order. Lastly, if you intend to analyze new documents, be sure the files are formatted as 
    plain ASCII text.
## Solution Architecture
The basic design strategy is described below.
### Approach
This project is architected as a batch data pipeline of five scripts. These scripts are the "micro-services" for the pipeline. The idea was to break the problem into small discrete pieces that could be tackled (or later replaced) simply. The pipeline is designed to run as a batch in a precise sequence. There is no inter-service communication, instead each script loads the necessary data from files created by the previous step.
The basic algorithm used is as follows:
-	Treat the corpa as a single combined corpus;
-	Break the corpus into individual sentences using default nltk tokenizers;
-	Use a third party API to mark each sentence as Positive, Neutral, or Negative;
-	Compute frequencies of words in Positive and Negative sentences;
-	Select the adjectives and adverbs;
-	Merge the lists into a combined list and select the top twenty;
-	Format the report.
### Structure of Code
The project is structured using best practice for Python solutions. The structure is as follows:
```
Root\
	Corpus\
		[document files]
	Docs\
		Back-end Coding Test.docx
		Final Report.xlsx
	Modules\
		__init__.py
		Nlp.py
		Restclient.py
		Utilities.py
	Output\
		[intermediate data files]
	Tests\
		[unit tests]
	Venv\
		[virtual environment]
	DetermineSentiment.py
	InterestingWords.py
	ParseSentences.py
	PrepareTable.py
	Setup.py
	TagPartsOfSpeech.py
	Runall.sh
	Requirements.txt
```
### Data Pipeline
The data pipeline is comprised of the following scripts. These script must be run in the proper sequence.
| Seq. | Script | Description |
| --- | --- | --- |
| 1 | ParseSentences.py | Read the document files and break them into individual sentences. |
| 2 | DetermineSentiment.py | Call an API to determine the sentiment of the sentence. |
| 3 | TagPartsOfSpeech.py | Using NLTK, tag each word to identify how it is used. |
| 4 | InterestingWords.py | Compute the most interesting words. |
| 5 | PrepareTable.py | Compile the results that are the final report. |
## Cheats
In the interest of time, and since this is a coding test and not a production system, I took some shortcuts. In particular, I’d like to call out two of these shortcuts.
-	*Using an API to determine sentiment scores* I did not train my own sentiment model. Instead I used an API that provided the scores. **Note** the API will throttle usage at 10,000 calls per day. The corpus provided for this test contained 937 sentences, each requiring an API call.
-	*Manual formatting of results* I had intended to use a Jupyter Notebook to format the final report. Given time constraints and the challenge of displaying sentences through a notebook, I chose Excel instead. The Excel workbook had to be formatted manually. That said, no data was manipulated within the workbook.
## Ideas for Improvement
This is a challenging an interesting project. I have completed the work desribed in the original problem definition. That said, there are several ways this work could be iterated on to make it even better. Some possible improvements are:
-	*Training sentiment ML* Build my own sentiment model instead of using the API. This could improve model performance as well as the speed of the system.
-	*Clean the data* Because I knew that I was selecting only adjectives and adverbs, I intentionally left bad data within the tagged POS. The solution, however, would be more flexible by paying more attention to cleaning the data. In particular, punctuation should not be treated as words, and more words can be added to the list of stop words.
-	*Use sentiment scores to weight words* The most interesting words is based on the frequency of occurrence in positive or negative sentences. The results could be more interesting by applying the predictive score as a weight to the sentences.
-	*Generate formatted output* The report could be created automatically instead of being copied into an Excel workbook.
-	*Better visualizations* The final report contains worksheets showing treemaps of Positive and Negative words. A word cloud would be a better visualization.
-	*Establish unit tests* The solution should have code coverage via unit tests; especially for the functions in the utilities module.
