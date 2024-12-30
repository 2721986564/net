# @Time    : 2021/03/14 22:44
# @Author  : SY.M
# @FileName: build_glove_embeddind_dict.py

import pickle

path = "C:/Users/Lenovo/Desktop/神经网路课设/glove.42B.300d.txt"

glove_embedding = {}
with open(path, 'r', encoding='utf-8') as f:
    while True:
        embedding = []
        line = f.readline()
        if line == '':
            break
        word, embedding_str = line.split(' ')[0], line.split(' ')[1:]
        for i in embedding_str:
            embedding.append(eval(i))
        glove_embedding[word] = embedding

    with open('C:/Users/Lenovo/Desktop/神经网路课设/RNN_on_sentiment-analysis-on-movie-reviews-main/RNN_on_sentiment-analysis-on-movie-reviews/utils/build_glove_embeddind_dict'
              '.pkl', 'wb') as f1:
        pickle.dump(glove_embedding, f1, pickle.HIGHEST_PROTOCOL)
