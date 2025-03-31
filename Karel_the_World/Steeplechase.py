"""
File: Steeplechase.py
Name: Zoe
---------------------------------
TODO:
"""

from karel.stanfordkarel import *
def turn_right():
    for i in range(3):
        turn_left()


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()
def up():
    """
    pre-condition:Karel is on the left side of the wall, facing East
    post-condition:Karel is at the upper left of pre-condition, facing East
    """
    while not front_is_clear():
        turn_left()
        move()
        turn_right()

def cross():
    """
    pre-condition:Karel is at the upper left of the wall, facing North
    post-condition:Karel is at the upper right, facing South
    """
    move()
    turn_right()

def down():
    """
    pre-condition:Karel is at the upper right of the wall, facing South
    post-condition:Karel is at the lower right of the wall, facing South
    """
    while front_is_clear():
        move()

def jump():
    """
    pre-condition:Karel is on the left side of the wall, facing East
    post-condition:Karel is on the right side of the wall
    """
    up()
    cross()
    down()




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
