import sys
def winx(tick):
    if (tick [0] == ['    X    ','|','    X    ','|','    X    '] or tick [2] == ['    X    ','|','    X    ','|','    X    '] or tick [4] == ['    X    ','|','    X    ','|','    X    ']):
        print('Player 1 wins') # horizontal check
        sys.exit()
    elif ((tick[0][0] == '    X    'and tick [2][0] == '    X    'and tick[4][0] == '    X    ') or (tick[0][2]== '    X    ' and tick [2][2] == '    X    'and tick[4][2] == '    X    ') or (tick[0][4] == '    X    'and tick [2][4] == '    X    'and tick[4][4] == '    X    ')):
        print('Player 1 wins')  # column check
        sys.exit()
    elif ((tick[0][0] == '    X    'and tick [2][2] == '    X    'and tick[4][4] == '    X    ') or (tick[0][4] == '    X    'and tick [2][2] == '    X    'and tick[4][0] == '    X    ')):
        print('Player 1 wins')   # diagonal check
        sys.exit()
    else :
        pass
def wino(tick):
    if (tick [0] == ['    O    ','|','    O    ','|','    O    '] or tick [2] == ['    O    ','|','    O    ','|','     O   '] or tick [4] == ['    O    ','|','    O    ','|','    O    ']):
        print('Player 2 wins')  # horizontal check
        sys.exit()
    elif ((tick[0][0] == '    O    'and tick [2][0] == '    O    'and tick[4][0] == '    O    ') or (tick[0][2]== '    O    ' and tick [2][2] == '    O    'and tick[4][2] == '    O    ') or (tick[0][4] == '    O    'and tick [2][4] == '    O    'and tick[4][4] == '    O    ')):
        print('Player 2 wins')  # column check
        sys.exit()
    elif ((tick[0][0] == '    O    'and tick [2][2] == '    O    'and tick[4][4] == '    O    ') or (tick[0][4] == '    O    'and tick [2][2] == '    O    'and tick[4][0] == '    O    ')):
        print('Player 2 wins')   # diagonal check
        sys.exit()
    else :
        pass
print("Lets play tick tack toe")
print()
tick=[['    1    ','|','    2    ','|','    3    '],['-----------------------------'],['    4    ','|','    5    ','|','    6    '],['-----------------------------'],['    7    ','|','    8    ','|','    9    ']]
pos={1:0,2:2,3:4,4:0,5:2,6:4,7:0,8:2,9:4}
for i in range(0,5):
	for j in range(0,len(tick[i])):
		print(tick[i][j],end="")
	print()
count =0
val = {1 : 'X' , 2 : 'O'} 
index=list()
z=1
while count <4:
    print("Player-",z)
    inp=int(input("Enter the index of the box where you want to enter: "))
    if(inp not in index):
        count+=1
        index.append(inp)
        if inp <= 3:
            i=0
            tick[i][pos[inp]]="    "+val[z]+"    "
        elif inp <= 6:
            i=2
            tick[i][pos[inp]]="    "+val[z]+"    "
        else:
            i=4
            tick[i][pos[inp]]="    "+val[z]+"    "
        for i in range(0,5):
            for j in range(0,len(tick[i])):
                print(tick[i][j],end="")
            print()
        z=3-z
    else:
        print('index',inp,'is non empty')
        continue
while count <9:
    print("Player-",z)
    inp=int(input("Enter the index of the box where you want to enter: "))
    if(inp not in index):
        count+=1
        index.append(inp)
        if inp <= 3:
            i=0
            tick[i][pos[inp]]="    "+val[z]+"    "
        elif inp <= 6:
            i=2
            tick[i][pos[inp]]="    "+val[z]+"    "
        else:
            i=4
            tick[i][pos[inp]]="    "+val[z]+"    "
        for i in range(0,5):
            for j in range(0,len(tick[i])):
                print(tick[i][j],end="")
            print()
        z=3-z
        winx(tick)
        wino(tick)
    else:
        print('index',inp,'is non empty')
        continue
print('This game is a tie')