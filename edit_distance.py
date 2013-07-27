A = "shop"
B = "stop"

def edit_distance(A,B):
    m = [[0] * (len(B)+1) for i in xrange(len(A)+1)]
    for i in xrange(len(A)+1): m[i][0] = i
    for i in xrange(len(B)+1): m[0][i] = i
    
    for i in xrange(1,1 + len(A)):
        for j in xrange(1,1 + len(B)):
            if A[i - 1] == B[j - 1]:
                m[i][j] = 1 + min(m[i-1][j],m[i][j-1],m[i-1][j-1] - 1)
            else:
                m[i][j] = 1 + min(m[i-1][j],m[i][j-1],m[i-1][j-1])
    print m
    return m[len(A)][len(B)]
    
print edit_distance(A,B)
    
