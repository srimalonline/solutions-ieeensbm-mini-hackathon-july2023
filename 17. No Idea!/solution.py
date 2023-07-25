NM = input().split()
Z = input().split()
A = set(input().split())
B = set(input().split())

h = 0

for i in Z:
    if i in A:
        h+=1
    if i in B:
        h-=1
print(h)