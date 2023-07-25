def minion_game(string):
    # Solution Code
    s_points = 0
    k_points = 0
    vowels = 'AEIOU'
    for i in range(len(string)):
        points = len(string)-i
        if string[i] in vowels:
            k_points += points
        else:
            s_points +=points
            
    if k_points > s_points:
        print(f'Kevin {k_points}')
    elif k_points < s_points:
        print(f'Stuart {s_points}')
    else:
        print(f'Draw')
    # Solution Code

if __name__ == '__main__':
    s = input()
    minion_game(s)