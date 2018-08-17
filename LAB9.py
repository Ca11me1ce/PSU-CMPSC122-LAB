#Lab #9
#Due Date: 07/06/2018, 11:59PM EST

#Name:


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

class Stack:
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=''
        while temp:
            out+=str(temp.value)+ '\n'
            temp=temp.next
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        #write your code here
        return self.top==None
    def size(self):
        #write your code here
        count, curr=0, self.top
        while curr!=None:
            count+=1
            curr=curr.next
        return count
    def peek(self):
        #write your code here
        return self.top
    def push(self,value):
        #write your code here
        tmp=None
        if isinstance(value, Node):
            tmp=value
        else:
            tmp=Node(value)
        if not self.top:
            self.top=tmp
        #problem here
        else:
            node=self.top
            while node.next:
                node=node.next
            node.next=tmp
            #self.top=tmp
        #self.top=tmp
    def pop(self):
        #write your code here
        if self.top==None: return 'Stack is empty'
        tmp=self.top
        self.top=self.top.next
        return tmp
    # --- Your code ends here
    
#############################
#                           #
#   test cases, do not copy #
#                           #
#############################
x=Stack()
x.push(3)
x.push(1)
print(x)
print(x.pop())
print(x.pop())
print('----------')
x.push(5)
x.push(9)
x.push(7)
x.push(2)
print(x)
print('----------')
print(x.pop())
x.push(55)
print('@@@@@')
print(x.pop())
print(x.pop())
print('@@@@@')
print(x)
"""
x=Stack()
print(x.isEmpty())
print(x.size())
print(x.pop())
x.push(100)
x.push(400)
x.push(300)
x.push(200)
print(x)
print(x.peek())
print(x.isEmpty())
print(x.size())
x.pop()
print(x)
print(x.peek())
print(x.size())
"""



