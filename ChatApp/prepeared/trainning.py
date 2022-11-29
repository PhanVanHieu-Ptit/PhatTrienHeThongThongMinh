import random
import json
import pickle
import numpy as np

import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer

import tensorflow as tf;
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Activation, Dropout
# from tensorflow.keras.optimizers import SGD


lematizer = WordNetLemmatizer()

intents = json.loads(open('nhuCau.json',encoding="utf8").read())

words =[]
classes =[]
documents = []
ignore_letters = ['?','!','.',',']

for intent in intents['intents']:
    for pattern in intent["patterns"]:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list,intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lematizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))

classes = sorted(set(classes))

pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))

training = []
output_empty = [0] * len(classes)

for documents in documents:
    bag = []
    word_patterns = documents[0]
    word_patterns = [lematizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(documents[1])] = 1
    training.append([bag,output_row])

random.shuffle(training)
training = np.array(training)

training_x = list(training[:,0])
training_y = list(training[:,1])

model = tf.keras.models.Sequential()
# model = tf.keras.Sequential()
# model.add(tf.keras.Input(shape=len(training_x[0])))
model.add(tf.keras.layers.Dense(128,input_shape=(len(training_x[0]),), activation='relu'))
# model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(len(training_y[0]), activation='softmax'))

sgd = tf.keras.optimizers.SGD(learning_rate=0.01, weight_decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd,metrics=['accuracy'])

hist = model.fit(np.array(training_x), np.array(training_y),epochs=200, batch_size=5, verbose=1)

model.save('chatbotmodel.h5',hist)
# model.save('chatbot_model.model')
print('done')
