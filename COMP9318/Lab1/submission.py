## import modules here 

################# Question 0 #################

def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x): # do not change the heading of the function
    import math
    low,high,ans = 0, x, 0
    counter = 1
    if(x==1):
        return (x) 
    while(low <= high):
        counter += 1
        mid = (low + high)//2
        if(mid * mid <= x and (mid+1)*(mid+1) > x):
            return(mid)
        elif(mid * mid > x):
            high = mid
        else:
            low = mid


################# Question 2 #################


# x_0: initial guess
# EPSILON: stop when abs(x - x_new) < EPSILON
# MAX_ITER: maximum number of iterations

## NOTE: you must use the default values of the above parameters, do not change them

def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    #implement newtone's method
    counter = 0
    while(counter < MAX_ITER):
        counter+=1
        x_new = x_0
        x_0 = x_0 - f(x_0)/fprime(x_0)
        if(abs(x_0 - x_new) < EPSILON):
            return x_0
    return x_0



################# Question 3 #################

class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)


def make_tree(tokens): # do not change the heading of the function
    t = Tree(tokens[0])
    parent = t
    child = t
    buff = []
    for i in tokens[1:]:
        if(i == '['):
            buff.append(parent)
            parent = child

        elif(i == ']'):
            parent = buff.pop()

        else:
            child = Tree(i)
            parent.add_child(child)
    return t 

def max_depth(root): # do not change the heading of the function
    if(root.children == []):
        return 1
    result = 1
    for i in root.children:
        h = 1 + max_depth(i)
        if(h > result):
            result = h
    return result






