def isPalindrome(s):
    if len(s)>-1 and len(s)<2:return True
    if s[-1]!=s[0]:return False
    else:return isPalindrome(s[1:-1])
    
print(isPalindrome('noon'))
