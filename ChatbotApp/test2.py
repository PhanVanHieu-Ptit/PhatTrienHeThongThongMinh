# from ChatbotApp.dataProcess import data_process
# rootPath = 'D:\\Reactjs\\HTTT\\Chat-Box-Deep-Learning-\\ChatbotApp'
# type = 'true'# true or wrong
# import os
# train_x,train_y = data_process(rootPath,os.path.abspath('data/'+type+'/trainning/trainning.json'),type)
import re
from static.emo_unicode import UNICODE_EMOJI
emoji_pattern = re.compile('|'.join(UNICODE_EMOJI), flags=re.UNICODE)
emoji_example = " Without you by my side, 💓 😉 I am not complete. You have given me the best of love, 🎈 and I want to be by your side forever. Thank you for giving my life that direction it needed. 💋‍ Thank you for loving me unconditional. 💏"
print(emoji_pattern.sub(r'', emoji_example))
