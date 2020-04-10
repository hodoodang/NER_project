from gensim.models import Word2Vec
from gensim.models import KeyedVectors

'''
size = 워드 벡터의 특징 값. 즉, 임베딩 된 벡터의 차원.
window = 컨텍스트 윈도우 크기
min_count = 단어 최소 빈도 수 제한 (빈도가 적은 단어들은 학습하지 않는다.)
workers = 학습을 위한 프로세스 수
sg = 0은 CBOW, 1은 Skip-gram.

'''
# 모델 만들기, 저장
def make_w2v_model(sentences, size=100, window=5, min_count=5, workers=4, sg=1):

  word_model = Word2Vec(sentences, size=100, window=5, min_count=5, workers=4, sg=1)
  word_model.wv.save_word2vec_format('word_w2v') 

  print('model save success!')


# 모델 로드
def load_w2v(model_path):
  # model_name = 'word_w2v'
  loaded_model = KeyedVectors.load_word2vec_format(model_path)
  
  return loaded_model

# 출력 예시 코드
# loaded_model = load_w2v('/content/drive/My Drive/와이즈넛/NER_project/word_w2v')
# loaded_model.wv.get_vector('가장')
