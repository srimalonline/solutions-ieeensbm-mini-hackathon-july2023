T = int(input())

for t in range(T):
    n = int(input())
    L = [int(a) for a in input().split()]
    
    cost = 0
    
    for i in range(n-1):
        j = L.index(min(L[i:]))
        cost += j-i+1
        L[i:j+1] = reversed(L[i:j+1])
    print(cost)