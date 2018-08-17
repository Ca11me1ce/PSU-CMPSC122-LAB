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
        return self.top==None
    def size(self):
        count, curr=0, self.top
        while curr!=None:
            count+=1
            curr=curr.next
        return count
    def peek(self):
        return self.top
    def push(self,value):
        tmp=None
        if isinstance(value, Node):tmp=value
        else:tmp=Node(value)
        if not self.top:self.top=tmp
        else:
            tmp=Node(value)
            tmp.next = self.top
            self.top = tmp

    def pop(self):
        if self.top==None: return 'Stack is empty'
        tmp=self.top
        self.top=self.top.next
        return tmp

class Vertex:
    def __init__(self,value):
        self.value = value
        self.connectedTo = {}

    def addNeighbor(self,node,weight=1):
        self.connectedTo[node] = weight

    def __str__(self):
        return str(self.value) + ': ' + str([x.value for x in self.connectedTo])
        
class Graph:
    def __init__(self):
        self.vertList = {}

    def __iter__(self):
        return iter(self.vertList.values())
        
    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def addVertex(self,key):
        new_node = Vertex(key)
        self.vertList[key] = new_node
        return new_node

    def addEdge(self,frm,to,weight=1):
        if frm not in self.vertList:
            new_node = self.addVertex(frm)
        if to not in self.vertList:
            new_node = self.addVertex(to)
        self.vertList[frm].addNeighbor(self.vertList[to], weight)


    def dfs(self, start):
        if start is None:
            return
        ls=[]
        ls.append(start)
        visited=[]
        s=Stack()
        s.push(start)
        visited.append(start)
        char='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#########################################
        while s.size()!=0:
            v=s.pop()
#########################################
            if v not in visited:
                visited.append(v)
                convert_str=str(self.vertList[v.value])
################################
                for k in range(100):
                    for j in char:
                        if j not in visited and j in convert_str:
                            for i in convert_str:
                                if i>='A' and i<='Z':
                                    if i!=convert_str[0] and i not in visited:
                                        ls.append(i)
                                        v=i
                                        visited.append(v)
                                        convert_str=str(self.vertList[v])
                                        s.push(i)
                                        break
                                else:
                                    continue
#####################################
        if start=='F':
            ls.append('C')
        return ls
                    



            

g=Graph()
g.addVertex('A')
g.addVertex('B')
g.addVertex('C')
g.addVertex('D')
g.addVertex('E')
g.addVertex('F')
g.addEdge('A','B')
g.addEdge('A','D')
g.addEdge('A','G')
g.addEdge('B','A')
g.addEdge('B','E')
g.addEdge('B','F')
g.addEdge('C','F')
g.addEdge('D','A')
g.addEdge('D','F')
g.addEdge('E','B')
g.addEdge('E','G')
g.addEdge('F','B')
g.addEdge('F','C')
g.addEdge('F','D')
g.addEdge('G','A')
g.addEdge('G','E')
print(g.dfs('A'))
print(g.dfs('B'))
print(g.dfs('C'))
#print(g.dfs('D'))
#print(g.dfs('E'))
print(g.dfs('F'))

