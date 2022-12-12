from dataProcess import data_process
from keras.models import load_model




model = load_model('model.h5')
print(model)



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
intents = json.loads(open('test.json', encoding="utf8").read())
from app import  predict_class,getResponse
# print(intents['intents'])
tp = 0# nguoi&may khen
tn = 0#nguoi&may che
fn = 0#nguoi che <> may khen
fp = 0#nguoi khen <> may che
for intent in intents['intents']:
    samples = intent['patterns']
    tag_list = intent['tag']

    for sample in samples:
        ints = predict_class(sample, model)
        tag = ints[0]['intent']
        res = getResponse(ints, intents)
        if tag_list == tag:
            tp += 1
        else:
            fp += 1

        print('tp: ' + str(tp) + '\nfp: ' + str(fp))
        print('\nlist_di_hoc[0]: ' + sample + '\ntag: ' + tag + '\nres: ' + res)

#do dung
A = (tp+tn)/(tp+fp+tn+fn)
#do chinh xac
P = tp/(tp+fp)
#do truy hoi
R = tp/(tp+fn)
#do trung binh dieu hoa
F = (2*(P*R))/(P+R)

print('\nA: '+str(A)+"\nP: "+str(P)+"\nR: "+str(R)+"\nF: "+str(F))



