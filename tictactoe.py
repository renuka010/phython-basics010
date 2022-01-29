def mark(lst,position,player):
    print('TIC TAC TOE'.center(30))
    lst[position-1]=player
    print(" -----------------------                                    |1|2|3|")
    print("|       |       |       |                                   |4|5|6|")
    print(f"|   {lst[0]}   |   {lst[1]}   |   {lst[2]}   |                                   |7|8|9|")
    print("|       |       |       |")
    print(" -----------------------")
    print("|       |       |       |")
    print(f"|   {lst[3]}   |   {lst[4]}   |   {lst[5]}   |")
    print("|       |       |       |")
    print(" -----------------------")
    print("|       |       |       |")
    print(f"|   {lst[6]}   |   {lst[7]}   |   {lst[8]}   |")
    print("|       |       |       |")
    print(" -----------------------")
    return lst

def play(lst,player_no):
    position=11
    
    #getting a position to mark from player
    while(position not in range(1,10) or lst[position-1]!=' '):
        position=input(f'Player{player_no}, Please enter a position to mark (1-9): ')
        if position.isdigit():
            position=int(position)
            if position not in range(1,10):
                print('Please enter a number from 1 to 9')
            elif lst[position-1]!=' ':
                print('Please enter a position that is not marked already')
        else:
            print('Please enter a number ')
    
    #returning position
    return position
    clear_output()

def print_header():
    print('TIC TAC TOE'.center(30))
    print(" -----------------------")
    print("|       |       |       |")
    print("|   1   |   2   |   3   |")
    print("|       |       |       |")
    print(" -----------------------")
    print("|       |       |       |")
    print("|   4   |   5   |   6   |")
    print("|       |       |       |")
    print(" -----------------------")
    print("|       |       |       |")
    print("|   7   |   8   |   9   |")
    print("|       |       |       |")
    print(" -----------------------")

def check(lst):
    if (lst[0]==lst[4]==lst[8] or lst[2]==lst[4]==lst[6]) and lst[4]!=' ':
        return True
    for position in [0,1,2]:
        if(lst[position]==lst[3+position]==lst[6+position] and lst[position]!=' '):
            return True
    for position in [0,3,6]:
        if(lst[position]==lst[1+position]==lst[2+position] and lst[position]!=' '):
            return True
    return False

choice='n'
while choice in ['n','N']:
    print_header()
    lst=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1 = ''
    while player1 not in ['X','O']:
        player1 = input('Please select a token (X or O): ')
        if player1 == 'X':
            player2 = "O"
        else:
            player2 ="X"
    
    Winner=''
    while Winner not in['Player1','Player2','DRAW']:
        position=play(lst,1)
        lst=mark(lst,position,player1)
        if check(lst):
            Winner='Player1'
        Draw=0
        for i in range(0,9):
            if lst[i]==' ':
                Draw+=1
        if Draw==0 and Winner!='Player1':
            Winner='DRAW'
        if Winner not in['Player1','Player2','DRAW']:
            position=play(lst,2)
            lst=mark(lst,position,player2)
            if check(lst):
                Winner='Player2'
    if Winner=='Player1':
        print("CONGRATULATIONS!!! PLAYER1 WON XD")
    elif Winner=='Player2':
        print("CONGRATULATIONS!!! PLAYER2 WON XD")
    else:
        print('THE GAME IS A DRAW :|')
    choice=''
    while choice not in ['Y','y','n','N']:
        choice = input('Do you want to exit? (Y/N): ')