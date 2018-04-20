
###########################################################################
#Code Name: Matrix Trick
#Developed by: ElenaZ
#Modified by: Eric Zhou
#Date: 20 Apr, 2018
#Code Description: it is a game that demonstrates liner algebra -  matrix function. It asks for
#any five random numbers from user and displays the sum of the selected numbers.
#fun to play:)
###########################################################################

import msvcrt
import time
import numpy as np

m=np.zeros((4,4),int)
print(m)

print('pls enter 6 numbers:')
m[0,1] = int(input('1st num:'))
m[0,2] = int(input('2nd num:'))
m[0,3] = int(input('3rd num:'))
m[1,0] = int(input('4th num:'))
m[2,0] = int(input('5th num:'))
m[3,0] = int(input('6th num:'))
print(m)

m[1,1] = m[0,1] + m[1,0]
m[1,2] = m[0,2] + m[1,0]
m[1,3] = m[0,3] + m[1,0]
m[2,1] = m[0,1] + m[2,0]
m[2,2] = m[0,2] + m[2,0]
m[2,3] = m[0,3] + m[2,0]
m[3,1] = m[0,1] + m[3,0]
m[3,2] = m[0,2] + m[3,0]
m[3,3] = m[0,3] + m[3,0]
print(m)

t_m = m[1:,1:]
print(t_m)

print('Rule 1: pls select 3 lucky numbers, all the numbers sit on the same rows and columns as the selected one have to be crossed out and can not be selected!')
print('Rule 2: number sits on matrix position =00 can not be selected!')
#pause 30 secs
print('------------- sum of your two selected numbers are... /.\./.\. ---------')
time.sleep(5)
total_out= str(m[0,1] + m[0,2] + m[0,3] + m[1,0] + m[2,0] + m[3,0])
print('sum of your two selected numbers is: ' + total_out)
