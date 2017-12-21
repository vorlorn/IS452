import nltk
import pickle

def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})

pos = []
with open("pos.txt",'r',encoding='utf=8') as f:
    print("Loading pos...")
    for i in f:
        pos.append([format_sentence(i), 1])
    print("Done!")

neg = []
with open("neg.txt",'r',encoding='utf=8') as f:
    print("Loading neg...")
    for i in f:
        neg.append([format_sentence(i), 0])
    print("Done!")


# split labeled data into the training and test data
training = pos[:int((.8)*len(pos))] + neg[:int((.8)*len(neg))]
test = pos[int((.8)*len(pos)):] + neg[int((.8)*len(neg)):]

# use naive bayes classifier to classify sentiment
from nltk.classify import NaiveBayesClassifier
print("Loading classifier...")
classifier = NaiveBayesClassifier.train(training)

from nltk.classify.util import accuracy
print("Accuracy:",accuracy(classifier, test)) # Accuracy of this classifier

print("Saving classifier...")
f = open('myClassifier.pickle','wb')
pickle.dump(classifier,f)
print("Done!")
f.close()
