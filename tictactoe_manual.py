board = { '1': ' ', '2': ' ', '3': ' ',
          '4': ' ', '5': ' ', '6': ' ',
          '7': ' ', '8': ' ', '9': ' ' }

def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

turn = 'X'
for i in range(9):
     printboard(board)
     print('Turn for ' + turn + '. Move on which space?')
     move = input()
     board[move] = turn
     if( (board['1']==board['5']==board['9']==turn) or (board['1']==board['2']==board['3']==turn) or
         (board['4']==board['5']==board['6']==turn) or (board['7']==board['8']==board['9']==turn)or
         (board['1']==board['4']==board['7']==turn) or (board['2']==board['5']==board['8']==turn)or
         (board['3']==board['6']==board['9']==turn) or (board['3']==board['5']==board['7']==turn)):
         printboard(board)
         print( turn + ' wins!')
         break
     if ( i == 8 ):
         print( 'draw!')
         break
     if turn == 'X':
        turn = 'O'
     else:
        turn = 'X'
