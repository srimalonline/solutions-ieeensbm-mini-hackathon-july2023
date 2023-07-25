T = int(input())

for t in range(T):
    X, Y, S = input().split()
    X, Y = [int(X), int(Y)]
    S = list(S)
    S.append(0)
    cost = 0
    for i in range(len(S)-1):
        if S[i] == "?":
            S[i] = S[i-1]
        else:
            if i==0:
                continue
            if S[i]=="C" and S[i-1]=="J":
                cost+=Y
            elif S[i]=="J" and S[i-1]=="C":
                cost+=X
    print(cost)