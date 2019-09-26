


class Indexer:
    def __init__(self):
        self.index = {} 
    def add_document(self,document, tokens):
        
        for t in tokens:
            if t in self.index:
                self.index[t].add(document)
            else:
                self.index[t] = {document}

