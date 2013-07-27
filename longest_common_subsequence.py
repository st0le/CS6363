import random

def random_array(sz,lo=10,hi=100):
    return map(lambda _:random.randint(lo,hi),xrange(sz))


A = random_array(random.randint(10,20),1,10)
B = random_array(random.randint(10,20),1,10)

def lcs(A,B):
    m = [[0] * (len(B) +  1) for i in xrange(len(A) + 1) ]
    for i in xrange(len(A) + 1): m[i][0] = 0
    for i in xrange(len(B) + 1): m[0][i] = 0
    for i in xrange(1,len(A)+1):
        for j in xrange(1,len(B)+1):
            m[i][j] = 1 + m[i-1][j-1] if A[i-1] == B[j-1] else max(m[i-1][j],m[i][j-1])
    
    l = []
    i = len(A)
    j = len(B)
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            l.append(A[i - 1])
            i -= 1
            j -= 1
        elif m[i-1][j] > m[i][j-1]:
            i -= 1
        else:
            j -= 1
    l.reverse()
    return m[len(A)][len(B)],l

print A
print B
print lcs(A,B)