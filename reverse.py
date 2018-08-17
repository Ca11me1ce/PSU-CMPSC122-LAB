def reverse(l):
    if len(l)<2:
        return l
    else:
        tmp=[l[-1]]
        return tmp+reverse(l[:-1])

print(reverse([5,8,1]))
