# -*- coding: utf-8 -*-
"""
This code computes the best-match metric for two rooted unordered trees
with possibly repeated labels. This metric is defined in my paper
https://arxiv.org/abs/2103.11553

This code is tested on different trees in my paper.

For the function BM(n,T1,T2), input n is the tree depth, and inputs T1,T2
are the two trees that we want to calculate the best-match metric.  
T1 and T2 should be perfect binary trees with depth n. If not, add null
children vertices with label 'n' to verticies with depth <n and have 
less than two children. 
The trees are recorded by their labels, in the order of depth-first search.
For example, consider a tree T="abcdefg" with depth 3. 
It means the root has label 'a'; two children of 'a' are 'b' and 'e'; 
two children of 'b' are 'c' and 'd'; two children of 'e' are 'f' and 'g'.

@author: Yue Wang
"""


def d(T1,T2): # calculate the distance between two trees with depth 1
    if T1==T2:
        return 0
    else:
        return 1

def BM(n,T1,T2): 
    # calculate the best-match metric D_BM for two trees with depth n
    if n==1:
        return d(T1,T2) # if depth is 1, directly use the d function
    else:
        m=2**(n-1)-1 # number of vertices in each tree
        r1=d(T1[0],T2[0])+BM(n-1,T1[1:m+1],T2[m+1:m*2+1])\
        +BM(n-1,T1[m+1:m*2+1],T2[1:m+1]) # distance for one possible match
        r2=d(T1[0],T2[0])+BM(n-1,T1[1:m+1],T2[1:m+1])\
        +BM(n-1,T1[m+1:m*2+1],T2[m+1:m*2+1]) 
        # distance for another possible match
        return min(r1,r2) # the match with the smaller distance is chosen
    # and this is D_BM
    
    # recursively find the best match


# test for different examples
T1="xxxyxxy"
T2="yyxyyxy"
T3="zzxxzyy"
print('D_BM(T1,T2)=',BM(3,T1,T2))
print('D_BM(T1,T3)=',BM(3,T1,T3))
print('D_BM(T2,T3)=',BM(3,T2,T3))
print('')

T4="xxxnnnn"
T5="xyynnnn"
T6="xzzzzzz"
print('D_BM(T4,T5)=',BM(3,T4,T5))
print('D_BM(T4,T6)=',BM(3,T4,T6))
print('D_BM(T5,T6)=',BM(3,T5,T6))
print('')

T7="zxnnnnnnnnnnnnnnyzxnnynnnnnnnnn"
T8="zxnnnnnnnnnnnnnnyzxnnznnnnnnnnn"
T9="xynnnnnnnnnnnnnnzxxnnxnnnnnnnnn"
T10="zznnnnnnnnnnnnnnyzxnnynnnnnnnnn"
T11="xnnnnnnnnnnnnnnnzxnnnnnnyzxynnn"

print('D_BM(T7,T8)=',BM(5,T7,T8))
print('D_BM(T7,T9)=',BM(5,T7,T9))
print('D_BM(T7,T10)=',BM(5,T7,T10))
print('D_BM(T7,T11)=',BM(5,T7,T11))
print('D_BM(T8,T9)=',BM(5,T8,T9))
print('D_BM(T8,T10)=',BM(5,T8,T10))
print('D_BM(T8,T11)=',BM(5,T8,T11))
print('D_BM(T9,T10)=',BM(5,T9,T10))
print('D_BM(T9,T11)=',BM(5,T9,T11))
print('D_BM(T10,T11)=',BM(5,T10,T11))
print('')

TA="wxwwwwwwzzsszzz"
TS="xxwxxwxxxwwwwww"
print('D_BM(TA,TS)=',BM(4,TA,TS))


