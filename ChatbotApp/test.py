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
from ChatbotApp.app3 import  predict_class,getResponse
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



