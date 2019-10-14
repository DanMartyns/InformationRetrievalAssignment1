from Indexer import Indexer
import os
from collections import deque


class Interpreter:

    def __init__ (self,path,tokenizer) :
        self.path = path
        self.tokenizer = tokenizer

    def process(self, indexer, document):
        
        PMID = None
        value = ''
        tag = ''
        # iterate over file 
        for line in document:

                if line.find('- '):
                    
                    # for each line, split by "-", resulting in a "tag - value"                    
                    if line.startswith('   '):
                        value+=' '+line.strip() 
                    else:
                        if value!="": 
                            # Check if the 'tag' is 'PMID' or 'TI'
                            if tag=='PMID': PMID = value 
                            if tag=='TI': 
                                indexer.add_document(PMID, value)
                        tag, *values = line.split('- ')
                        tag = tag.strip()
                        value = '- '.join(values).strip('\n')              
