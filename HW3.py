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

def findNextOpr(txt):
    if len(txt)<=0 or not isinstance(txt,str):
        print("type error: findNextOpr")
        return "type error: findNextOpr"
    a=[]
    b=txt.strip()
    if chr(42) not in txt and chr(45) not in txt and chr(43) not in txt and chr(47) not in txt and chr(94) not in txt:
        return -1

    for x in range(len(b)):
        if (b[x]==chr(42) or b[x]==chr(45) or b[x]==chr(43) or b[x]==chr(47) or b[x]==chr(94)) and x!=0:
            a.append(b[x])

    if a==[]:
        return -1
    else:
        return txt.find(a[0])

def isNumber(txt):
    if len(txt)==0 or not isinstance(txt, str):
        print("type error: isNumber")
        return "type error: isNumber"
    txt=txt.strip()

    try:
        if txt[0] == '-':
            txt=txt[1:]
    except:
        return False
    try:
        float(txt)
        return True
    except:
        return False


def getNextNumber(expr, pos):
    if len(expr)==0 or not isinstance(expr, str) or pos<0 or pos>=len(expr) or not isinstance(pos, int):
        print("type error: getNextNumber")
        return None, None, "type error: getNextNumber"
    txt = expr[pos:]
    oprPos = findNextOpr(txt)
    if oprPos != -1:
        if isNumber(txt[:oprPos])==True:
            return float(txt[:oprPos]), txt[oprPos], oprPos+pos

        else:
            return None, txt[oprPos], oprPos+pos
    else:
        if isNumber(txt):
            return float(txt), None, None

        else:
            return None, None, None


def exeOpr(num1, opr, num2):
    if opr=="+":
        return num1+num2

    elif opr=="-":
        return num1-num2

    elif opr=="*":
        return num1*num2

    elif opr=="/":
        if num2==0:
            print("Zero division error")
            return "Zero division error"
        else:
            return num1/num2

    elif opr=="^":
        return num1 ** num2

    else:
        print("error in exeOpr")
        return "error in exeOpr"

