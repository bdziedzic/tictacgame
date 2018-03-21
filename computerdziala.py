import termios, sys, os, random
import time

TERMIOS = termios
 
def getkey():
    fd = sys.stdin.fileno()                                            
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c


board =  ['1','2','3',
        '4','5','6',
        '7','8','9']
lista = ['1','2','3','4','5','6','7','8','9']
win_commbinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

choice = ["Y", "N"]

first_player = "w"
second_player = "z"



def draw():
    print("___", "*","___", "*")
    print(board[6],"_", "*", board[7],"_", "*", board[8])
    print("___", "*","___", "*")

    print("*", "*", "*","*","*","*", "*","*")

    print("___", "*","___", "*")
    print(board[3],"_", "*", board[4],"_", "*", board[5])
    print("___", "*","___", "*")

    print("*", "*", "*","*","*","*","*","*")

    print("___", "*","___", "*")
    print(board[0],"_", "*", board[1],"_", "*", board[2])
    print("___", "*","___", "*")

def win1(x):
    print("\033[1;34m" "First player won!""\033[1;m")
    x+=1

def win2(x):
    x+=1
    draw()
    print("\033[1;31m""Second player won!""\033[1;m")
    
    

def start():
    wybor = "P"
    print("Hello! Tic tac toe, Let's go!")
    while wybor not in choice:
        
        wybor = input("Do you want to play? y/n : ").upper()
        print(wybor)
    if wybor == "Y":
        multiplayer = input("Type 1 to single-player, type 2 to multi-player ")
        if multiplayer == "1":
            single()
        elif multiplayer == "2":
            multi()
    elif wybor == "N":
        print("Goodbye!")

    
    
          
 

def first(first_player):
    while first_player not in lista:
        print("Put your 'X'")
        first_player = getkey().decode()
        if first_player not in lista:
            print("Please press a number from 1 to 9")
            continue
        while board[int(first_player)-1] == "\033[1;34m""x""\033[1;m" or board[int(first_player)-1] == "\033[1;31m""o""\033[1;m":
            print("This spot is taken!")
            print("Choose the number")
            first_player = getkey().decode()
            while first_player not in lista:
                first_player = input("Please press a number from 1 to 9")
        if first_player == "1":
            board[0] = "\033[1;34m""x""\033[1;m"
        elif first_player == "2":
            board[1] = "\033[1;34m""x""\033[1;m"
        elif first_player == "3":
            board[2] = "\033[1;34m""x""\033[1;m"
        elif first_player == "4":
            board[3] = "\033[1;34m""x""\033[1;m"
        elif first_player == "5":
            board[4] = "\033[1;34m""x""\033[1;m"
        elif first_player == "6":
            board[5] = "\033[1;34m""x""\033[1;m"
        elif first_player == "7":
            board[6] = "\033[1;34m""x""\033[1;m"
        elif first_player == "8":
            board[7] = "\033[1;34m""x""\033[1;m"
        elif first_player == "9":
            board[8] = "\033[1;34m""x""\033[1;m"
           
def second(second_player):    
    while second_player not in lista: 
        print("\033[1;31m""2nd player's turn""\033[1;m")
        second_player = getkey().decode()
        if second_player not in lista:
            print("Please press a number from 1 to 9")
            continue
        while board[int(second_player)-1] == "\033[1;34m""x""\033[1;m" or board[int(second_player)-1] == "\033[1;31m""o""\033[1;m":
            print("This place is taken")
            second_player = getkey().decode()
            while second_player not in lista:
                print("Please press a number from 1 to 9")
                second_player = getkey().decode()
        if second_player in board:
            if second_player == "1":
                board[0] = "\033[1;31m""o""\033[1;m"
            elif second_player == "2":
                board[1] = "\033[1;31m""o""\033[1;m"
            elif second_player == "3":
                board[2] = "\033[1;31m""o""\033[1;m"
            elif second_player == "4":
                board[3] = "\033[1;31m""o""\033[1;m"
            elif second_player == "5":
                board[4] = "\033[1;31m""o""\033[1;m"
            elif second_player == "6":
                board[5] = "\033[1;31m""o""\033[1;m"
            elif second_player == "7":
                board[6] = "\033[1;31m""o""\033[1;m"
            elif second_player == "8":
                board[7] = "\033[1;31m""o""\033[1;m"
            elif second_player == "9":
                board[8] = "\033[1;31m""o""\033[1;m"

def computer(): 
    computer_choice = 1
    while computer_choice not in board:
        computer_choice = random.choice(lista)
        print(computer_choice)
        if computer_choice not in board: 
            continue   
        elif computer_choice in board:
            time.sleep(2)
        while computer_choice in board:
            print(computer_choice)
            board[int(computer_choice) - 1] = "\033[1;31m""o""\033[1;m"
            print(board)
            break
        break

    
            
            
'''
if computer_choice == "1":
    board[0] = "\033[1;31m""o""\033[1;m"
    elif computer_choice == "2":
        board[1] = "\033[1;31m""o""\033[1;m"
    elif computer_choice == "3":
        board[2] = "\033[1;31m""o""\033[1;m"
    elif computer_choice == "4":
        board[3] = "\033[1;31m""o""\033[1;m"
    elif computer_choice == "5":
        board[4] = "\033[1;31m""o""\033[1;m"
    elif computer_choice == "6":
        board[5] = "\033[1;31m""o""\033[1;m"
    elif computer_choice == "7":
        board[6] = "\033[1;31m""o""\033[1;m"
    elif computer_choice == "8":
        board[7] = "\033[1;31m""o""\033[1;m"
    elif computer_choice == "9":
        board[8] = "\033[1;31m""o""\033[1;m"
    break'''

'''zmienne staly sie lokalne'''

def single():   
    x = 0                                                       
    rounds = 0
    while x==0:
        draw()   
        first(first_player)   
        rounds = rounds + 1
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] =="\033[1;34m""x""\033[1;m":
                win1(x)
                x+=1
                break
        draw()
        if rounds == 5 and x == 0:
            print("\033[1;32mRemis!!!\033[1;m")
            x+=1         
            break
        if x == 0:
            computer() 
            for a in win_commbinations:                                      
                if board[a[0]] == board[a[1]] == board[a[2]] =="\033[1;31m""o""\033[1;m":
                    win2(x)
                    x+=1
                    break

def multi():
    x = 0
    rounds = 0
    while x==0:
        draw()   
        first(first_player)   
        rounds = rounds + 1
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] =="\033[1;34m""x""\033[1;m":
                win1(x)
                x+=1
                break
        draw()
        if rounds == 5 and x == 0:
            print("\033[1;32mRemis!!!\033[1;m")
            x+=1         
            break
        if x == 0:
            second(second_player) 
            for a in win_commbinations:                                      
                if board[a[0]] == board[a[1]] == board[a[2]] =="\033[1;31m""o""\033[1;m":
                    win2(x)
                    x+=1
                    break
      

start()


#main(x, rounds)




    


