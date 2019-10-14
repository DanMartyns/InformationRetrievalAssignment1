from Interpreter import Interpreter
from Tokenizer import Tokeninzer, Tokeninzer_2_1
from Indexer import Indexer
import pickle
from os.path import isfile
import os

def log(progress, maximum):
    perc = round(progress/maximum*50)
    going = perc<50
    print('\r ['+'='*perc+ '>'*going+'.'*(50-perc-going)+'] ',str(perc*2)+'%',end = '\r')


class CorpusReader:
    
    def __init__(self,path,tokenizer,search,write):
        self.path = path
        self.tokenizer = Tokeninzer_2_1 if tokenizer else Tokeninzer
        self.search = search
        self.write = write
        
    
    # check if there is a next Document
    def processFile(self):
        interpreter = Interpreter(self.path,self.tokenizer)
        
        # return all the documents present in the file
        output = self.path+'.bin'
        if isfile(output):
            print('loading tokens')
            self.documents = pickle.load(open(output,'rb'))
            indexer = Indexer(self.tokenizer,index = self.documents)
        else:
            indexer = Indexer(self.tokenizer)
            file = open(self.path,'r', encoding='utf-8', errors='ignore')
            maximum = os.stat(self.path).st_size
            # initialize the variables
            i=0
            progress = 0
            document = []
            for line in file:
                    progress += len(line)
                    if line=='\n':
                        interpreter.process(indexer, document)
                        document = []
                    else:
                        document+=[line]
                    i+=1
                    if i>=5000:
                        i=0
                        log(progress, maximum)

                            
            file.close()
            self.documents = indexer.index
            print('\nsaving tokens')
            pickle.dump(self.documents, open(output,'wb'))
          
        
        if self.search != '':
            print(indexer.search(self.search))
        if self.write:
            indexer.writeIndexToFile(f"{self.path}_indexer.txt")

