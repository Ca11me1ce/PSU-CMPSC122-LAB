#Lab #6
#Due Date: 06/15/2018, 11:59PM EST

#Name:


#### DO NOT modify the triangle(n) function in any way! 
def triangle(n):
    return recursive_triangle(n, n)
###################


def recursive_triangle(k, n):
# --- Your code starts here
    ls=''
    if(n==0):
        return# ' '*(k-n)+'*'*n
    recursive_triangle(k, n-1)
    if(n<=k):
        return (' '*(k-n)+'*'*n)
    #return 
# --- ends here



## DELETE THIS PART FROM YOUR FINAL SUBMISSION
### To verify your format
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