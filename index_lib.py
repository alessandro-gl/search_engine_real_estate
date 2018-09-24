import sys
import os
import nltk as nl
from nltk.stem import SnowballStemmer
snowball_stemmer = SnowballStemmer("italian")
from collections import Counter

def bag(data, threshold=1):
    symbols=['0','1','2','3','4','5','6','7','8','9',',','<','>','/','?',"*",';',':','"','.','[',']','{','}','|','=','+','-','_','(',')','&','^','%','$','#','@','!',"'",'~','\\','\t','\n','\r']         
    for rep_empty in range(len(data)):
    	if data[rep_empty] in symbols:
		data=data.replace(data[rep_empty], " ")
    data=data.split()
    new = [word for word in data if word not in nl.corpus.stopwords.words('italian')]
    data = [snowball_stemmer.stem(word).encode("utf-8") for word in new]
    out = dict(Counter(data))
    return {i:out[i] for i in out if out[i]>= threshold}

def indexloop(k, leng):
    return((k+1) if k<leng else k)

def createIndex(dict_words, bag, post_objects, numb_file):
    list1 = dict_words.keys()

    list2 = bag.keys()
    list1.sort()

    list2.sort()
    l1 =len(list1)

    l2=len(list2)
    loop1 = 0
    loop2 = 0
    if len(list1)==0:
        for key, value in bag.iteritems():

            dict_words[key]=1
            post_objects[key]= [[numb_file, value]]
        return
    while(loop1<l1 and loop2<l2):

        if list1[loop1]==list2[loop2]:
            dict_words[list1[loop1]]+=1

            post_objects[list1[loop1]].append([numb_file, bag[list2[loop2]]])
            loop1=indexloop(loop1, l1)
            loop2=indexloop(loop2, l2)

        elif list1[loop1]>list2[loop2]:
            dict_words[list2[loop2]]=1
            post_objects[list2[loop2]]=[[numb_file, bag[list2[loop2]]]]

            loop2=indexloop(loop2, l2)
        else:
            loop1=indexloop(loop1, l1)      
    if loop2<l2:
        dict_words[list2[loop2]]=1

        post_objects[list2[loop2]]=[[numb_file, bag[list2[loop2]]]]
        loop2=indexloop(loop2, l2)

def readfile(number):
    root="./documents"
    path=root+"/documents-"+str(number/500*500+1).zfill(6)+"-"+str(number/500*500+500).zfill(6)+ "/"
    file = open(path+str(number).zfill(6)+".tsv","r")
    data=file.readline().decode("utf-8")
    return data    

def searchInter(set1, set2):
    set1.sort()

    set2.sort()
    inter=[]

    l1 = len(set1)
    l2 = len(set2)
    loop1=0
    loop2=0
    while(loop1<l1 and loop2<l2):
        if set1[loop1]==set2[loop2]:
            inter.append(set1[loop1])

            loop1=indexloop(loop1, l1)
            loop2 =indexloop(loop2, l2)

        elif set1[loop1]>set2[loop2]:

            loop2 =indexloop(loop2, l2)
        else:
            loop1=indexloop(loop1, l1)

    return inter
    
