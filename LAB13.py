#Lab #13
#Due Date: 07/13/2018, 11:59PM EST

#Name: 


def merge(list1, list2):
    i,j, ls=0, 0, []
    while((i<len(list1))&(j<len(list2))):
        if(list1[i]>list2[j]):
            ls.append(list2[j])
            j+=1
        elif(list1[i]<list2[j]): 
            ls.append(list1[i])
            i+=1
        else:                    
            ls.append(list1[i])
            ls.append(list2[j])
            i+=1
            j+=1
    if(i<len(list1)):
        for m in range(i, len(list1)):ls.append(list1[m])
    else:
        for n in range(j, len(list2)):ls.append(list2[n])
    return ls

def mergeSort(numList):
    ls=[]
    for y in range(len(numList)):ls.append([numList[y]])
    while len(ls)!=1:  
        x=0
        while(x<=len(ls)-2): 
            ls[x]=merge(ls[x], ls[x+1])
            del ls[x+1] 
            x+=1
    numList=ls[0]
    return numList


print(mergeSort([12,35,87,26,9,28,7]))
print(merge([12,35],[26,87]))