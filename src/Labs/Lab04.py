'''
Created on Oct 22, 2012

@author: Alex
'''
import os, sys, nltk, gzip
sys.path.append(os.path.join("D:\\", "LanguageEngineeringNew"))
import os, collections, nltk
urban_dictionary = set()  
f = gzip.open(os.path.join("D:\\","LanguageEngineeringNew","data","UrbanDictionary","terms.gz")) 
for line in f:
    urban_dictionary.add(line.strip())
f.close()

class SpellChecker(object):

    def __init__(self, probability_distribution=None):
        if probability_distribution:
            self.probabilities = probability_distribution
        else:
            gutenberg_spelling_training = os.path.join("D:\\","LanguageEngineeringNew","data","gutenberg","spelling.txt")
            with open(gutenberg_spelling_training) as fh: 
                data = fh.read()
            samples = data.split()
            fd = nltk.probability.FreqDist(samples)
            self.probabilities = nltk.probability.LidstoneProbDist(fd, 0.001)
        self.NWORDS = self.probabilities.samples()
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def edits1(self,word):
        '''Generate all tokens of an edit-distance of 1 away from *word*'''
        splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes    = [a + b[1:] for a, b in splits if b]
        transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
        replaces   = [a + c + b[1:] for a, b in splits for c in self.alphabet if b]
        inserts    = [a + c + b for a, b in splits for c in self.alphabet]
        return set(deletes + transposes + replaces + inserts) 

    def known(self,words):
        '''Return only those tokens in *words* that appear in our training data.''' 
        return set(w for w in words if w in self.NWORDS)

    def correct(self,word):
        '''Given a word, spellcheck it'''
        if self.known([word]) or not word.isalpha(): # if *word* is known, or non-alphabetic
            return word        #then return *word*
        else:
            alters1 = self.edits1(word)
            known_edits1 = self.known(alters1) 
            if known_edits1:
                return max(known_edits1, key=self.probabilities.prob)
            else: #Otherwise no replacement was found, so just give up and return the original word
                alters2 = set()
                for alter1 in alters1:
                    alters2 |= self.edits1(alter1)
                known_edits2 = self.known(alters2)
                if known_edits2:
                    return (max(known_edits2, key=self.probabilities.prob) + ": Resorted to two edits")
                else:
                    return (word + ": Resorted to two edits and found nothing")
                    
s = SpellChecker()

example_tokens = ["porect", "to", "tat"]
for word in example_tokens:
    print "%s --> %s" % (word, s.correct(word))
    
'''    
from sussex_nltk.corpus_readers import ReutersCorpusReader
from sussex_nltk.corpus_readers import MedlineCorpusReader
from sussex_nltk.corpus_readers import TwitterCorpusReader
rcr = ReutersCorpusReader()
mcr = MedlineCorpusReader() 
tcr = TwitterCorpusReader()   
sample_size = 10   
corpus_reader = tcr
tokens = corpus_reader.sample_words_by_sents(sample_size)   

for word in tokens:
    print "%s --> %s" % (word, s.correct(word))
  

tokensT = tcr.sample_words_by_sents(25000) #get a sample of tokens
fd = nltk.probability.FreqDist(tokensT) #build a frequency distribution over tokens
probability_distribution = nltk.probability.LidstoneProbDist(fd, 0.001) #build a probability distribution

#Create a spell checker with new probability distribution
s = SpellChecker(probability_distribution)

#Now use the spellchecker how you normally would    
'''