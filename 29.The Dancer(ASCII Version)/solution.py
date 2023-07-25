# 0 - Normal/Out Position
# 1 - Hip/In Position
# 2 - Head Position

def drawASCIIMan(right_hand, left_hand, right_leg, left_leg, is_turned):
    man=[
        [' ', 'o', ' '],
        [' ', '|', ' '],
        [' ', ' ', ' ']
        ];
    if is_turned:
        # Hand swap
        temp = left_hand
        left_hand = right_hand
        right_hand = temp
        # Leg swap
        temp = left_leg
        left_leg = right_leg
        right_leg = temp
    
    # Right hand position
    if right_hand==0:
        man[1][0]='/'
    elif right_hand==1:
        man[1][0]='<'
    elif right_hand==2:
        man[0][0]='('
    # Left hand position
    if left_hand==0:
        man[1][2]='\\'
    elif left_hand==1:
        man[1][2]='>'
    elif left_hand==2:
        man[0][2]=')'
    # Right leg position
    if right_leg==0:
        man[2][0]='/'
    elif right_leg==1:
        man[2][0]='<'
    # Left leg position
    if left_leg==0:
        man[2][2]='\\'
    elif left_leg==1:
        man[2][2]='>'
    
    # Printing ASCII Man
    for i in range(3):
        for j in range(3):
            print(man[i][j], end="")
        print("")
    
    
    
T = int(input())
for tc in range(T):
    d = int(input())
    turn_status=False
    left_hand_status = 0
    right_hand_status = 0
    left_leg_status = 0
    right_leg_status = 0
    for ncom in range(d):
        command = input()
        if command[:3]=="say":
            print(command[4:])
        elif command[:4]=="turn":
            turn_status= not turn_status
            drawASCIIMan(right_hand_status, left_hand_status, right_leg_status, left_leg_status, turn_status)
        elif command[:4]=="left" or command[:5]=="right":
            if command[:4]=="left":
                if command[5:9]=="hand":
                    if command[13:]=="start": left_hand_status = 0
                    if command[13:]=="hip": left_hand_status = 1
                    if command[13:]=="head": left_hand_status = 2
                elif command[5:8]=="leg":
                    if command[9:]=="out": left_leg_status = 0
                    if command[9:]=="in": left_leg_status = 1
            elif command[:5]=="right":
                if command[6:10]=="hand":
                    if command[14:]=="start": right_hand_status = 0 
                    if command[14:]=="hip": right_hand_status = 1 
                    if command[14:]=="head": right_hand_status = 2 
                elif command[6:9]=="leg":
                    if command[10:]=="out": right_leg_status = 0 
                    if command[10:]=="in": right_leg_status = 1 
            drawASCIIMan(right_hand_status, left_hand_status, right_leg_status, left_leg_status, turn_status)