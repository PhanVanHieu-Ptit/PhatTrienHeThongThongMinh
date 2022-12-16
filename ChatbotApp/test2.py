import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
from ChatbotApp.dataProcess import data_process
import os

rootPath = 'D:\\Reactjs\\HTTT\\Chat-Box-Deep-Learning-\\ChatbotApp'
type = 'wrong'# true or wrong

train_x,train_y = data_process(rootPath,os.path.abspath('data/'+type+'/trainning/trainning.json'),type)
print(train_x)
print(train_y)