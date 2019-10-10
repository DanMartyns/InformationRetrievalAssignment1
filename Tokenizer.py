
from Stemmer import Stemmer
class Tokeninzer:
    def __init__(self,path):
        self.stemmer = Stemmer('english')
        file = open(path,'r', encoding='utf-8', errors='ignore')
        self.stopwords = set([i.strip('\n') for i in file.readlines()]+['s'])
    def tokenize(self,TI):
        st = self.stemmer
        stopwords = self.stopwords #for efficiency
        lowercase = ''.join([i if i.isalpha() else ' ' for i in TI.lower()])
        return sorted([st.stemWord(i) for i in lowercase.replace('  ',' ').split() if i not in stopwords])
    
class Tokeninzer_2_1: #no stopwords implemented
    def __init__(self):
        pass
    def tokenize(self,TI):
        lowercase = ''.join([i if i.isalpha() else ' ' for i in TI.lower()])
        return sorted([i for i in lowercase.replace('  ',' ').split() if len(i)>3])
    

