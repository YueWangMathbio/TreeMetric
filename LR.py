# -*- coding: utf-8 -*-
"""
This code computes the left-regular metric D_LR for two rooted unordered trees
with possibly repeated labels. This metric is defined in my paper
https://arxiv.org/abs/2103.11553

This code is tested on different trees in my paper.

For the function LR(n,T1,T2), input n is the tree depth, and inputs T1,T2
are the two trees that we want to calculate the left-regular metric.  
T1 and T2 should be perfect binary trees with depth n. If not, add null
children vertices with label 'n' to verticies with depth <n and have 
less than two children. 
The trees are recorded by their labels, in the order of depth-first search.
For example, consider a tree T="abcdefg" with depth 3. 
It means the root has label 'a'; two children of 'a' are 'b' and 'e'; 
two children of 'b' are 'c' and 'd'; two children of 'e' are 'f' and 'g'.

@author: Yue Wang
"""

def d(T1,T2): # calculate the ordered-tree distance D_OT for two trees
    counter=0
    m=len(T1)
    for x in range(0, m):
        if T1[x]!=T2[x]:
            counter=counter+1
    return counter

def compare(T1,T2): # compare the label strings for two trees
# ind<=0 means T1<=T2; ind>0 means T1>T2
    ind=0
    m=len(T1)
    for x in range(0, m):
        if T1[x]<T2[x]:
            ind=-1
            break
        elif T1[x]>T2[x]:
            ind=1
            break
    return ind
            
def transform(n,T): # replace alphabetical labels by number labels
# n is the depth of the tree T
# this assigns a total order on the label set
    m=2**n-1    
    newT=[]
    for x in range(0, m):
        if T[x]=='z':
            newT.append(1)
        elif T[x]=='y':
            newT.append(2)
        elif T[x]=='x':
            newT.append(3)
        elif T[x]=='w':
            newT.append(4)
        elif T[x]=='s':
            newT.append(5)
        elif T[x]=='n':
            newT.append(6)
    return newT

def regular(n,T): # transform a tree into its left-regular form
# n is the depth of the tree T
    if n==1:
        return T[:] # a tree of depth 1 is already left-regularized
    else:
        newT=[]
        m=2**(n-1)-1 
        TL=regular(n-1,T[1:m+1])
        TR=regular(n-1,T[m+1:2*m+1]) 
        # left-regularize both subtrees of the root
        # the left-regularization is implemented recursively
        newT.append(T[0])
        if compare(TL,TR)>0:
            newT[1:m+1]=TR[:]
            newT[m+1:2*m+1]=TL[:]
        else:
            newT[1:m+1]=TL[:]
            newT[m+1:2*m+1]=TR[:]
        return newT
    # assemble the root and the two subtrees
    
def LR(n,T1,T2): # calculate the D_LR: left-regularize two trees
# then calculate the D_OT
# n is the depth of the trees T1, T2
    T1=transform(n,T1)
    T1=regular(n,T1)
    T2=transform(n,T2)
    T2=regular(n,T2)
    return d(T1,T2)
            

# test for different examples
T1="xxxyxxy"
T2="yyxyyxy"
T3="zzxxzyy"
print('D_LR(T1,T2)=',LR(3,T1,T2))
print('D_LR(T1,T3)=',LR(3,T1,T3))
print('D_LR(T2,T3)=',LR(3,T2,T3))
print('')

T4="xxxnnnn"
T5="xyynnnn"
T6="xzzzzzz"
print('D_LR(T4,T5)=',LR(3,T4,T5))
print('D_LR(T4,T6)=',LR(3,T4,T6))
print('D_LR(T5,T6)=',LR(3,T5,T6))
print('')

T7="zxnnnnnnnnnnnnnnyzxnnynnnnnnnnn"
T8="zxnnnnnnnnnnnnnnyzxnnznnnnnnnnn"
T9="xynnnnnnnnnnnnnnzxxnnxnnnnnnnnn"
T10="zznnnnnnnnnnnnnnyzxnnynnnnnnnnn"
T11="xnnnnnnnnnnnnnnnzxnnnnnnyzxynnn"

print('D_LR(T7,T8)=',LR(5,T7,T8))
print('D_LR(T7,T9)=',LR(5,T7,T9))
print('D_LR(T7,T10)=',LR(5,T7,T10))
print('D_LR(T7,T11)=',LR(5,T7,T11))
print('D_LR(T8,T9)=',LR(5,T8,T9))
print('D_LR(T8,T10)=',LR(5,T8,T10))
print('D_LR(T8,T11)=',LR(5,T8,T11))
print('D_LR(T9,T10)=',LR(5,T9,T10))
print('D_LR(T9,T11)=',LR(5,T9,T11))
print('D_LR(T10,T11)=',LR(5,T10,T11))
print('')

TA="wxwwwwwwzzsszzz"
TS="xxwxxwxxxwwwwww"
print('D_LR(TA,TS)=',LR(4,TA,TS))