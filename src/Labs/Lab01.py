'''
Created on Oct 30, 2012

@author: Alex
'''
#amazon = tokens1, textA
#reuters = tokens2, textR
#wallstreet = tokens3, textW
#twitter = tokens4, textT
#medline = tokens5, textM
#text1 = Moby Dick
#text2 = Sense and Sensibility
#text3 = The Book of Genesis
#text4 = Inaugural Address Corpus
#text5 = Chat Corpus
#text6 = Monty Python and the Holy Grail
#text7 = Wall Street Journal
#text8 = Personals Corpus
#text9 = The Man Who Was Thursday
from __future__ import division
from nltk.book import *
import os, sys, nltk
sys.path.append(os.path.join("D:\\", "LanguageEngineering"))
import sussex_nltk
 

#Sense and Sensibility
print len(text2)
print len(set(text2))
print len(text2)/len(set(text2))
from nltk.corpus import stopwords
filtered_tokens_text2 = [w for w in text2 if w.isalpha() and w not in stopwords.words('english')]
print len(filtered_tokens_text2)
print len(set(filtered_tokens_text2))
print len(filtered_tokens_text2) / len(set(filtered_tokens_text2))
V = set(filtered_tokens_text2)
long_wordsSS = [w for w in V if len(w) > 15]
print sorted(long_wordsSS)
print len(long_wordsSS)
fdist_text2 = FreqDist(text2)
filtered_fdist_text2 = FreqDist(filtered_tokens_text2)
print fdist_text2
word_fdist2 = FreqDist([len(w) for w in text2])
filtered_word_fdist2 = FreqDist([len(w) for w in filtered_tokens_text2])
print word_fdist2
print word_fdist2.keys()
print word_fdist2.items()
print word_fdist2.max()
print word_fdist2.freq(word_fdist2.max())
print filtered_word_fdist2.max()
print filtered_word_fdist2.freq(word_fdist2.max())
vocabulary_text2 = fdist_text2.keys()
print vocabulary_text2[:10]
filtered_vocab_text2 = filtered_fdist_text2.keys()
print filtered_vocab_text2[:10]
print text2.collocations()
print text2.concordance("great")
print text2.similar("great")
 
import matplotlib.pyplot as pyplot
def zipf_dist(freqdist,num_of_ranks=50,show_values=True):
    x = range(1,num_of_ranks+1)
    y = freqdist.values()[:num_of_ranks]
    pyplot.bar(x,y,color="#1AADA4")
    pyplot.xlabel("SENSE AND SENSIBILITY: Rank of types ordered by frequency of occurrence")
    pyplot.ylabel("Frequency of occurrence")
    pyplot.grid(True)
    pyplot.xticks(range(1,num_of_ranks+1,2),range(1,num_of_ranks+1,2))
    pyplot.xlim([0,num_of_ranks+2])
    if show_values:
        for xi,yi in zip(x,y):
            pyplot.text(xi+0.25,yi+50,yi,verticalalignment="bottom",rotation=55,fontsize="small")
    pyplot.show()
    print "Plot complete."
   
print zipf_dist(fdist_text2)
print zipf_dist(filtered_fdist_text2)        


#chat corpus
print len(text5)
print len(set(text5))
print len(text5)/len(set(text5))
from nltk.corpus import stopwords
filtered_tokens_text5 = [w for w in text5 if w.isalpha() and w not in stopwords.words('english')]
print len(filtered_tokens_text5)
print len(set(filtered_tokens_text5))
print len(filtered_tokens_text5) / len(set(filtered_tokens_text5))
Q = set(filtered_tokens_text5)
long_wordsCC = [w for w in Q if len(w) > 15]
print sorted(long_wordsCC)
print len(long_wordsCC)
fdist_text5 = FreqDist(text5)
filtered_fdist_text5 = FreqDist(filtered_tokens_text5)
print fdist_text5
word_fdist5 = FreqDist([len(w) for w in text5])
filtered_word_fdist5 = FreqDist([len(w) for w in filtered_tokens_text5])
print word_fdist5
print word_fdist5.keys()
print word_fdist5.items()
print word_fdist5.max()
print word_fdist5.freq(word_fdist5.max())
print filtered_word_fdist5.max()
print filtered_word_fdist5.freq(filtered_word_fdist5.max())
vocabulary_text5 = fdist_text5.keys()
print vocabulary_text5[:10]
filtered_vocab_text5 = filtered_fdist_text5.keys()
print filtered_vocab_text5[:10]
print text5.collocations()
print text5.concordance("great")
print text5.similar("great")
 
