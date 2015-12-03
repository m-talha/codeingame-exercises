import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
thorX = initial_tx; thorY = initial_ty

# game loop
while 1:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # A single line providing the move to be made: N NE E SE S SW W or NW
    
    delta_y = light_y - thorY
    delta_x = light_x - thorX
    print(delta_y, file=sys.stderr); print(delta_x, file=sys.stderr)
    angle = 0
    
    if (delta_y != 0 and delta_x != 0):
        hyp = math.sqrt((delta_y*delta_y + delta_x*delta_x))
        angle = math.atan2(delta_y, delta_x)
  
    if (angle > 0 and angle < math.pi/2):
        print('SE')
        thorX +=1; thorY+=1
    elif (angle > math.pi/2 and angle < math.pi):
        print('SW')
        thorX -=1; thorY+=1
    elif (angle > math.pi and angle < math.pi*3/4):
        print('NW')
        thorX -=1; thorY-=1
    elif (angle > math.pi*3/4 and angle < math.pi*2):
        print('NE')
        thorX +=1; thorY-=1
    elif (angle == 0 and thorX < light_x):
        print('E')
        thorX +=1
    elif (angle == 0 and thorX > light_x):
        print('W')
        thorX -=1
    elif (angle == 0 and thorY > light_y):
        print('N')
        thorY -=1
    elif (angle == 0 and thorY < light_y):
        print('S')
        thorY +=1
