s = input()

# Solution code
count = 0
user_inputs = [int(s[i]) for i in range(len(s))]
cfi = 0 # Continue From Index
number = -1

while number!=user_inputs[cfi]:
    number = user_inputs[cfi]
    for i in range (cfi, len(user_inputs)):
        if user_inputs[cfi] != user_inputs[i]:
            cfi=i
            break
        count += 1 
    print((count, number), end=" ")
    count=0
# Solution code