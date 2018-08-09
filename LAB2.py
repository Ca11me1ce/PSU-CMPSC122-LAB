#!/usr/bin/python3.5
#coding: UTF-8
import LAB1

def countWords(txt):
    txt=LAB1.removePunctuation(txt)
    txt=txt.lower()
    if txt!="invalid input":
        ls=txt.split(' ')
        count={}
        for i in ls:
            if i=='':
                continue
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        return count
    return "Invalid input"