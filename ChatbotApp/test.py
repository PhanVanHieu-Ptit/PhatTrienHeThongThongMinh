from keras.models import load_model
import os
# rootPath = 'E:\\DoAnPhatTrienHeThongThongMinh\\ChatbotApp'
type = 'wrong'# true or wrong
# load model
# model = load_model(rootPath+'\\model\\true\\model.h5')#true

model = load_model(os.path.abspath('model/'+type+'/model.h5'))

#path validation
# validationPath = rootPath+'\\data\\true\\validation\\validation.json'#true
validationPath =os.path.abspath('data/'+type+'/validation/validation.json')
#path test
testPath = os.path.abspath('data/true/testting/test.json') #true



# validate_x,validate_y = data_process('validation.json')
# test_x, test_y = data_process('test.json')

# print('=============================VALIDATION==========================================')
# scores = model.evaluate(validate_x, validate_y)
# print("Loss:", (scores[0]))
# print("Accuracy:", (scores[1]*100))

# print('=============================TEST==========================================')
# scores = model.evaluate(test_x, test_y)
# print("Loss:", (scores[0]))
# print("Accuracy:", (scores[1]*100))
import json
# from ChatbotApp.app3 import  predict_class,getResponse
import numpy as np
import nltk
import random
import pickle
nltk.download('popular')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# intents = json.loads(open('data.json').read())
intents = json.loads(open(os.path.abspath('data/'+type+'/trainning/trainning.json'), encoding="utf8").read())
words = pickle.load(open(os.path.abspath('model/'+type+'/texts.pkl'), 'rb'))
classes = pickle.load(open(os.path.abspath('model/'+type+'/labels.pkl'), 'rb'))

def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']

    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

tp = 0# nguoi&may khen
tn = 0#nguoi&may che
fn = 0#nguoi che <> may khen
fp = 0#nguoi khen <> may che

#test with data true
intents = json.loads(open(testPath, encoding="utf8").read())
# print(intents['intents'])


for intent in intents['intents']:
    samples = intent['patterns']
    tag_list = intent['tag']
    print('\n\n=====================================' + tag_list + '=========================================\n\n')
    for sample in samples:
        ints = predict_class(sample, model)
        tag = ints[0]['intent']

        percent = ints[0]['probability']
        res = getResponse(ints, intents)

        if tag_list == tag:
            tp += 1
        else:
            fp += 1
        print('tp: ' + str(tp) + '\nfp: ' + str(fp))
        print('\nsample: ' + sample + '\ntag: ' + tag + '\nPercent: ' + percent + '\nres: ' + res)



#test with data wrong
testPath =  os.path.abspath('data/wrong/testting/test.json')  # wrong
intents = json.loads(open(testPath, encoding="utf8").read())
for intent in intents['intents']:
    samples = intent['patterns']
    tag_list = intent['tag']
    print('\n\n=====================================' + tag_list + '=========================================\n\n')
    for sample in samples:
        ints = predict_class(sample, model)
        tag = ints[0]['intent']

        percent = ints[0]['probability']
        res = getResponse(ints, intents)
        if tag_list == tag:
            tn += 1
        else:
            fn += 1

        print('tn: ' + str(tn) + '\nfn: ' + str(fn))
        print('\nsample: ' + sample + '\ntag: ' + tag+'\nPercent: '+ percent + '\nres: ' + res)

print('\ntp:'+str(tp))
print('\ntn:'+str(tn))
print('\nfp:'+str(fp))
print('\nfn:'+str(tn))
#do dung
A = (tp+tn)/(tp+fp+tn+fn)
#do chinh xac
P = tp/(tp+fp)
#do truy hoi
R = tp/(tp+fn)
#do trung binh dieu hoa
F = (2*(P*R))/(P+R)

print('\nA: '+str(A)+"\nP: "+str(P)+"\nR: "+str(R)+"\nF: "+str(F))


# Importing packages
import matplotlib.pyplot as plt


# creating the dataset
data = {'Độ đúng': A, 'Độ chính xác': P, 'Độ truy hồi': R,
        'Độ trung bình điều hòa': F}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plotZ
plt.bar(courses, values, color='maroon',
        width=0.4)
plt.title("Biểu đồ độ chính xác khi test bộ dữ liệu")

fig1 = plt.figure()
ax = fig1.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['TP', 'TN', 'FP', 'FN']
dataOut = [tp,tn,fp,fn]
ax.pie(dataOut, labels = langs,autopct='%1.2f%%')
plt.show()


