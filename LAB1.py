#!/usr/bin/python3.5
#coding: UTF-8

def joinedList(n):
    a=[]
    ls=[]
    if type(n)==int:
        a=list(range(1, n+1))
        ls.extend(a)
        a.reverse()
        ls.extend(a)
        return ls
    else:
        return "Invalid input"

def removePunctuation(txt):
    if type(txt)==str:
        for i in txt:
            if i.isalpha()==False:
                txt=txt.replace(i, " ")
        return txt
    else:
        return "Invalid input"