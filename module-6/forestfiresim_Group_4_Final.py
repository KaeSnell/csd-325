"""
Jessie Miers
Jonathan Davila
Kalea Snell
7/6/25

Module 6.2
Program has been modified from original to include
a water feature that acts as fire break that fire can 
not go passed. ~ was added to represent water and 
given the color cyan. 
"""

"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '

#Add ~ for water.   <<<<<
WATER = '~'

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here:
                    continue

                #This ensures water will always stay water in the next cycle. It is technically redundant, but it is there as a fail-safe to ensure water will not be changed.   <<<<    
                if forest[(x,y)] == WATER:
                    nextForest[(x,y)] = WATER
                
                elif ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Fire spreads to neighboring trees:
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY

          
                else:
                    # Just copy the existing object:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
                              
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.

    
    #Code added to block out water area in the simulation.
    #Spaces in this area will be water. 

    #Original code for water
    """
    for y in range(6,16):
        for x in range(30,40):
            forest[(x,y)] = WATER 
    
    """
    #Code added to Number 4 of water in the simulation since our group was Group 4 as added flair.       
        
    for y in range(6,16):
        for x in range(40,43):
            forest[(x,y)] = WATER
    
    for y in range(11,13):
        for x in range(27,46):
            forest[(x,y)] = WATER
    
    diagonal_water_coords = [(28,10),(29,10),(30,10),
                            (29,9),(30,9),(31,9),
                            (30,8),(31,8),(32,8),
                            (31,7),(32,7),(33,7),
                            (32,6),(33,6),(34,6),
                            (33,5),(34,5),(35,5),
                            (34,4),(35,4),(36,4),
                            (35,3),(36,3),(37,3)] 
    for coord in diagonal_water_coords:
        forest[coord] = WATER

    
         
    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)

    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
          	
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')

            #Added to ensure if space is water color it cyan.    <<<<<
            elif forest[(x,y)]== WATER:
                bext.fg('cyan')
                print(WATER, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
