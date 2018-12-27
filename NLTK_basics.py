# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:09:51 2018

@author: Harika
"""


import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')
text = "course on 'nltk', in pluralsight which Was started by me today."

#TOKENIZING A TEXT
from nltk import word_tokenize, sent_tokenize
words = word_tokenize(text)
sents = sent_tokenize(text)
print(words)

#REMOVAL OF STOP WORDS
from nltk.corpus import stopwords
from string import punctuation
customStopWords = set(stopwords.words('English')+list(punctuation));
sentWOStopwords = [word for word in words if word not in customStopWords]

#IDENTIFYING BIGRAMS
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(sentWOStopwords)
sorted(finder.ngram_fd.items())

trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder_1 = TrigramCollocationFinder.from_words(sentWOStopwords)
sorted(finder_1.ngram_fd.items())

#STEMMING
tex2 = "Mary closed on proceed closing night when she was in the mood to close."
from nltk.stem.lancaster import LancasterStemmer
words_2 = word_tokenize(tex2)
st = LancasterStemmer()
stemmedWords = [st.stem(word) for word in words_2]
print(stemmedWords)

#TAGGING TO PartsOfSpeech
nltk.pos_tag(words_2)

from nltk.corpus import wordnet as wn
for ss in wn.synsets('high'):
    print(ss,ss.definition())
from nltk.wsd import lesk
sense1=lesk(word_tokenize("Reach higher altitudes"),'high')
print(sense1,sense1.definition())
sense2 = lesk(word_tokenize("Don't become high after a drink"),'high')
print(sense2,sense2.definition())
