from Tokenizer import Tokeninzer, Tokeninzer_2_1


class Indexer:
    def __init__(self, Tokenizer, index = {}):
        self.Tokeninzer = Tokeninzer
        self.index = index 
        if Tokeninzer:
            self.tokeninzer = Tokeninzer('snowball_stopwords_EN.txt') 
        else :
            self.tokeninzer = Tokeninzer_2_1('snowball_stopwords_EN.txt')

    def add_document(self,document, body):
        tokens = self.tokeninzer.tokenize(body)
        for t in tokens:
            if t in self.index:
                self.index[t].append(document)
            else:
                self.index[t] = [document]
    def search(self, query):
        tokens = self.tokeninzer.tokenize(query)
        print('search tokens:',tokens)
        documents = {}
        for t in tokens:
            if t not in self.index: continue
            for d in self.index[t]:
                
                if d not in documents:
                    documents[d] = 1
                else:
                    documents[d]+=1

        
        return sorted([(v, k) for k,v in documents.items()])[::-1] 


        
