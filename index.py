
import nltk
nltk.download('stopwords')
from  index_lib import *

dict_words={}
posting_file= {}
file_numbers = 200

print "\nLoading...\n"
for item in range(file_numbers):
    read_data = readfile(item)
    sys.stdout.flush()
    bags=  bag(read_data)
    createIndex(dict_words,bags, posting_file, item)
print "Done.\n" 
print "vocabulary.txt and postings.txt created in index folder.\n"

dictionary=dict_words.keys()
dictionary.sort()

if not os.path.exists("index"):
    os.makedirs("index")
outpath="./index/"
vocabulary= open(outpath+"vocabulary.txt", "w")
postings = open(outpath+"postings.txt", "w")
k=0
for word in dictionary:
    vocabulary.write(str(k)+"\t"+word+"\n")
    outstr=""
    for element in posting_file[word]:
        outstr+=str(element[0])+"\t"
    postings.write(str(k)+"\t"+outstr+"\n")
    k+=1

