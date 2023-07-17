def print_formatted(number):
    # Solution Code
    space = len(bin(number)[2:])+1
    for i in range(1, number+1):
        baseList = [i, oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]]
        print(f"{baseList[0]:>{space-1}}{baseList[1]:>{space}}{baseList[2]:>{space}}{baseList[3]:>{space}}")
    # Solution Code

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)