def reverse(l):
    if not l:return []
    return [l[-1]]+reverse(l[:-1])

#############################
#                           #
#   test case, do not copy  #
#                           #
#############################
print(reverse([5,8,1]))
