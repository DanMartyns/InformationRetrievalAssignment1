from Tokenizer import Tokeninzer
from Indexer import Indexer
import os
from collections import deque



def log(progress, maximum):
    perc = round(progress/maximum*50)
    going = perc<50
    print('\r ['+'='*perc+ '>'*going+'.'*(50-perc-going)+'] ',str(perc*2)+'%',end = '\r')

class Interpreter:

    def process(self,path):
        tokeninzer = Tokeninzer('snowball_stopwords_EN.txt') 
        indexer = Indexer()
        #feedback variables
        maximum = os.stat(path).st_size
        
        # initialize the variables
        i=0
        progress = 0
        
        PMID = None
        TI = None
        
        # open the file
        file = open(path,'r', encoding='utf-8', errors='ignore')
        value = ''
        tag = ''
        
        # iterate over file 
        for line in file:
                progress += len(line)

                if line.find('- '):
                    
                    # for each line, split by "-", resulting in a "tag - value"                    
                    if line.startswith('   '):
                        value+=' '+line.strip() 
                    else:
                        if value!="": 
                            # Check if the 'tag' is 'PMID' or 'TI'
                            if tag=='PMID': PMID = value 
                            if tag=='TI': 
                                TI = tokeninzer.tokenize(value)
                                indexer.add_document(PMID, TI)
                        tag, *values = line.split('- ')
                        tag = tag.strip()
                        value = '- '.join(values).strip('\n')
                        
                    #print('line',line)
                    #print('tag',tag)               
                    
                    i+=1
                    if i>=5000:
                        i=0
                        log(progress, maximum)

                            
        file.close()
        #print([{'PMID':i,'TI':t} for i,t in zip(PMID,TI)])
        
        # returns a list consisting of several dictionaries
        # each dictionary will represent a document
        # return {i:t for i,t in zip(PMID,TI) } returns directly to index
        return indexer.index
        #return [ {'PMID': i,'TI': t} for i,t in zip(PMID,TI)]