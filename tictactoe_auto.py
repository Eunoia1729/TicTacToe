import random

board = { '1': ' ', '2': ' ', '3': ' ',
          '4': ' ', '5': ' ', '6': ' ',
          '7': ' ', '8': ' ', '9': ' ' }


def printboard(board):
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('---------')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('---------')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    
while True:
 for j in range(1,10):
     board[str(j)]=' '
 list=[1,2,3,4,5,6,7,8,9]     
 print('Do you want to be X or O?(type X or O)')
 player = input()

 if player.upper() == 'X':
        computer = 'O'
        player ='X'
 else:
        player ='O'
        computer = 'X'
 print('The computer will go first.')
 list1 = [ ['1','5','9'],['1','2','3'],['4','5','6'],['7','8','9'],['1','4','7'],['2','5','8'],['3','6','9'],['3','5','7'] ]
 list2 = ['1','3','7','9']
 list3 = ['9','7','3','1']
 for i in range(5):
     
     #position1= random.randint(0,len(list)-1)
     while( True):
       flag = 0  
       if( 5 in list):
         position1 = 5
         break
       for k in range( len(list1)):
           if( (board[str(list1[k][0])] == board[str(list1[k][1])] == computer) and ( int(list1[k][2]) in list )):
                   position1 = list1[k][2]
                   flag = 1
                   break
           if( board[str(list1[k][2])] == board[str(list1[k][1])] == computer and (int(list1[k][0]) in list )):
                   position1 = list1[k][0]
                   flag = 1
                   break
           if( (board[str(list1[k][0])] == board[str(list1[k][2])] == computer) and ( int(list1[k][1]) in list ) ):
                   position1 = list1[k][1]
                   flag = 1
                   break
       if(flag == 1):
            break
       for k in range( len(list1)):
           if( (board[str(list1[k][0])] == board[str(list1[k][1])] == player) and ( int(list1[k][2]) in list )):
                   position1 = list1[k][2]
                   flag = 1
                   break
           if( board[str(list1[k][2])] == board[str(list1[k][1])] == player and (int(list1[k][0]) in list )):
                   position1 = list1[k][0]
                   flag = 1
                   break
           if( board[str(list1[k][0])] == board[str(list1[k][2])] == player and (int(list1[k][1]) in list )):
                   position1 = list1[k][1]
                   flag = 1
                   break
       if(flag == 1):
            break
       for k in range(len(list2)):
                if( int(list2[k]) in list and int(list3[k]) in list ):
                  position1 = list2[k]
                  flag = 1
                  break
       if(flag == 1):
            break
       position1 =list[random.randint(0,len(list)-1)]
       break        
                
                
     board[str(position1)] = computer
     #del list[position1]
     list.remove(int(position1))
     #print(position1)
     #print(list)
     
     turn = computer
     printboard(board)
     
     if( (board['1']==board['5']==board['9']==turn) or (board['1']==board['2']==board['3']==turn) or                      
         (board['4']==board['5']==board['6']==turn) or (board['7']==board['8']==board['9']==turn) or
         (board['1']==board['4']==board['7']==turn) or (board['2']==board['5']==board['8']==turn) or
         (board['3']==board['6']==board['9']==turn) or (board['3']==board['5']==board['7']==turn)) :
               
                    print('The computer has beaten you! You lose.')
                    break
    
     if( i == 4 and turn == computer):
         print( 'draw!')
         break
     

     print('What is your next move?')
     
     move = input()
     board[move] = player
     list.remove(int(move))
     turn = player
     
     if( (board['1']==board['5']==board['9']==turn) or (board['1']==board['2']==board['3']==turn) or                      
         (board['4']==board['5']==board['6']==turn) or (board['7']==board['8']==board['9']==turn) or
         (board['1']==board['4']==board['7']==turn) or (board['2']==board['5']==board['8']==turn) or
         (board['3']==board['6']==board['9']==turn) or (board['3']==board['5']==board['7']==turn)) :
         
                   print('You have beaten the computer! You win.')
                   break
                       
 print('Do you want to play again? (yes or no)')
 answer = input()
 if ( answer.lower() == 'no'):
      break
