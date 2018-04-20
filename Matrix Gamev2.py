
###########################################################################
#Code Name: Matrix Trick
#Developed by: ElenaZ
#Date: 20 Apr, 2018
#Code Description: it is a game that demonstrate linear algebra. It asks for
#random 5 numbers from a user and display the sum of the numbers selected
#fun to play:)
###########################################################################

import msvcrt
import time

inboard = {'1','2','3','4','5'}
theBoard = {'11': ' ', '12': ' ', '13': ' ',
            '21': ' ', '22': ' ', '23': ' ',
            '31': ' ', '32': ' ', '33': ' '}
def printBoard(board):
    print(board['11'] + '|' + board['12'] + '|' + board['13'])
    print('-+-+-')
    print(board['21'] + '|' + board['22'] + '|' + board['23'])
    print('-+-+-')
    print(board['31'] + '|' + board['32'] + '|' + board['33'])
#only populate the first row and first column
printBoard(theBoard)
print('pls enter 5 numbers:')

theBoard['11'] = input()
theBoard['12'] = input()
theBoard['13'] = input()
theBoard['21'] = input()
theBoard['31'] = input()
printBoard(theBoard)

print ('Press Enter to auto calc the rest of the cells in the matrix:\n')
if (ord(msvcrt.getch())) == 13:
    theBoard['22'] = str(int(theBoard['12']) + int(theBoard['21']))
    theBoard['23'] = str(int(theBoard['13']) + int(theBoard['21']))
    theBoard['32'] = str(int(theBoard['12']) + int(theBoard['31']))
    theBoard['33'] = str(int(theBoard['13']) + int(theBoard['31']))
    printBoard(theBoard)

print('Rule 1: pls select 2 lucky numbers, all the numbers sit on the same rows and columns as the selected ones have to be crossed out and can not be selected!')
print('Rule 2: number sits on matrix position =11 can not be selected!')
#pause 30 secs
print('------------- calculating the the sum of your selected 2 numbers /.\./.\. ---------')
time.sleep(30)
total_out= str(int(theBoard['12']) + int(theBoard['13']) + int(theBoard['21']) + int(theBoard['31']))
print('sum of your selected 2 numbers is: ' + total_out)
