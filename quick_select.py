import random

def random_array(sz,lo = 10, hi = 100):
    return [random.randint(lo,hi) for i in xrange(sz)]


def quick_select(A,k):
    N = len(A)
    pivot = random.randint(0,N - 1)
    
    A[pivot],A[0] = A[0],A[pivot]
    left = 1
    right = N - 1
    while left < right:
        while left < N and A[left] <= A[0] : left = left + 1
        while right >= 0 and A[right] > A[0]: right = right - 1
        if left < right:
            A[left],A[right] = A[right],A[left]
    if A[0] > A[right]:
        A[0],A[right] = A[right],A[0]
    if k == right:
        return A[k]
    elif k > right:
        return quick_select(A[right+1:],k - right - 1)
    else:
        return quick_select(A[:right],k)

def quick_select2(A,k):
    lb = 0
    ub = len(A)
    while ub - lb >= 1:
        #partition
        pivot = random.randint(lb,ub - 1)
        #print A[lb:ub],A[pivot],k
        A[pivot],A[lb] = A[lb],A[pivot]
        left,right = lb + 1, ub - 1
        while left < right:
            while left < right and A[left] <= A[lb]: left = left + 1
            while right >= lb and A[right] > A[lb]: right = right - 1
            if left < right:
                A[left],A[right] = A[right],A[left]
        if A[lb] > A[right]:
            A[lb],A[right] = A[right],A[lb]
        
        if lb + k == right :
            return A[right]
        elif lb + k > right :
            k = k - (right - lb) - 1
            lb = right + 1
        else:
            ub = right
    return None


R = random_array(10)
k = random.randint(0,len(R) - 1)
print R,k
print sorted(R)[k]
print quick_select(R,k)
print quick_select2(R,k)