def _calculator(expr):
    if len(expr)<=0 or not isinstance(expr,str):

        print("input error: line A in calculator")
        return "input error: line A in calculator"

    expr = expr.strip()
    if expr[0]!="-":
        newNumber, newOpr, oprPos = getNextNumber(expr, 0)

    else:
        newNumber, newOpr, oprPos = getNextNumber(expr, 1)
        newNumber *= -1

    if newNumber is None:
        print("input error: line B in calculator")
        return "input error: line B in calculator"

    elif newOpr is None:
        return newNumber

    elif newOpr=="+" or newOpr=="-":
        mode="add"
        addResult=newNumber 
        mulResult=None
        expResult=None 

    elif newOpr=="*" or newOpr=="/":
        mode="mul"
        addResult=0
        mulResult=newNumber
        expResult=None

    elif newOpr=="^":
        mode="exp"
        expResult=newNumber
        addResult=0
        mulResult=None
    pos=oprPos+1
    opr=newOpr  
    oldopr=None

    while True:
        newNumber, newOpr, oprPos = getNextNumber(expr, pos)
        if newNumber is None:
            return "input error: line B in calculator"

        elif newOpr is None:
            if mode=='add':
                if opr=='*':
                    return exeOpr(addResult, oldopr, mulResult*newNumber)
                elif opr=='/':
                    return exeOpr(addResult, oldopr, mulResult/newNumber)
                else:
                    return exeOpr(addResult, opr, newNumber)
            elif mode=='mul':
                if expResult==None:
                    expResult=0

                if mulResult==None:
                    mulResult=0
                return addResult + exeOpr(mulResult, opr, newNumber)

            elif mode=="exp":
                if expResult<0:
                    expResult=exeOpr(expResult,opr,newNumber)
                    if expResult>0:
                        expResult=-1*expResult

                else:
                    expResult=exeOpr(expResult,opr,newNumber)

                if mulResult!=0 and (oldopr=='*' or oldopr=='/'):
                    mulResult=exeOpr(mulResult,oldopr,expResult)
                    expResult=0

        elif newOpr=='+' or newOpr=='-':
            if expResult==None:
                expResult=0

            if mulResult==None:
                mulResult=0

            if mode=='add':
                addResult = exeOpr(addResult, opr, newNumber)
                mulResult = 0
                expResult= 0

            elif mode=='mul':
                addResult += exeOpr(mulResult, opr, newNumber)
                mulResult = 0
                expResult= 0

            elif mode=='exp':
                if expResult<0:
                    expResult=exeOpr(expResult,opr,newNumber)
                    if expResult>0:
                        expResult=-1*expResult
                        addResult+=expResult

                else:
                    addResult+=exeOpr(expResult,opr,newNumber)

                if oldopr=='*' or oldopr=='/':
                    expResult=exeOpr(expResult,opr,newNumber)
                    mulResult=exeOpr(mulResult,oldopr,expResult)
                    addResult+=mulResult

                mulResult = 0
                expResult = 0

            mode='add'

        elif newOpr=="*" or newOpr=="/":
            if mode=='add':                
                if opr=='-':
                    oldopr='-'
                    mulResult = newNumber

                elif opr=='+':
                    #print('here1')
                    oldopr='+'
                    mulResult = newNumber
                    mode='mul'
                else:
                    mulResult = newNumber

            elif mode=='mul':
                mulResult = exeOpr(mulResult, opr, newNumber)

            elif mode=='exp':
                if expResult<0:
                    expResult=exeOpr(expResult,opr,newNumber)
                    if expResult>0:
                        expResult=-1*expResult
                else:
                    expResult=exeOpr(expResult,opr,newNumber)

                if  mulResult !=0 and (oldopr=='*' or oldopr=='/'):
                    mulResult=exeOpr(mulResult,oldopr,expResult)
                    expResult=0

                else:
                    mulResult=expResult
                    expResult=0
                mode='mul'
        elif newOpr=='^':
            if mode=='add':
                if expResult==None:
                    expResult=0

                if mulResult==None:
                    mulResult=0

                if opr=='-':
                    expResult = -newNumber

                else:
                    expResult = newNumber
                oldopr=opr
            elif mode=='mul':
                expResult=newNumber
                oldopr=opr

            mode='exp'    

        if oprPos==None:
            break

        pos=oprPos + 1
        opr=newOpr

    if mulResult== None:
        mulResult=0

    if expResult==None:
        expResult=0

    return addResult+mulResult+expResult 

def calculator(expr):
    if len(expr)<=0 or not isinstance(expr,str): 
        print("argument error: calculator")
        return "argument error: calculator"

    expr = expr.strip()
    s = Stack()
    pos = expr.find("(")

    while True:
        if '(' in expr and ')' not in expr:
            return 'error'

        elif '(' not in expr and ')' in expr:
            return 'error'

        elif '(' not in expr and ')' not in expr:
            return _calculator(expr)

        else:
            for x in range(len(expr)):
                if expr[x]=='(':
                    s.push(x)

                elif expr[x]==')':
                    a=s.pop().value
                    if not isinstance(a,int):
                        return 'error'
                    else:  
                        expr1=expr[a+1:x]
                        expr1=_calculator(expr1)
                        expr=expr[:a]+str(expr1)+expr[x+1:]
                        return calculator(expr)

    
print(calculator("3*(10 - 2*3)"))
print(calculator(" -2 / (- 4) * (3 - 2*( 4- 2^3)) +3"))
print(calculator("2*(4+2*(5-3^2)+1)+4"))
print(calculator("-(-2)*10 - 3*(2 - 3*2) "))
print(calculator("-(-2)*10 - 3*(2 - 3*2)) "))
print(calculator("-(-2)*10 - 3*/(2 - 3*2) "))
