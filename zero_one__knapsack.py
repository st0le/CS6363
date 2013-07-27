import random

def random_array(sz,lo=10,hi=100):
    return map(lambda _:random.randint(lo,hi),xrange(sz))


N = 10
P = [10,40,30,50]
W = [5,4,6,3]

def zeroKS(w,p,W):
    m = [[0]*(W+1) for i in xrange(len(w)+1)]
    for i in xrange(1,len(w) + 1):
        for j in xrange(W+1):
            if j < w[i - 1]:
                m[i][j] = m[i-1][j]
            else:
                m[i][j] = max(m[i-1][j],m[i-1][j - w[i - 1]] + p[i - 1])    

    i = len(w)
    j = W
    ks = []
    while i > 0:
        if m[i-1][j] != m[i][j]:
            ks.append(i-1)
            j -= w[i - 1]
        i -= 1
    
    return m[len(w)][W],ks

print P
print W
print zeroKS(W,P,10)
    
        
    
    
    
