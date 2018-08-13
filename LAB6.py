def triangle(n):
    return recursive_triangle(n, n)


def recursive_triangle(k, n):
    ls=''
    if(n==0):
        return# ' '*(k-n)+'*'*n
    recursive_triangle(k, n-1)
    if(n<=k):
        return (' '*(k-n)+'*'*n)



print(recursive_triangle(3, 5))
print(triangle(8))
# should output:
#  ***
#   **
#    *
#
#********
# *******
#  ******
#   *****
#    ****
#     ***
#      **
#       *
