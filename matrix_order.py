p = [5,10,3,12,5,50,6]
p = [40,20,30,10,30]
def matrix_order(p):
    N = len(p)
    m = [[0] * N for i in xrange(N)]
    s = [[0] * N for i in xrange(N)]
    
    for l in xrange(1,N):
        for i in xrange(1,N - l):
            j = i + l
            m[i][j] = float('inf')
            for k in xrange(i, j):
                c = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                if m[i][j] > c:
                    m[i][j] = c
                    s[i][j] = k
    
    def backtrack(i,j):
        if i == j :
            return "A" + str(i)
        else:
            return "(" + backtrack(i,s[i][j]) + " x " + backtrack(s[i][j] + 1,j) + ")"
    print backtrack(1,N-1)
    
    
    
    return m[1][N-1]
print p
print matrix_order(p)