board = [" - " , " - " , " - " ,
         " - " , " - " , " - " ,
         " - " , " - " , " - " ]

#to know whether the game is running
still_game_goin = True

#for winner dicision
winner = None

#for fliping player
player = " X "


#dispalying the empty board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


#play game
def play_game():

    display_board()

    while still_game_goin:
        global winner
        player_turn()
        winner = check_if_win()
        if winner == True:
            print(player + " WINS THE GAME.")
            break
        flip_player(player)
        game_ends()



#starting the game
def player_turn():
    position = input("enter the position for " + player + "'s turn :")
    position = int(position) - 1
    if board[position] == " X " or board[position] == " O ":
        print("the position  is already choosen")
    else:
        board[position] = player

    display_board()



#flipping the player
def flip_player(p):
    global player
    if p == " X ":
        player = " O "
    elif p == " O ":
        player = " X "


#checking  for the winner
def check_if_win():
    row_winner = check_rows()
    colown_winner = check_colowns()
    diagonal_winner = check_diagonals()

    if row_winner == True or colown_winner == True or diagonal_winner == True:
        return True
    else:
        return False


def check_rows():

    pos = 0
    if board[pos] == board[pos + 1] == board[pos + 2]:
        return  True
    else:
        return False


    pos_1 = 3
    if board[pos_1] == board[pos_1 + 1] == board[pos_1 + 2]:
        return True
    else:
        return False

    pos_2 = 6
    if board[pos_2] == board[pos_2 + 1] == board[pos_2 + 2]:
        return True
    else:
        return False



def check_colowns():

    pos = 0
    if board[pos] == board[pos + 3] == board[pos + 6]:
        return True
    else:
        return False

    pos_1 = 3
    if board[pos_1] == board[pos_1 + 3] == board[pos_1 + 6]:
        return True
    else:
        return False

    pos_2 = 6
    if board[pos_2] == board[pos_2 + 3] == board[pos_2 + 6]:
        return True
    else:
        return False




def check_diagonals():

    pos = 0
    if board[pos] == board[pos + 4] == board[pos + 8]:
        return True
    else:
        return False

    pos_1 = 3
    if board[pos_1] == board[pos_1 + 4] == board[pos_1 + 8]:
        return True
    else:
        return False

    pos_2 = 6
    if board[pos_2] == board[pos_2 + 4] == board[pos_2 + 8]:
        return True
    else:
        return False


def game_ends():
    result = 0
    global still_game_goin
    for pos in range(len(board)):
        if board[pos] != " - ":
            result = result + 1

    if result == 9:
         still_game_goin = False
         print("game tie")



play_game()



print("romba perumai ah irukke  .. .... . . .!!")