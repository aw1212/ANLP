'''
Created on Oct 19, 2012

@author: Alex
'''
import os, sys, nltk
import re
sys.path.append(os.path.join("D:\\", "LanguageEngineeringNew"))
import sussex_nltk
from nltk.tokenize import word_tokenize
from sussex_nltk.corpus_readers import ReutersCorpusReader
from sussex_nltk.corpus_readers import MedlineCorpusReader
from sussex_nltk.corpus_readers import TwitterCorpusReader
rcr = ReutersCorpusReader()
mcr = MedlineCorpusReader() 
tcr = TwitterCorpusReader()  
'''
#whitespace

for sentence in rcr.sample_raw_sents(50):
    print sentence
    print sentence.split()
    

for sentence in mcr.sample_raw_sents(50):
    print sentence
    print sentence.split()


for sentence in tcr.sample_raw_sents(50):
    print sentence
    print sentence.split()


corpus_reader = rcr
number_of_sample_sents = 50

def lab3(corpus_reader, number_of_sample_sents): 
    for sentence in corpus_reader.sample_raw_sents(number_of_sample_sents):   
        s = re.sub("([.?!'])"," \g<1>", sentence)
        print re.sub("([%$#@])"," \g<1>", s).split()

print lab3(rcr, 50)    

corpus_reader = mcr
print lab3(mcr, 50)

corpus_reader = tcr
print lab3(tcr, 50)


from nltk.tokenize import word_tokenize
for sentence in rcr.sample_raw_sents(50):
    words = word_tokenize(sentence)
    print words

from nltk.tokenize import word_tokenize
for sentence in mcr.sample_raw_sents(50):
    words = word_tokenize(sentence)
    print words    
    

from nltk.tokenize import word_tokenize
for sentence in tcr.sample_raw_sents(50):
    words = word_tokenize(sentence)
    print words        

def lab3plus(corpus_reader, number_of_sample_sents):
    for sentence in corpus_reader.sample_raw_sents(number_of_sample_sents):
        t = re.sub("([.?!'])"," \g<1>", sentence).split()
    for words in t:
        print words
        
print lab3plus(rcr, 50)        
'''   
from sussex_nltk.tokenize import twitter_tokenize, twitter_tokenize_batch 
for sentence in tcr.sample_raw_sents(50):               
    print twitter_tokenize(sentence) 