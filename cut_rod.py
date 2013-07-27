

def cut_rod(L,P):
    N = len(P)
    m = [0] * (L+1)
    pi = [0] * (L+1)
    for i in xrange(1,L+1):
        S = [m[i-j] + P[j] for j in xrange(min(i+1,len(P)))]
        maxIndex = max(xrange(len(S)),key=S.__getitem__)
        m[i] = S[maxIndex]
        pi[i] = maxIndex
    pieces = []
    while L > 0:    
        pieces.append(pi[L])
        L = L - pi[L]
    return m[-1],pieces

P = [0,1,5,8,9,10,17,17,20,24,30]
print cut_rod(300,P)    