import matplotlib.pyplot as pyplot
def zipf_dist(freqdist,num_of_ranks=50,show_values=True):
    x = range(1,num_of_ranks+1)
    y = freqdist.values()[:num_of_ranks]
    pyplot.bar(x,y,color="#1AADA4")
    pyplot.xlabel("CHAT CORPUS: Rank of types ordered by frequency of occurrence")
    pyplot.ylabel("Frequency of occurrence")
    pyplot.grid(True)
    pyplot.xticks(range(1,num_of_ranks+1,2),range(1,num_of_ranks+1,2))
    pyplot.xlim([0,num_of_ranks+2])
    if show_values:
        for xi,yi in zip(x,y):
            pyplot.text(xi+0.25,yi+50,yi,verticalalignment="bottom",rotation=55,fontsize="small")
    pyplot.show()
    print "Plot complete."
   
print zipf_dist(fdist_text5)   
print zipf_dist(filtered_fdist_text5) 


#AMAZON
from sussex_nltk.corpus_readers import AmazonReviewCorpusReader
arcr = AmazonReviewCorpusReader()
positive_reviews = arcr.positive()
negative_reviews = arcr.negative()
dvd_reviews = arcr.category("dvd")
positive_dvd_reviews = dvd_reviews.positive()
tokens1 = positive_dvd_reviews.sample_words(102152)
print len(tokens1)
print len(set(tokens1))
print len(tokens1) / len(set(tokens1))
from nltk.corpus import stopwords
filtered_tokens1 = [w for w in tokens1 if w.isalpha() and w not in stopwords.words('english')]
print len(filtered_tokens1)
print len(set(filtered_tokens1))
print len(filtered_tokens1) / len(set(filtered_tokens1))
X = set(filtered_tokens1)
long_wordsA = [w for w in X if len(w) > 15]
print sorted(long_wordsA)
print len(long_wordsA)
from nltk.text import Text
textA = Text(tokens1)
filtered_textA = Text(filtered_tokens1)
fdistA = FreqDist(textA)
filtered_fdistA = FreqDist(filtered_textA)
print fdistA
word_fdistA = FreqDist([len(w) for w in textA])
filtered_word_fdistA = FreqDist([len(w) for w in filtered_textA])
print word_fdistA
print word_fdistA.keys()
print word_fdistA.items()
print word_fdistA.max()
print word_fdistA.freq(word_fdistA.max())
print filtered_word_fdistA.max()
print filtered_word_fdistA.freq(filtered_word_fdistA.max())
vocabulary1 = fdistA.keys()
print vocabulary1[:10]
filtered_vocab1 = filtered_fdistA.keys()
print filtered_vocab1[:10]
print textA.collocations()
print textA.concordance("great")
print textA.similar("great")
 
 
import matplotlib.pyplot as pyplot
def zipf_dist(freqdist,num_of_ranks=50,show_values=True):
    x = range(1,num_of_ranks+1)
    y = freqdist.values()[:num_of_ranks]
    pyplot.bar(x,y,color="#1AADA4")
    pyplot.xlabel("AMAZON: Rank of types ordered by frequency of occurrence")
    pyplot.ylabel("Frequency of occurrence")
    pyplot.grid(True)
    pyplot.xticks(range(1,num_of_ranks+1,2),range(1,num_of_ranks+1,2))
    pyplot.xlim([0,num_of_ranks+2])
    if show_values:
        for xi,yi in zip(x,y):
            pyplot.text(xi+0.25,yi+50,yi,verticalalignment="bottom",rotation=55,fontsize="small")
    pyplot.show()
    print "Plot complete."
   
print zipf_dist(fdistA)         
print zipf_dist(filtered_fdistA) 


#REUTERS
from sussex_nltk.corpus_readers import ReutersCorpusReader
rcr = ReutersCorpusReader()
sport_cr = rcr.category("sport")
finance_cr = rcr.category("finance")
tokens2 = sport_cr.sample_words(102152)
print len(tokens2)
print len(set(tokens2))
print len(tokens2) / len(set(tokens2))
from nltk.corpus import stopwords
filtered_tokens2 = [w for w in tokens2 if w.isalpha() and w not in stopwords.words('english')]
print len(filtered_tokens2)
print len(set(filtered_tokens2))
print len(filtered_tokens2) / len(set(filtered_tokens2))
Y = set(filtered_tokens2)
long_wordsR = [w for w in Y if len(w) > 15]
print sorted(long_wordsR)
print len(long_wordsR)
from nltk.text import Text
textR = Text(tokens2)
filtered_textR = Text(filtered_tokens2)
fdistR = FreqDist(textR)
filtered_fdistR = FreqDist(filtered_textR)
print fdistR
word_fdistR = FreqDist([len(w) for w in textR])
filtered_word_fdistR = FreqDist([len(w) for w in filtered_textR])
print word_fdistR
print word_fdistR.keys()
print word_fdistR.items()
print word_fdistR.max()
print word_fdistR.freq(word_fdistR.max())
print filtered_word_fdistR.max()
print filtered_word_fdistR.freq(filtered_word_fdistR.max())
vocabulary2 = fdistR.keys()
print vocabulary2[:10]
filtered_vocab2 = filtered_fdistR.keys()
print filtered_vocab2[:10]
print textR.collocations()
print textR.concordance("great")
print textR.similar("great")
 
