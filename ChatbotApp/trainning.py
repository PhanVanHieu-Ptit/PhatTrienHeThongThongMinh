from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
from ChatbotApp.dataProcess import data_process
import os

rootPath = 'E:\\DoAnPhatTrienHeThongThongMinh\\ChatbotApp'
type = 'true'# true or wrong

train_x,train_y = data_process(rootPath,os.path.abspath('data/'+type+'/trainning/trainning.json'),type)
# train_x,train_y = data_process(rootPath,'\\data\\wrong\\trainning\\trainning.json')
# Create model - 3 layers. First layer 128 neurons, second layer 64 neurons and 3rd output layer contains number of neurons
# equal to number of intents to predict output intent with softmax
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])


# fitting and saving the model
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save(rootPath+'\\model\\'+type+'\\model.h5', hist)
# model.save(rootPath+'\\model\\wrong\\model.h5', hist)

# hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=3, verbose=1)
# model.save('model1.h5', hist)
#
# hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=10, verbose=1)
# model.save('model2.h5', hist)

print("model created")

