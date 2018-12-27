# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:00:37 2018

@author: Harika
"""


from nltk import word_tokenize, sent_tokenize
import urllib.request
from bs4 import BeautifulSoup
def getTextFromUrl(URL):
    with urllib.request.urlopen(URL) as response:
        html = response.read()
        soup = BeautifulSoup(html,"lxml")
        text = ' '.join(map(lambda p: p.text, soup.find_all('article')))
        text1 = text.encode('ascii',errors='replace').decode().replace("?", "")
        return text1

from nltk.corpus import stopwords
from string import punctuation
customStopWords = set(stopwords.words('English')+list(punctuation));
from heapq import nlargest
from collections import defaultdict
def getTopStatements(n):
    textt  = getTextFromUrl('https://www.washingtonpost.com/lifestyle/style/its-a-boy-its-a-girl-for-some-parents-learning-their-babys-sex-is-a-disappointment/2018/12/12/8aef32c0-f8be-11e8-8d64-4e79db33382f_story.html?utm_term=.fee86c811c2f')
    sentx = sent_tokenize(textt)
    wordx = word_tokenize(textt.lower())    
    wordxwo = [word for word in wordx if word not in customStopWords]
    from nltk.probability import FreqDist
    freq = FreqDist(wordxwo)
    ranking = defaultdict(int)
    for x,sent in enumerate(sentx):
        for w in word_tokenize(sent.lower()):
            if w in freq:
                ranking[x]+=freq[w]         
    sents_top = nlargest(n, ranking, ranking.get)
    summary =""
    for x in sents_top:
        summary+=("\n"+sentx[x]+"\n")
    return summary
  

print(getTopStatements(3))