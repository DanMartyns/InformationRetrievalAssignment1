import sys
import time
import argparse
from CorpusReader import CorpusReader
import os

def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def metrics(indexer):
    index = indexer.index
    keyvalue = [(j[1],j[0]) for j in sorted([( sum( [i[1] for i in v]  ) ,k) for k,v in index.items()])[-10:][::-1]]
    
    print(keyvalue)



class main:

    def __init__(self, path,tokenizer,search,write):
        start = time.time()

        cr = CorpusReader(path,tokenizer)
        cr.processFile()

        #performance metrics
        print("Index time: {:.2f} seconds".format(time.time()-start))
        size = os.stat(path+'.bin').st_size
        print("Index Size on disk :", sizeof_fmt(size))
        words = cr.index.keys()
        metrics(cr.indexer)
        
        print(f"Vocabulary: {len(words)} words, size: {sizeof_fmt(len(''.join(words)))}")
        if search != '':
            print(cr.indexer.search(search))
        if write:
            cr.indexer.writeIndexToFile(f"{path}_indexer.txt")
        



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Information Retrieval')
    parser.add_argument('-f', '--file', help='The path of the file')
    parser.add_argument('-t','--tokenizer', help='If you choose this flag, the tokenizer is the better one, other wise is the simple one', action='store_true') #default=False is implied by action='store_true'
    parser.add_argument('-s', '--search',nargs='*', type=str, help='Search in the documents where is the word or line you want', default='')
    parser.add_argument('-d','--delete',help='Delete the corresponding bin file', action='store_true')
    parser.add_argument('-w','--write',help='Write results in a file text',action='store_true')

    args = parser.parse_args()
    
    
    
    if args.delete:
        try: 
            os.remove(args.file+".bin")
        except:
            print("File does not exist, use -d flag to delete index")
    main(args.file,args.tokenizer, ' '.join(args.search),args.write)
    