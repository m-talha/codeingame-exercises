import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

biggest_m =-1
# game loop
while 1:
    biggest_h =0
    space_x, space_y = [int(i) for i in input().split()]
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        if (mountain_h > biggest_h):
            biggest_h = mountain_h
            biggest_m = i
            
    if (space_x == biggest_m):
        print("FIRE")
    else:
        print("HOLD")
        
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    #print("mountains:", file=sys.stderr)
    #print(mountain_h[3], file=sys.stderr)
    # either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing).
