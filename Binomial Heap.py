#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Creating a Heap

# Creating Node Class
class Node:
    def __init__(self, key):
        self.key = key;
        self.p = None;
        self.degree = 0;
        self.child = None;
        self.sibbling = None;
        
# Initialize Tree
class init_Tree:
    def __init__(self):
        self.Head = None;

#MAKE_HEAP
def MAKE_HEAP():
    H = init_Tree();
    return H;

#HEAP INSERT
def HEAP_INSERT(H, x):
    x_node = Node(x);
    H_tmp = MAKE_HEAP();
    H_tmp.Head = x_node;
    if H.Head == None:
        return [H_tmp, x_node];
    else:
        H = HEAP_UNION(H, H_tmp);   
        return [H, x_node];

#MINIMUM OF ROOTS
def MIN(H):  
    y = None;
    x = H.Head;
    min = 100000000;
    while x != None:
        if x.key < min:
            min = x.key;
            y = x;
        x = x.sibbling;
    return y;

# FIND PREVIOUS SIBBLING OF NODE
def FIND(H, x):
    tmp = H.Head;
    y = tmp;
    while tmp!= None:
        if tmp == x:
            if tmp == y:
                return None;
            else:
                return y;
        y = tmp;
        tmp = tmp.sibbling;

# Binomial Linkage
def HEAP_LINK(y, z):
    y.p = z;
    y.sibbling = z.child;
    z.child = y;
    z.degree = z.degree + 1;

#MERGE LISTS TOGETHER
def MERGE(H1, H2):
    x = H1.Head;
    y = H2.Head;
    H.Head = x;
    while x != None and y != None:
        if x.degree == y.degree:
            tmp_1 = x.sibbling;
            tmp_2 = y.sibbling;
            x.sibbling = y;
            y.sibbling = tmp_1;
            x = tmp_1;
            y = tmp_2;
        else:
            if x.degree <= y.degree:
                tmp_1 = x.sibbling;
                tmp_2 = y.sibbling;
                x.sibbling = y;
                y.sibbling = tmp_1;
                x = tmp_1;
            elif x.degree > y.degree:
                tmp_1 = x.sibbling;
                tmp_2 = y.sibbling;
                tmp_node = FIND(H1, x);
                if tmp_node != None:
                    tmp_node.sibbling = y;
                    y.sibbling = x;
                else:
                    H.Head = y;
                    y.sibbling = x;
                x.sibbling = tmp_2;
                y = tmp_2;
    return H.Head;

# UNION OF TWO HEAPS
def HEAP_UNION(H1, H2):
    H = MAKE_HEAP();
    H.Head = MERGE(H1, H2);
    if H.Head == None:
        return H;
    else:
        prev_x = None;
        x = H.Head;
        next_x = x.sibbling;
        while next_x != None:
            if (x.degree != next_x.degree) or (next_x.sibbling != None and next_x.sibbling.degree == x.degree):
                prev_x = x;
                x = next_x;
                next_x = x.sibbling;
            elif (x.degree == next_x.degree) and (x.key <= next_x.key):
                x.sibbling = next_x.sibbling;
                HEAP_LINK(next_x, x);
                if x.sibbling != None:
                    next_x = x.sibbling;
                else:
                    next_x = None;
            elif (x.degree == next_x.degree) and (x.key > next_x.key):
                if prev_x == None:
                    H.Head = next_x;
                else:
                    prev_x.sibbling = next_x;
                HEAP_LINK(x, next_x);
                x = next_x;
                if x.sibbling != None:
                    next_x = x.sibbling;
                else:
                    next_x = None;            
    return H;

#DEC KEY - VERIFIED LOGIC
def DEC_KEY(H, x, k):
    if k > x.key:
        return 0;
    else:
        x.key = k;
        y = x;
        z = y.p;
        while z != None and y.key < z.key:
            tmp = y.key;
            y.key = z.key;
            z.key = tmp;
    return H;

#EXTRACT_MIN - VERIFIED LOGIC
def EXTRACT_MIN(H):
    min_node = MIN(H);
    min_prev = FIND(H, min_node);
    if min_prev != None:
        min_prev.sibbling = min_node.sibbling;
    else:
        H.Head = min_node.sibbling;
    H_tmp = MAKE_HEAP();
    
    child = min_node.child;
    y = child;
    if child != None and child.sibbling != None:
        tmp = child.sibbling;
        child.sibbling = None;
    else:
        tmp = None;
    child = tmp;
    
    while (child != None):
        tmp = child.sibbling;
        child.sibbling = y;
        y = child;
        child = tmp;
    H_tmp.Head = y;

    if H.Head == None:
        return [H_tmp, min_node];
    else:
        H = HEAP_UNION(H, H_tmp);   
        return [H, min_node];

#HEAP DELETE NODE  - VERIFIED LOGIC
def HEAP_DELETE(H, x):
    H = DEC_KEY(H, x, -1928237193);
    temp = EXTRACT_MIN(H);
    H = temp[0]; 
    n = temp[1]; 
    return H;

#PRINTING ROOT LIST OF HEAP
def PRINT_HEAP(H):
    print("Printing Root List \n");
    n = H.Head;
    if n == None:
        print ("HEAP EMPTY!")
    while n != None:
        print ("Printing Parent");
        print (n.key);
        x = n.child;
        while x != None:
            print ("Child");
            print (x);
            print (x.key);            
            if x != None:
                b = x.child;
                while b != None:
                    print ("Child's child");
                    print (b);
                    print (b.key);
                    b = b.sibbling;
            x = x.sibbling;
        n = n.sibbling; 