import matplotlib.pyplot as pyplot 
def zipf_dist(freqdist,num_of_ranks=50,show_values=True):
    x = range(1,num_of_ranks+1)
    y = freqdist.values()[:num_of_ranks]
    pyplot.bar(x,y,color="#1AADA4")
    pyplot.xlabel("REUTERS: Rank of types ordered by frequency of occurrence")
    pyplot.ylabel("Frequency of occurrence")
    pyplot.grid(True)
    pyplot.xticks(range(1,num_of_ranks+1,2),range(1,num_of_ranks+1,2))
    pyplot.xlim([0,num_of_ranks+2])
    if show_values:
        for xi,yi in zip(x,y):
            pyplot.text(xi+0.25,yi+50,yi,verticalalignment="bottom",rotation=55,fontsize="small")
    pyplot.show()
    print "Plot complete."
   
print zipf_dist(fdistR)
print zipf_dist(filtered_fdistR)


#WALLSTREET
from sussex_nltk.corpus_readers import WSJCorpusReader
wsjcr = WSJCorpusReader()
tokens3 = wsjcr.sample_words(102152)
print len(tokens3)
print len(set(tokens3))
print len(tokens3) / len(set(tokens3))
from nltk.corpus import stopwords
filtered_tokens3 = [w for w in tokens3 if w.isalpha() and w not in stopwords.words('english')]
print len(filtered_tokens3)
print len(set(filtered_tokens3))
print len(filtered_tokens3) / len(set(filtered_tokens3))
Z = set(filtered_tokens3)
long_wordsW = [w for w in Z if len(w) > 15]
print sorted(long_wordsW)
print len(long_wordsW)
from nltk.text import Text
textW = Text(tokens3)
filtered_textW = Text(filtered_tokens3)
fdistW = FreqDist(textW)
filtered_fdistW = FreqDist(filtered_textW)
print fdistW
word_fdistW = FreqDist([len(w) for w in textW])
filtered_word_fdistW = FreqDist([len(w) for w in filtered_textW])
print word_fdistW
print word_fdistW.keys()
print word_fdistW.items()
print word_fdistW.max()
print word_fdistW.freq(word_fdistW.max())
print filtered_word_fdistW.max()
print filtered_word_fdistW.freq(filtered_word_fdistW.max())
vocabulary3 = fdistW.keys()
print vocabulary3[:10]
filtered_vocab3 = filtered_fdistW.keys()
print filtered_vocab3[:10]
print textW.collocations()
print textW.concordance("great")
print textW.similar("great")


import matplotlib.pyplot as pyplot 
def zipf_dist(freqdist,num_of_ranks=50,show_values=True):
    x = range(1,num_of_ranks+1)
    y = freqdist.values()[:num_of_ranks]
    pyplot.bar(x,y,color="#1AADA4")
    pyplot.xlabel("WALL STREET JOURNAL: Rank of types ordered by frequency of occurrence")
    pyplot.ylabel("Frequency of occurrence")
    pyplot.grid(True)
    pyplot.xticks(range(1,num_of_ranks+1,2),range(1,num_of_ranks+1,2))
    pyplot.xlim([0,num_of_ranks+2])
    if show_values:
        for xi,yi in zip(x,y):
            pyplot.text(xi+0.25,yi+50,yi,verticalalignment="bottom",rotation=55,fontsize="small")
    pyplot.show()
    print "Plot complete."
   
print zipf_dist(fdistW)
print zipf_dist(filtered_fdistW)

