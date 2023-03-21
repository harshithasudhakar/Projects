
""" TermTables - This library is used to draw the grid """
import termtables
""" DateTime - This library is used to calculate the time taken for the game to complete """
import datetime
""" Emoji - This library is used to print emojis """
import emoji

""" Prints the grid """
def print_grid(gridr1,gridr2,gridr3):
    tblheader=[["E - TIC TAC TOE"]]
    termtables.print(tblheader)
    header = [" ", "0", "1", "2"]
    data = [
        [0, gridr1[0], gridr1[1], gridr1[2]],
        [1, gridr2[0], gridr2[1], gridr2[2]],
        [2, gridr3[0], gridr3[1], gridr3[2]],
    ]
    termtables.print(data, header=header,  style=termtables.styles.double)

    

def input_values(player):
    i=0
    while True:
        #print("===============================================")
        i= int(input("Player " + str(player) + ", Please enter your row position : "))
        #print("===============================================")
        if (i<0) or (i>2):
            print(f'Row number {i} is invalid. Select again!!\n')
            continue    
        else :
            break

    j=0
    while True:
        #print("===============================================")
        j= int(input("Player " + str(player) + ", Please enter your column position : "))
        #print("===============================================")
        if (j<0) or (j>2):
            print(f'Column number {j} is invalid. Select again!!\n')
            continue
        if i==0 and  (gridr1[j]=='X' or gridr1[j]=='O'):
            print("Coordinates already taken. Input different coordinates\n")
            return False;
        if i==1 and  (gridr2[j]=='X' or gridr2[j]=='O'):
            print("Coordinates already taken. Input different coordinates\n")
            return False;
        if i==2 and  (gridr3[j]=='X' or gridr3[j]=='O'):
            print("Coordinates already taken. Input different coordinates\n")
            return False;
        else :
             break
            
    #Write move of the player to file
    file.write("Player " + str(player) + ": [" + str(i) + "," + str(j) + "]\n")

    #Mark the grid
    if i==0:
        if (player==1):            
            gridr1[j]='X'
        else:
            gridr1[j]='O'
    if i==1:
        if (player==1):
            gridr2[j]='X'
        else:
            gridr2[j]='O'
    if i==2:
        if (player==1):
            gridr3[j]='X'
        else:
            gridr3[j]='O'
    print_grid(gridr1,gridr2,gridr3)
    return True;

""" Finds if the move is a Winning-move"""
def winning_case(move_num,gridr1,gridr2,gridr3):
    #print(move_num)
    if move_num>=5:
        # horizontal
        if gridr1[0]=='X' and gridr1[1]=='X' and gridr1[2]=='X' :
            return 1;
        elif gridr1[0]=='O' and gridr1[1]=='O' and gridr1[2]=='O' :
            return 2;
        elif gridr2[0]=='X' and gridr2[1]=='X' and gridr2[2]=='X' :
            return 1;
        elif gridr2[0]=='O' and gridr2[1]=='O' and gridr2[2]=='O' :
            return 2;
        elif gridr3[0]=='X' and gridr3[1]=='X' and gridr3[2]=='X' :
            return 1;
        elif gridr3[0]=='O' and gridr3[1]=='O' and gridr3[2]=='O' :
            return 2;
        #Vertical
        elif gridr1[0]=='X' and gridr2[0]=='X' and gridr3[0]=='X' :
            return 1;
        elif gridr1[0]=='O' and gridr2[0]=='O' and gridr3[0]=='O' :
            return 2;
        elif gridr1[1]=='X' and gridr2[1]=='X' and gridr3[1]=='X' :
            return 1;
        elif gridr1[1]=='O' and gridr2[1]=='O' and gridr3[1]=='O' :
            return 2;
        elif gridr1[2]=='X' and gridr2[2]=='X' and gridr3[2]=='X' :
            return 1;
        elif gridr1[2]=='O' and gridr2[2]=='O' and gridr3[2]=='O' :
            return 2;
        #Diagonal
        elif gridr1[0]=='X' and gridr2[1]=='X' and gridr3[2]=='X' :
            return 1;
        elif gridr1[0]=='O' and gridr2[1]=='O' and gridr3[2]=='O' :
            return 2;
        elif gridr1[2]=='X' and gridr2[1]=='X' and gridr3[0]=='X' :
            return 1;
        elif gridr1[2]=='O' and gridr2[1]=='O' and gridr3[0]=='O' :
            return 2;
    return 0;

#Main Program
time1 = datetime.datetime.now()
file = open('tictactoe.txt', 'w')
gridr1=[' ', ' ', ' ']
gridr2=[' ', ' ', ' ']
gridr3=[' ', ' ', ' ']
winner=0
move=0

#Print Initial Board
print_grid(gridr1,gridr2,gridr3)

while True:
    while True:
        #print("==============================")
        #print("Enter the values of Player 1: \n")
        #print("==============================")
        #print('move' + str(move))
        file.write("Move " + str(move + 1) + ": ")
        ret=input_values(1)
        if (ret==False):
            continue
        else :
            break
    move=move+1
    winner = winning_case(move,gridr1,gridr2,gridr3)
    #print('move' + str(move))
    if (move>=9 and winner ==0) :
        break;
    
    if (winner !=0):
        print("==============================")
        print('Winner : Player', winner , emoji.emojize(':thumbs_up: !!!!!!'), emoji.emojize(':grinning_face_with_smiling_eyes:'))
        print("==============================")
        #print(emoji.emojize(":thumbs_up: !!!!!!"))
        file.write("================================\n")
        file.write("Winner : Player " +  str(winner) +"\n")
        file.write("================================")
        break;

    while True:
        #print("==============================")
        #print("Enter the values of Player 2: \n")
        #print("==============================")
        file.write("Move " + str(move + 1) + ": ")
        ret=input_values(2)
        if (ret==False):
            continue;
        else :
            break;
    move=move+1
    winner = winning_case(move,gridr1,gridr2,gridr3)
    #print(str(winner))
    if (winner !=0):
        print("==============================")
        print('Winner Player', winner , emoji.emojize(':thumbs_up: !!!!!!'), emoji.emojize(':grinning_face_with_smiling_eyes:'))
        #print(emoji.emojize(":thumbs_up: !!!!!!"))
        file.write("================================\n")
        file.write("Winner : Player " +  str(winner) +"\n")
        file.write("================================")
        print("==============================")
        break;
 
if (winner ==0):
    print("==============================")
    print('MATCH RESULT : DRAWN')
    file.write('\nMATCH RESULT : DRAWN\n')
    print("==============================")
print("END GAME")

time2 = datetime.datetime.now()
elapsedTime = time2 - time1
#print(f'{elapsedTime.seconds}seconds')
file.write(f'\nTotal time of the match: {elapsedTime.seconds}seconds\n')
file.close()

option = input('Do you want to see the summary of the game (y/n)?')

if (option.lower() == 'y') :
    tblheader=[["Game Summary"]]
    termtables.print(tblheader)
    with open('tictactoe.txt', 'r') as reader:
        for line in reader:
            print(line, end='')

file.close()

