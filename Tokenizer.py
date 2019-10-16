
from Stemmer import Stemmer

class Tokeninzer:
    
    def __init__(self,path):
        self.stemmer = Stemmer('english')
        # open the file and separate each line        
        file = open(path,'r', encoding='utf-8', errors='ignore')
        self.stopwords = set([i.strip('\n') for i in file.readlines()]+['s'])
    
    def tokenize(self,TI):
        st = self.stemmer
        #for efficiency
        stopwords = self.stopwords
        # replace all non-alphabetic characters by a space and convert a character to lowercase
        lowercase = ''.join([i if i.isalpha() else ' ' for i in TI.lower()])
        # replace all duplicate spaces for one and list of sorted words not in stopwords and reduce inflected words to their word stem
        return sorted([st.stemWord(i) for i in lowercase.replace('  ',' ').split() if i not in stopwords])
    
class Tokeninzer_2_1: #no stopwords implemented
    
    def __init__(self, path):
        pass
    
    def tokenize(self,TI):
        # replace all non-alphabetic characters by a space and convert a character to lowercase
        lowercase = ''.join([i if i.isalpha() else ' ' for i in TI.lower()])
        # replace all duplicate spaces for one and list of sorted words with more than 3 characters 
        return sorted([i for i in lowercase.replace('  ',' ').split() if len(i)>3])
    

