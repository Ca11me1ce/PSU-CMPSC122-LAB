#Lab #8
#Due Date: 07/06/2018, 11:59PM EST

#Name:

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
#Tip: work on paper first to see what pointers need to be updated
#     based on the position of the Node
                          
class OrderedLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        #self.length=0 #I added this attribute

    def __str__(self):
        temp=self.head
        out=''
        while temp:
            out+=str(temp.value)+ ' '
            temp=temp.next
        return ('Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out))

    __repr__=__str__


    def add(self, value):
        #write your code here
        tmp=None
        if isinstance(value, Node):tmp=value
        else:tmp=Node(value)
        if not self.head:self.head=tmp
        else:
            node=self.head
            while node.next:node=node.next
            node.next=tmp
        if self.head is None:return
        curr=self.head.next
        while curr!=None:
            curr_next, ptr=curr.value, self.head
            while ptr!=curr and ptr.value<=curr_next:ptr=ptr.next
            while ptr!=curr:
                curr_next,ptr.value=ptr.value,curr_next
                ptr=ptr.next
            curr.value=curr_next
            curr=curr.next
        self.tail=tmp
    def pop(self):
        #write your code here
        if self.head==None:return 'List is empty'
        tmp=self.head
        if tmp.next==None:
            n=tmp.value
            self.head,self.tail=None
            return n
        while tmp.next.next!=None:
            tmp=tmp.next
            self.tail=tmp
        n=tmp.next.value
        tmp.next=None
        return n
    def isEmpty(self):
        #write your code here
        return (self.head==None)
    def size(self):
        #write your code here
        if self.head==None:return 0
        count, curr=1, self.head
        while curr!=self.tail:
            count+=1
            curr=curr.next
        return count
    # --- Your code ends here

#############################
#                           #
#   test cases, do not copy #
#                           #
#############################
x=OrderedLinkedList()
print(x.size())
print(x.isEmpty())
print(x.pop())
#x.isEmpty()
x.add(7)
x.add(-11)
x.add(9)
x.add(1)
x.add(-1000)
print(x)
print(x.isEmpty())
print(x.size())
