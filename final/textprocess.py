import string
import csv

#load stopwords into a list
stopwords = []
with open('dataset/stopwords.txt','r',encoding='utf-8') as words:
    for i in words:
        stopwords.append(i.strip())

import re

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    # r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    # r'(?:[\w_]+)', # other words
    # r'(?:\S)' # anything else
    '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+' # Punctuation
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def removestopwords(stopwords, data):
    # remove stopwords, digits, punctuations, hashtags, emotion icons from tweets
    # return a string
    cat = []
    for word in data.split():
        if word.lower() not in stopwords:
            cat.append(''.join(word.lower()))

    lists = [word for word in cat if not tokens_re.search(word)]
    return ' '.join(lists)
# print(removestopwords(stopwords,"quotseptem!  Iber ! until i I i diequot released hardbeat records includes real booty babes remix musicmonday @me :) https://example.com"))

pos = open('dataset/pos.txt','w')
neg = open('dataset/neg.txt','w')
print("Loading dataset...")
with open('Sentiment Analysis Dataset.csv', 'r',encoding='utf-8') as csvfile:
    print("Done!")
    spamreader = csv.reader(csvfile)
    print("Processing text...")
    for row in spamreader:
        if row[1] == '1':
            pos.write(removestopwords(stopwords,row[3]) + '\n')
        elif row[1] == '0':
            neg.write(removestopwords(stopwords,row[3]) + '\n')
    print("Done!")

pos.close()
neg.close()


