from numpy import array

board=array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
temp_board=array([[f'({i},{j})' for j in range(3)] for i in range(3)])

print("Tic-Tac-Toe begins !\nTo exit the game mid-way, press 'Ctrl+C'\n")
print(f'\n{board[0]}\t{temp_board[0]}\n{board[1]} = {temp_board[1]}\n{board[2]}\t{temp_board[2]}\n')

def move(x, y, player):

    try:
        if board[x, y]!=' ':
            print('\nThe location chosen is already occupied, choose another location !\n')

            a, b=int(input(f'Enter the position for the {player}\nEnter the row number:')), int(input('Enter the column number:'))
            move(a, b, player)
            
        else:
            board[x, y]=player
            print(f'\n{board[0]}\n{board[1]}\n{board[2]}\n')
                
            print(f'Player {player} wins !\n') or quit() if board[x, 0]==board[x, 1]==board[x, 2]==player or board[0, y]==board[1, y]==board[2, y]==player or board[0, 0]==board[1, 1]==board[2, 2]==player or board[0, 2]==board[1, 1]==board[2, 0]==player else None

            check=tuple(0 for row in range(3) for column in range(3) if board[row, column]==' ')
            print("It's a draw ! The game ends here.\n") or quit() if len(check)==0 else None

    except IndexError:
        print('\nEnter a valid location !\n')

        a1, b1=int(input(f'Enter the position for the {player};\nEnter the row number:')), int(input('Enter the column number:'))
        move(a1, b1, player)

while True:

    try:
        x1, x2=int(input('Enter the position for the O;\nEnter the row number:')), int(input('Enter the column number:'))
        move(x1, x2, 'O')

        y1, y2=int(input('Enter the position for the X;\nEnter the row number:')), int(input('Enter the column number:'))
        move(y1, y2, 'X')

    except ValueError:
        print('\nEnter a valid location !\n')
