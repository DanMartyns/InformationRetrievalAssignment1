import sys
import os 
from CorpusReader import *

class main:

    def __init__(self, path):
        self.cr = CorpusReader(path)
        documents = []

        while(self.cr.hasNextDocument()):
            documents.append(self.cr.getNextDocument())

        # enumerates all the documents
        print(enumerate(documents))


if __name__ == "__main__":
    main(sys.argv[1])