# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 21:50:29 2018

@author: Achraf Baiz
"""


    
    
# fn+2 = fn + fn+1

def fibo(nbriter):
    cpt,fn,fnone,fntwo = 0,0,1,0   
    l = list()
    while cpt!=nbriter:
        if(fntwo == 0):
            print(0)
        fntwo = fn +fnone
        print (fnone,fntwo)
        l.append(fnone);l.append(fntwo)
        fn,fnone,cpt = fn+fnone,fnone+fntwo, cpt +1
    return l[:nbriter]

def pyramid(n):
    n= int(n)
    for i in range(1,n+2):
        m =''.join([esp for esp in [" " for v in range((n+1)-i)]])
        print(m,end='',flush=True)
        for j in range(1,i):
            print(j,end='',flush=True)
        for j in range(1,i):
            if i-j-1==0:
                continue
            print(i-j-1,end='',flush=True)
        print("\n")
