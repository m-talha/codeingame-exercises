import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(input())  # the length of the road before the gap.
gap = int(input())  # the length of the gap.
platform = int(input())  # the length of the landing platform.

jumped = False

# game loop
while 1:
    speed = int(input())  # the motorbike's speed.
    coord_x = int(input())  # the position on the road of the motorbike.

    # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
    if (speed <= gap and not jumped):
        print("SPEED")
    elif (jumped or speed > gap+1):
        print("SLOW")
    elif (speed > gap and coord_x + speed < road + gap):
        print("WAIT")
    else:
        print("JUMP")
        jumped = True