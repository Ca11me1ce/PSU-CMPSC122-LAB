def bubbleSort(numList):
    oldls=[]
    for i in range(len(numList)-1, 0, -1):
        oldls=numList
        for j in range(i):
            if numList[j+1]<numList[j]:
                tmp=numList[j]
                numList[j]=numList[j+1]
                numList[j+1]=tmp
        if oldls==numList:
            print(numList)
    return numList
bubbleSort([89, 15, 73, 40, 99, 56, 22, 7 ])