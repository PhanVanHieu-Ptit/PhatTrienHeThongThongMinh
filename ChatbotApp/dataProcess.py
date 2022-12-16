import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
import json
import pickle

import numpy as np
import random

def data_process(rootPath,nameFile,type):
    words = []
    classes = []
    documents = []
    ignore_words = ['?', '!', '"', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', ',', '/', ':', ';', '<', '=', '>', '?',
                    '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~', '\t', '\n', "'",'_']


    data_file = open(nameFile, encoding="utf8").read()

    intents = json.loads(data_file)


    for intent in intents['intents']:
        for pattern in intent['patterns']:

            # tokenize each word
            w = nltk.word_tokenize(pattern)
            words.extend(w)
            # add documents in the corpus
            documents.append((w, intent['tag']))

            # add to our classes list
            if intent['tag'] not in classes:
                classes.append(intent['tag'])

    # lemmaztize and lower each word and remove duplicates
    words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
    words = sorted(list(set(words)))
    # sort classes
    classes = sorted(list(set(classes)))
    # documents = combination between patterns and intents
    print(len(documents), "documents")
    # classes = intents
    print(len(classes), "classes", classes)
    # words = all words, vocabulary
    print(len(words), "unique lemmatized words", words)

    pickle.dump(words, open(rootPath+'\\model\\'+type+'\\texts.pkl', 'wb'))
    pickle.dump(classes, open(rootPath+'\\model\\'+type+'\\labels.pkl', 'wb'))

    # pickle.dump(words, open(rootPath + '\\model\\wrong\\texts.pkl', 'wb'))
    # pickle.dump(classes, open(rootPath + '\\model\\wrong\\labels.pkl', 'wb'))

    # create our training data
    training = []
    # create an empty array for our output
    output_empty = [0] * len(classes)
    # training set, bag of words for each sentence
    for doc in documents:
        # initialize our bag of words
        bag = []
        # list of tokenized words for the pattern
        pattern_words = doc[0]
        # lemmatize each word - create base word, in attempt to represent related words
        pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
        # create our bag of words array with 1, if word match found in current pattern
        for w in words:
            bag.append(1) if w in pattern_words else bag.append(0)

        # output is a '0' for each tag and '1' for current tag (for each pattern)
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1

        training.append([bag, output_row])
    # shuffle our features and turn into np.array
    random.shuffle(training)
    training = np.array(training)
    # create train and test lists. X - patterns, Y - intents
    train_x = list(training[:, 0])
    train_y = list(training[:, 1])
    print("Training data created")
    return train_x,train_y
