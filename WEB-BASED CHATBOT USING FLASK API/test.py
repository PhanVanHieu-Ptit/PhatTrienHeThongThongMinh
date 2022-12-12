from dataProcess import data_process
from keras.models import load_model




model = load_model('model.h5')
print(model)



validate_x,validate_y = data_process('trainning.json')
test_x, test_y = data_process('test.json')

# print('=============================VALIDATION==========================================')
# scores = model.evaluate(validate_x, validate_y)
# print("Loss:", (scores[0]))
# print("Accuracy:", (scores[1]*100))

print('=============================TEST==========================================')
scores = model.evaluate(test_x, test_y)
print("Loss:", (scores[0]))
print("Accuracy:", (scores[1]*100))
