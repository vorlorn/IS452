This project can collect tweets in one hashtag, and analysis the emotion of the text.

This sentiment analysis is based on Sentiment Analysis Dataset download from here(http://thinknook.com/twitter-sentiment-analysis-training-corpus-dataset-2012-09-22/) and NTLK(http://ntlk.org).



This project contains four .py files. You can run them by order, or just run one of these files.

1. collectdata.py : it can collect tweets based on tweepy and save thems into a json file. As long as this program is running, it will scrapy all new tweets from Twitter in one hashtag. To use this program, you can change the API here.
   There are tweets I collected in #MajorCrimes, a TV serious that came to 100 episode in 6e9p, 20 December, 2017. To collect this dataset, I run this program from 19:33:00(UTC) to 22:22:00(UTC) and the show was on air from 20:00(UTC) to 21:00(UTC).

2. textprocess.py : it process the data from Sentiment Analysis Dataset. After running this file, the dataset will be sepreate into pos.txt and neg.txt according to the marked sentiment, and remove all irrelevant word such as hashtags and digits and stopwords, URLs, punctuations, etc.

3. buildClassifier.py: it can use pos.txt and neg.txt datasets to creat a naive bayes classifier based on NTLK(http://nltk.org). It will save the classifier into myClassifier.pickle.

4. classify.py: it can classify tweets collected by collectdata.py using classifier build in buildClassifier.py. The result will be saved in result.csv, with the time and text and sentiment index. 0 for negative emotion and 1 for positice emotion.



The project uses these datasets:

1. MajorCrimes.json: Tweets collected by collectdata.py.

2. pos.txt: positive tweets extract from Sentiment Analysis Dataset.

3. neg.txt: negative tweets extract from Sentiment Analysis Dataset.

4. stopwords.txt: words that irrelevant to sentiment analysis. This file can be changed.

5. Sentiment Analysis Dataset.csv: download from http://thinknook.com/twitter-sentiment-analysis-training-corpus-dataset-2012-09-22/
   The dataset is based on data from the following two sources:
     University of Michigan Sentiment Analysis competition on Kaggle
     Twitter Sentiment Corpus by Niek Sanders
   It contains 1,578,627 classified tweets, each row is marked as 1 for positive sentiment and 0 for negative sentiment.

(Note: This dataset is too large for GitHub. To use it in textprocess.py, you should include this dataset into dataset/.)
