from Interpreter import *
from Indexer import Indexer
import pickle
from os.path import isfile
class CorpusReader:
    
    def __init__(self,path,tokenizer,search,write):
        self.path = path
        self.tokenizer = tokenizer
        self.search = search
        self.write = write
        
        interpreter = Interpreter(self.path,self.tokenizer)
        # return all the documents present in the file
        output = path+'.bin'
        if isfile(output):
            
            print('loading tokens')
            self.documents = pickle.load(open(output,'rb'))
            
        else:
            self.documents = interpreter.process()
            print('\nsaving tokens')
            pickle.dump(self.documents, open(output,'wb'))
          
        indexer = Indexer(self.tokenizer,index = self.documents)
        if self.search != '':
            print(indexer.search(self.search))
        if self.write:
            indexer.writeIndexToFile(f"{path}_indexer.txt")
        # initialize iterator variable                
        self.iterator = 0
    
    # check if there is a next Document
    def hasNextDocument(self):
        return self.iterator < len(self.documents)

    # returns the next Document
    def getNextDocument(self):
        if not self.hasNextDocument() :
            return None
        dic = self.documents#[self.iterator]
        self.iterator += 1
        return dic
