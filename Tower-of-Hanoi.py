import sys

def recursive_toh(n,start,end,intermediate):
    if n==0:
        return
    recursive_toh(n-1,start,intermediate,end)
    print(f"Move disc {n} from {start} to {end}")
    recursive_toh(n-1,intermediate,end,start)



class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.array = [0]*capacity
        
def createStack(capacity):
    stack = Stack(capacity)
    return stack
    
def isFull(stack):
    return (stack.top == (stack.capacity - 1))
    
def isEmpty(stack):
    return (stack.top == -1)
    
def push(stack, data):
    if isFull(stack):
        return
    stack.top += 1
    stack.array[stack.top] = data
    
def pop(stack):
    if isEmpty(stack):
        return -sys.maxsize
    Top = stack.top
    stack.top -= 1
    return stack.array[Top]

def move(fromrod, torod, disc):
    print(f"Move Disc {disc} from {fromrod} to {torod}")

def movediscs(start,end,s,d):
    p1top = pop(start)
    p2top = pop(end)
    
    if p1top == -sys.maxsize:
        push(start,p2top)
        move(d,s,p2top)
        
    elif p2top == -sys.maxsize:
        push(end,p1top)
        move(s,d,p1top)
        
    elif p1top > p2top:
        push(start,p1top)
        push(start,p2top)
        move(d,s,p2top)
        
    else:
        push(end,p2top)
        push(end,p1top)
        move(s,d,p1top)

def nonrecursive_toh(n,start,end,intermediate):
    s,d,a = start,end,intermediate
    if n%2 == 0:
        a,d = d,a
    no_of_moves = pow(2,n)-1
    
    for i in range(n,0,-1):
        push(start,i)
    
    for i in range(1,no_of_moves+1):
        if i%3 == 1:
            movediscs(start,end,s,d)
        elif i%3 == 2:
            movediscs(start,intermediate,s,a)
        else:
            movediscs(intermediate,end,a,d)
        

if __name__=="__main__":
    
    n = int(input('Enter the number of discs on Start Tower initially : '))
    A = input('Enter the name of start disc : ')
    B = input('Enter the name of end disc : ')
    C = input('Enter the name of intermediate disc : ')
    
    # print('Recursive Method:-')
    # recursive_toh(n,A,B,C)
    print('Non-Recursive Method:-')
    A = createStack(n)
    B = createStack(n)
    C = createStack(n)
    nonrecursive_toh(n,A,B,C)