#TWITTER
from sussex_nltk.corpus_readers import TwitterCorpusReader
tcr = TwitterCorpusReader()
tokens4 = tcr.sample_words(102152)
print len(tokens4)
print len(set(tokens4))
print len(tokens4) / len(set(tokens4))
from nltk.corpus import stopwords
filtered_tokens4 = [w for w in tokens4 if w.isalpha() and w not in stopwords.words('english')]
print len(filtered_tokens4)
print len(set(filtered_tokens4))
print len(filtered_tokens4) / len(set(filtered_tokens4))
J = set(filtered_tokens4)
long_wordsT = [w for w in J if len(w) > 15]
print sorted(long_wordsT)
print len(long_wordsT)
from nltk.text import Text
textT = Text(tokens4)
filtered_textT = Text(filtered_tokens4)
fdistT = FreqDist(textT)
filtered_fdistT = FreqDist(filtered_textT)
print fdistT
word_fdistT = FreqDist([len(w) for w in textT])
filtered_word_fdistT = FreqDist(len(w) for w in filtered_textT)
print word_fdistT
print word_fdistT.keys()
print word_fdistT.items()
print word_fdistT.max()
print word_fdistT.freq(word_fdistT.max())
print filtered_word_fdistT.max()
print filtered_word_fdistT.freq(filtered_word_fdistT.max())
vocabulary4 = fdistT.keys()
print vocabulary4[:10]
filtered_vocab4 = filtered_fdistT.keys()
print filtered_vocab4[:10]
print textT.collocations()
print textT.concordance("great")
print textT.similar("great")

import matplotlib.pyplot as pyplot 
def zipf_dist(freqdist,num_of_ranks=50,show_values=True):
    x = range(1,num_of_ranks+1)
    y = freqdist.values()[:num_of_ranks]
    pyplot.bar(x,y,color="#1AADA4")
    pyplot.xlabel("TWITTER: Rank of types ordered by frequency of occurrence")
    pyplot.ylabel("Frequency of occurrence")
    pyplot.grid(True)
    pyplot.xticks(range(1,num_of_ranks+1,2),range(1,num_of_ranks+1,2))
    pyplot.xlim([0,num_of_ranks+2])
    if show_values:
        for xi,yi in zip(x,y):
            pyplot.text(xi+0.25,yi+50,yi,verticalalignment="bottom",rotation=55,fontsize="small")
    pyplot.show()
    print "Plot complete."
   
print zipf_dist(fdistT)
print zipf_dist(filtered_fdistT)

#MEDLINE
from sussex_nltk.corpus_readers import MedlineCorpusReader
mcr = MedlineCorpusReader()
tokens5 = mcr.sample_words(102152)
print len(tokens5)
print len(set(tokens5))
print len(tokens5) / len(set(tokens5))
from nltk.corpus import stopwords
filtered_tokens5 = [w for w in tokens5 if w.isalpha() and w not in stopwords.words('english')]
print len(filtered_tokens5)
print len(set(filtered_tokens5))
print len(filtered_tokens5) / len(set(filtered_tokens5))
H = set(filtered_tokens5)
long_wordsM = [w for w in H if len(w) > 15]
print sorted(long_wordsM)
print len(long_wordsM)
from nltk.text import Text
textM = Text(tokens5)
filtered_textM = Text(filtered_tokens5)
fdistM = FreqDist(textM)
filtered_fdistM = FreqDist(filtered_textM)
print fdistM
word_fdistM = FreqDist([len(w) for w in textM])
filtered_word_fdistM = FreqDist([len(w) for w in filtered_textM])
print word_fdistM
print word_fdistM.keys()
print word_fdistM.items()
print word_fdistM.max()
print word_fdistM.freq(word_fdistM.max())
print filtered_word_fdistM.max()
print filtered_word_fdistM.freq(filtered_word_fdistM.max())
vocabulary5 = fdistM.keys()
print vocabulary5[:10]
filtered_vocab5 = filtered_fdistM.keys()
print filtered_vocab5[:10]
print textM.collocations()
print textM.concordance("great")
print textM.similar("great")

import matplotlib.pyplot as pyplot 
def zipf_dist(freqdist,num_of_ranks=50,show_values=True):
    x = range(1,num_of_ranks+1)
    y = freqdist.values()[:num_of_ranks]
    pyplot.bar(x,y,color="#1AADA4")
    pyplot.xlabel("MEDLINE: Rank of types ordered by frequency of occurrence")
    pyplot.ylabel("Frequency of occurrence")
    pyplot.grid(True)
    pyplot.xticks(range(1,num_of_ranks+1,2),range(1,num_of_ranks+1,2))
    pyplot.xlim([0,num_of_ranks+2])
    if show_values:
        for xi,yi in zip(x,y):
            pyplot.text(xi+0.25,yi+50,yi,verticalalignment="bottom",rotation=55,fontsize="small")
    pyplot.show()
    print "Plot complete."
   
print zipf_dist(fdistM)
print zipf_dist(filtered_fdistM)

