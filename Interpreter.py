class Interpreter:

    def process(self,path):
        lista = []
        
        # open the file
        file = open(path,"r")
        
        # iterate over file 
        for line in file :
                
                # initialize the variables
                value = ""
                
                # check if the line is a "tag - value" or the continuation of the value of the previous tag.
                if line.find('-'):

                    # for each line, split by "-", resulting in a "tag - value"                    
                    r = line.split("-")
                    tag = r[0].strip()

                    # Check if the 'tag' is 'PMID' or 'TI'
                    # A dictionary has: {'PMID': value , 'TI': value }
                    # each dictionary will represent a document
                    if tag == "PMID" or tag == "TI":            
                        value = r[1]
                
                # if is the continuation of the value of the previous tag, is ignored
                else : 
                    value += r[1]     

                # Add to a dictionary
                lista.append(value)            
        file.close()

        # returns a list consisting of several dictionaries
        return [ {'PMID':i[0],'TI':i[1]} for i in group(lista,2)]