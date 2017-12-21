import json
import nltk
import pickle
import csv
import time
import datetime

# Load classifer
f = open('myClassifier.pickle','rb')
print("Loading Classifier...")
classifier = pickle.load(f)
print("Done!")
print(classifier.show_most_informative_features())
def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})


file = open('dataset/MajorCrimes.json','r',encoding='utf-8')
data = open('result.csv','w')

csvwriter = csv.writer(data)

# write time, text and sentiment into result.csv
head = True
for line in file.readlines():
    tweet = json.loads(line)

    if head:
        csvwriter.writerow(['time','text','Sentiment'])
        head = False

    timeArray = time.strptime(tweet['created_at'],"%a %b %d %H:%M:%S +0000 %Y")
    result = []
    result.append(datetime.datetime.fromtimestamp(time.mktime(timeArray)).strftime("%H:%M:%S"))
    result.append(tweet['text'])
    result.append(classifier.classify(format_sentence(tweet['text'])))
    csvwriter.writerow(result)


file.close()
data.close()
