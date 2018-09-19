# -*- coding: utf-8 -*-
"""
Created on Wed Sept 18 21:50:29 2018
@author: Achraf Baiz

This algorithm try to search in the different levels of the builed tree to find the appropriate set of weigths that will be equal or closest to the bag weight
without going greater than it;
Our tree of sets combination is made bu using lists, eash element of it is a level of the tree, and each level is a number of combination sets.

example 

    - items   = {60, 100, 120}
     respective
    - weights = {10, 20, 30}
     bag maximum size 
    - w       =  50
     
                    {10 , 20 , 30}=60                                   LEVEL 1
       --------------------------------------------
     {10 , 20}=30         {10 , 30}=40        {20 , 30}=50              LEVEL 2
       --------------------------------------------
        {10}=10              {20}=20                {30}=30             LEVEL 3
     
     folowing the rules, the best set would be {20,30} = 50 (w = 50) which means the respective items {100,120} = 220  

""" 

def combination(list,n,r):
    tab    = []
    list.sort()
    c = factorial(n)/(factorial(r)*factorial(n-r))
    while(True):
        weights = [random.choice(list) for k in range(r)]
        weights.sort()
        if(len(set(weights))==r and (weights not in tab)):
            tab.append(weights)
            if(len(tab) == int(c)):
                break
    return tab

def closest(list,x):
    close = 0
    for w in list:
       if(w>=close and w <= x):
            close = w
    return close


def knapsacke(N,WS,W):
    levels  = []
    weigths = []
    values  = []
    temp    = []
    sums    = []
    for i in range(1, len(WS) + 1):             # i represente the step level of the graph tree
        levels.append(combination(WS,len(WS),i))
    for i in range(1,len(levels)+1):
        print("++++++++++", levels[i-1], "++++++++++")
        temp.append(([sum(slot) for slot in levels[i-1]],i))
    sums = dict([(level[1],closest(level[0],W)) for level in temp])
    max_,niv=max(sums.values()),list(filter(lambda x : sums.get(x) if sums.get(x)==max(sums.values()) else None,sums.keys()))[0]
    weigths.append(levels[niv-1][temp[niv-1][0].index(max_)])
    values.extend([N[WS.index(w)] for w in weigths[0]])
    return weigths.pop(0),values


if __name__ == "__main__":

    N=[60,100,120,140]
    WS=[10,20,30,45]
    W=107

    print("|Weight/s               -               Value/s|",knapsacke(N,WS,W), sep="\n",flush=True)
