from Interpreter import *
import pickle
from os.path import isfile
class CorpusReader:
    
    def __init__(self,path):
        interpreter = Interpreter()
        # return all the documents present in the file
        output = path+'.bin'
        if isfile(output):
            print('loading tokens')
            self.documents = pickle.load(open(output,'rb'))
        else:
            self.documents = interpreter.process(path)
            print('\nsaving tokens')
            pickle.dump(self.documents, open(output,'wb'))
        
        # initialize iterator variable                
        self.iterator = 0
    
    # check if there is a next Document
    def hasNextDocument(self):
        return self.iterator < len(self.documents)

    # returns the next Document
    def getNextDocument(self):
        if not self.hasNextDocument() :
            return None
        dic = self.documents[self.iterator]
        self.iterator += 1
        return dic
