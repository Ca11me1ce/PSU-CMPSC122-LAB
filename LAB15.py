def makingSound(n,sound):
        def nested(arg):
            ls=[]
            for i in range(arg):
                if i%n==0:ls.append(sound)
                else:ls.append(i)
            return ls
        return nested
            
"""
Test cases, do not copy!
"""
catSound=makingSound(6, 'Meow')
print(catSound(10))
print(makingSound(6, 'Meow')(10))
