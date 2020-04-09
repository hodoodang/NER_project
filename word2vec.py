import gensim

ko_model = gensim.models.Word2Vec.load('./model/word2vec/ko.bin')

sample = ko_model.wv.get_vector('강아지')
print(len(sample))

vectors = ko_model['강아지']
print(vectors.shape)