def isPrime(n, i=2):
    if(n<2):return False
    if(n==2):return True
    if(n%i==0):return False
    if(i==n-1):return True
    return isPrime(n, i+1)
## isPrime(2) should return True
## isPrime(6) should return False