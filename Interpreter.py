from Tokenizer import Tokeninzer
import os

def log(progress, maximum):
    perc = round(progress/maximum*50)
    going = perc<50
    print('\r ['+'='*perc+ '>'*going+'.'*(50-perc-going)+'] ',str(perc*2)+'%',end = '\r')

class Interpreter:

    def process(self,path):
        tokeninzer = Tokeninzer('snowball_stopwords_EN.txt') 
        
        #feedback variables
        maximum = os.stat(path).st_size
        
        # initialize the variables
        i=0
        progress = 0
        
        PMID = []
        TI = []
        
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
                        value+=line.strip()
                    else:
                        if value!="": 
                            # Check if the 'tag' is 'PMID' or 'TI'
                            if tag=='PMID': PMID.append(value)
                            if tag=='TI': 
                                TI.append(tokeninzer.tokenize(value))
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
        return [ {'PMID': i,'TI': t} for i,t in zip(PMID,TI)]