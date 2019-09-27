import sys
import time
import argparse
from CorpusReader import *

class main:

    def __init__(self, path,tokenizer,search):
        self.cr = CorpusReader(path,tokenizer,search)
        documents = []

        while(self.cr.hasNextDocument()):
            documents.append(self.cr.getNextDocument())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Information Retrieval')
    parser.add_argument('-f', '--file', help='The path of the file')
    parser.add_argument('-t','--tokenizer', help='If you choose this flag, the tokenizer is the better one, other wise is the simple one', action='store_true') #default=False is implied by action='store_true'
    parser.add_argument('-s', '--search',nargs='*', type=str, help='Search in the documents where is the word or line you want', default='')
    
    args = parser.parse_args()
    start = time.time()
    main(args.file,args.tokenizer, ' '.join(args.search))
    print("Execution time : {:.2f} seconds".format(time.time()-start))