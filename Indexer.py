
class Indexer:
    def __init__(self, Tokenizer, index = {}):
        self.index = index 
        self.tokenizer = Tokenizer('snowball_stopwords_EN.txt') 

    def add_document(self,document, body):
        tokens = self.tokenizer.tokenize(body)
        lastToken = None
        for t in tokens:
            if lastToken==t:
                self.index[t][-1] = (self.index[t][-1][0], self.index[t][-1][1]+1)
                continue
            if t in self.index:
                self.index[t].append((document, 1))
            else:
                self.index[t] = [(document, tokens.count(t))]
            lastToken = t
    def search(self, query):
        tokens = self.tokenizer.tokenize(query)
        print('search tokens:',tokens)
        documents = {}
        for t in tokens:
            if t not in self.index: continue
            for d in self.index[t]:
                doc, count = d
                if doc not in documents:
                    documents[doc] = count
                else:
                    documents[doc]+=count

        
        return sorted([(v, k) for k,v in documents.items()])[::-1] 
    
    def writeIndexToFile(self, output='output.txt'):
        #aaaaa,doc id:term freq,doc id:term freq,…
        #aaaab,doc id:term freq,doc id:term freq,…
        #aaaac,doc id:term freq,doc id:term freq,…
        keys = sorted(self.index.keys())
        with open(output,'w') as fw:
            fw.write( '\n'.join([','.join([k]+[str(info) for d in self.index[k] for info in d]) for k in keys]))
        
