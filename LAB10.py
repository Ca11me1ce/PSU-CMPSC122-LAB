class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None

    def __str__(self):
        temp=self.head
        out=''
        while temp:
            out+=str(temp.value)+ ' '
            temp=temp.next
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head,self.tail,out))

    __repr__=__str__


    def isEmpty(self):
        #write your code here
        return self.head==None
    def size(self):
        #write your code here
        if self.head==None:return 0
        count, curr=1, self.head
        while curr!=self.tail:
            count+=1
            curr=curr.next
        return count
    def enqueue(self, value):
        #write your code here
        tmp=None
        if isinstance(value, Node):tmp=value
        else:tmp=Node(value)
        if not self.head:self.head=tmp
        else:
            node=self.head
            while node.next:node=node.next
            node.next=tmp
        self.tail=tmp
    def dequeue(self):
        #write your code here
        if self.head==None:return 'Queue is empty'
        tmp=self.head
        if tmp.next==None:
            n=tmp.value
            self.head,self.tail=None
            return n
        #problem here
        while tmp.next.next!=None:
            tmp=tmp.next
            self.tail=tmp
        n=tmp.next.value
        tmp.next=None
        return n

    # --- Your code ends here

#############################
#                           #
#   test cases, do not copy #
#                           #
#############################
x=Queue()
print(x.isEmpty())
x.enqueue(10)
x.enqueue(3)
x.enqueue(12)
print('---',x,'---')
print(x.dequeue())
x.enqueue(8)
x.enqueue(11)
x.enqueue(5)
print(x.dequeue())
print(x.isEmpty())
print(x.size())
print(x)

"""
x=Queue()
print(x.isEmpty())
print(x.size())
x.enqueue(100)
x.enqueue(500)
x.enqueue(300)
x.enqueue(200)
x.enqueue(400)
print(x)
print(x.size())
print(x.isEmpty())
x.dequeue()
print(x)
print(x.isEmpty())
x.dequeue()
print(x)
print(x.isEmpty())
"""
