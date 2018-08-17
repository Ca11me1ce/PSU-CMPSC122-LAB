#Lab #7
#Due Date: 06/15/2018, 11:59PM EST

#Name:

### You can add a second parameter to the function call
### if you believe you need it.
### However, it must be preloaded, as the user will only provide the number
def isPrime(n, i=2):
# --- Your code starts here
    if(n<2):return False
    if(n==2):return True
    if(n%i==0):return False
    if(i==n-1):return True
    return isPrime(n, i+1)
# --- ends here

## isPrime(2) should return True
## isPrime(6) should return False