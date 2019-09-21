from Interpreter import *

class CorpusReader:
    
    def __init__(self,path):
        interpreter = Interpreter()
        # return all the documents present in the file
        self.documents = interpreter.process(path)
        # initialize iterator variable                
        self.iterator = 0
    
    # check if there is a next Document
    def hasNextDocument():
        return iterator < len(documents)

    # returns the next Document
    def getNextDocument():
        if not hasNextDocument() :
            return null
        dic = documents[iterator]
        iterator += 1
        return dic
