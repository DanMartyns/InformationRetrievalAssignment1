from Tokenizer import Tokeninzer, Tokeninzer_2_1


class Indexer:
    def __init__(self, Tokenizer, index = {}):
        self.Tokeninzer = Tokeninzer
        self.index = index 
        if Tokeninzer:
            self.tokeninzer = Tokeninzer('snowball_stopwords_EN.txt') 
        else :
            self.tokeninzer = Tokeninzer_2_1()

    def add_document(self,document, body):
        tokens = self.tokeninzer.tokenize(body)
        lastToken = None
        for t in tokens:
            if lastToken==t:
                continue
            if t in self.index:
                self.index[t].append((document, tokens.count(t)))
            else:
                self.index[t] = [(document, tokens.count(t))]
            lastToken = t
    def search(self, query):
        tokens = self.tokeninzer.tokenize(query)
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
    
    def writeIndexToFile(self, output=''):
        #aaaaa,doc id:term freq,doc id:term freq,…
        #aaaab,doc id:term freq,doc id:term freq,…
        #aaaac,doc id:term freq,doc id:term freq,…
        keys = sorted(self.index.keys())
        #fw = file('')
        for k in keys:
            print(*([k]+[info for d in self.index[k] for info in d]),sep=',')
        
