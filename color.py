"""
Given two cells of a chessboard. If they are painted in one color, print the word YES,
 and if in a different color - NO.
The program receives the input of four numbers from 1 to 8, 
each specifying the column and row number, first two - 
for the first cell, and then the last two - for the second cell.

"""
a1 = int(input())
a2 = int(input())
c1 = int(input())
c2 = int(input())

if (a1+a2+c1+c2)%2==0:
    print("YES")
else:
    print("NO")