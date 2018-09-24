from  index_lib import *

print ""
search_input = raw_input("Enter your keywords: ")
search_bag = bag(search_input)

vocabulary = open("./index/vocabulary.txt","r")
split_vocabulary = vocabulary.read().splitlines()
create_index={}
for row in split_vocabulary:
        row = row.split("\t")
        create_index[row[1]]=row[0]

postings =  open("./index/postings.txt","r")
split_postings = postings.read().splitlines()
create_postings ={}
for row in split_postings:
        row = row.split("\t")
        create_postings[row[0]] = [row[n] for n in range(1,len(row)-1)]
        
output = searchInter(create_index.keys(), search_bag.keys())
out_obj = create_postings[create_index[output[0]]]

for row in output:
        out_obj = searchInter(out_obj, create_postings[create_index[row]])
for obj_raw in out_obj:
        print ""
        file = readfile(int(obj_raw))
        print file
        print ""

