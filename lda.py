import json
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
p_stemmer = PorterStemmer()
import gensim
from gensim import corpora, models


# create English stop words list
en_stop = get_stop_words('en')


tokenizer = RegexpTokenizer(r'\w+')



fname = 'superbowl.json'
texts = []
with open(fname, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        text = tweet['text']
        raw = text.lower()
        tokens = tokenizer.tokenize(raw)
        stopped_tokens = [i for i in tokens if not i in en_stop]
        # Create p_stemmer of class PorterStemmer
        p_stemmer = PorterStemmer()
        # stem token
        texts.append([p_stemmer.stem(i) for i in stopped_tokens])


dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts][:100]
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary, passes=20)
print(ldamodel.print_topics(num_topics=3, num_words=3))