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
    if (x >= max(list)):
        if (x == max(list)):
            return x
        elif (x > max(list)):
            return 0
    for w in list:
       if(w>close and w <= x):
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
        print("++++++++++", levels[i-1])
        temp.append(([sum(slot) for slot in levels[i-1]],i))
    sums = dict([(level[1],closest(level[0],W)) for level in temp])
    print(sums)
    max_,niv=max(sums.values()),list(filter(lambda x : sums.get(x) if sums.get(x)==max(sums.values()) else None,sums.keys()))[0]
    weigths.append(levels[niv-1][temp[niv-1][0].index(max_)])
    values.extend([N[WS.index(w)] for w in weigths[0]])
    return weigths.pop(0),values

if __name__ == "__main__":

    N=[60,100,120,140]
    WS=[10,20,30,45]
    W=73
    print(knapsacke(N,WS,W), sep="\n",flush=True)
