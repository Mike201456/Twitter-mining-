# define preprocess 

import re
from nltk.stem.porter import PorterStemmer
p_stemmer = PorterStemmer()
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [p_stemmer.stem(token) if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
    
# define stop words

# define stop words
import operator 
import json 
from collections import Counter
from nltk.corpus import stopwords
import string 
from nltk import ngrams
import sentiment_mod as s
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import style
import time

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'RT', 'via', 
                                                   '🎉', '…','🚕','🚙','👇','🏻'] 
        
#[ json.loads(l).get('text') for l in tweetfile]

# show most_common words 
fname = 'uber.json'
dates_uber = []
with open(fname, 'r') as f:
 
    count_all = Counter()
    count_all_2 = Counter()
    count_all_3 = Counter()
    val = []
    for line in f:
        try:
            tweet = json.loads(line)
            #text = tweet['text']
            #print(text)
            
            #sentiment_value, confidence = s.sentiment(text)
            #if confidence*100 >= 80:
                #val.append(sentiment_value)
                
                
            #tweet = json.loads(line).get('text')
            # create a list with all the terms 
            terms_all = [term.lower() for term in preprocess(tweet['text'])
                        if term not in stop 
                        and not term.startswith(('#', '@','https','RT'))]
            dates_uber.append(tweet['created_at'])
            terms_ngram_2 = ngrams(terms_all, 2)
            terms_ngram_3 = ngrams(terms_all, 3)
            # update the counter 
            count_all.update(terms_all)
            count_all_2.update(terms_ngram_2)
            count_all_3.update(terms_ngram_3)
            counter
        except:
            continue
print(len(dates_uber))

# a list of "1" to count the hashtags
ones = [1]*len(dates_uber)
# the index of the series
idx = pd.DatetimeIndex(dates_uber)
# the actual series (at series of 1s for the moment)
uber_timestamp = pd.Series(ones, index=idx)
 
# Resampling / bucketing
per_minute = uber_timestamp.resample('1Min', how='sum').fillna(0)


#ax = plt.subplot(111)
#ax.bar(uber_timestamp, per_minute, width=10)
#ax.xaxis_date()
#time_chart = vincent.Line(uber_timestamp)
#time_chart.axis_titles(x='Time', y='Freq')
#time_chart.to_json('time_chart.json')

#print(type(per_minute))


f = open('uber.txt', 'r')
text01 = f.read().split('\n')

p = n = 0
for i in text01:
    if i == 'pos':
        p += 1
    if i == 'neg':
        n += 1
ratio = p/n
#print(ratio)
# print the first 5 most frequent words
print(count_all.most_common(10))
print(count_all_2.most_common(10))
print(count_all_3.most_common(10))
print(ratio)


#per_minute.plot.bar()
#plt.show()


#.clear()
#ax1.plot(per_minute)
#ani = animation.FuncAnimation(fig, animate, interval=100)
#plt.show()
#plt.close(fig)