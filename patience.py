


#-----Assignment Description-----------------------------------------#
#
# PATIENCE
#
# This assignment tests your skills at processing data stored in
# lists, creating reusable code and following instructions to display
# a complex visual image.  The incomplete Python program below is
# missing a crucial function, "deal_cards".  You are required to
# complete this function so that when the program is run it draws a
# game of Patience (also called Solitaire in the US), consisting of
# multiple stacks of cards in four suits.  See the instruction sheet
# accompanying this file for full details.
#
# Note that this assignment is in two parts, the second of which
# will be released only just before the final deadline.  This
# template file will be used for both parts and you will submit
# your final solution as a single Python 3 file, whether or not you
# complete both parts of the assignment.
#
#--------------------------------------------------------------------#



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must NOT rely on any non-standard Python
# modules that need to be installed separately, because the markers
# will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

# Constants defining the size of the card table
table_width = 1100 # width of the card table in pixels

table_height = 800 # height (actually depth) of the card table in pixels
canvas_border = 30 # border between playing area and window's edge in pixels
half_width = table_width // 2 # maximum x coordinate on table in either direction
half_height = table_height // 2 # maximum y coordinate on table in either direction

# Work out how wide some text is (in pixels)
def calculate_text_width(string, text_font = None):
    penup()
    home()
    write(string, align = 'left', move = True, font = text_font)
    text_width = xcor()
    undo() # write
    undo() # goto
    undo() # penup
    return text_width

# Constants used for drawing the coordinate axes
axis_font = ('Consolas', 10, 'normal') # font for drawing the axes
font_height = 14 # interline separation for text
tic_sep = 50 # gradations for the x and y scales shown on the screen
tics_width = calculate_text_width("-mmm -", axis_font) # width of y axis labels

# Constants defining the stacks of cards
stack_base = half_height - 25 # starting y coordinate for the stacks
num_stacks = 6 # how many locations there are for the stacks
stack_width = table_width / (num_stacks + 1) # max width of stacks
stack_gap = (table_width - num_stacks * stack_width) // (num_stacks + 1) # inter-stack gap
max_cards = 10 # maximum number of cards per stack

# Define the starting locations of each stack
stack_locations = [["Stack " + str(loc + 1),
                    [int(-half_width + (loc + 1) * stack_gap + loc * stack_width + stack_width / 2),
                     stack_base]]
                    for loc in range(num_stacks)]

# Same as Turtle's write command, but writes upside down
def write_upside_down(string, **named_params):
    named_params['angle'] = 180
    tk_canvas = getscreen().cv
    tk_canvas.create_text(xcor(), -ycor(), named_params, text = string)

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# create the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the coordinate axes displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_axes = True):

    # Set up the drawing canvas
    setup(table_width + tics_width + canvas_border * 2,
          table_height + font_height + canvas_border * 2)

    # Draw as fast as possible
    tracer(False)

    # Make the background felt green and the pen a lighter colour
    bgcolor('green')
    pencolor('light green')

    # Lift the pen while drawing the axes
    penup()

    # Optionally draw x coordinates along the bottom of the table
    if show_axes:
        for x_coord in range(-half_width + tic_sep, half_width, tic_sep):
            goto(x_coord, -half_height - font_height)
            write('| ' + str(x_coord), align = 'left', font = axis_font)

    # Optionally draw y coordinates to the left of the table
    if show_axes:
        max_tic = int(stack_base / tic_sep) * tic_sep
        for y_coord in range(-max_tic, max_tic + tic_sep, tic_sep):
            goto(-half_width, y_coord - font_height / 2)
            write(str(y_coord).rjust(4) + ' -', font = axis_font, align = 'right')

    # Optionally mark each of the starting points for the stacks
    if show_axes:
        for name, location in stack_locations:
            # Draw the central dot
            goto(location)
            color('light green')
            dot(7)
            # Draw the horizontal line
            pensize(2)
            goto(location[0] - (stack_width // 2), location[1])
            setheading(0)
            pendown()
            forward(stack_width)
            penup()
            goto(location[0] -  (stack_width // 2), location[1] + 4)
            # Write the coordinate
            write(name + ': ' + str(location), font = axis_font)

    #Draw a border around the entire table
    penup()
    pensize(3)
    goto(-half_width, half_height) # top left
    pendown()
    goto(half_width, half_height) # top
    goto(half_width, -half_height) # right
    goto(-half_width, -half_height) # bottom
    goto(-half_width, half_height) # left

    # Reset everything, ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any partial drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()

#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the deal_cards function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_game function appearing below.  Your
# program must work correctly for any data set that can be generated
# by the random_game function.
#

# Each of these fixed games draws just one card
fixed_game_0 = [['Stack 1', 'Suit A', 1, 0]]
fixed_game_1 = [['Stack 2', 'Suit B', 1, 0]]
fixed_game_2 = [['Stack 3', 'Suit C', 1, 0]]
fixed_game_3 = [['Stack 4', 'Suit D', 1, 0]]

# Each of these fixed games draws several copies of just one card
fixed_game_4 = [['Stack 2', 'Suit A', 4, 0]]
fixed_game_5 = [['Stack 3', 'Suit B', 3, 0]]
fixed_game_6 = [['Stack 4', 'Suit C', 2, 0]]
fixed_game_7 = [['Stack 5', 'Suit D', 5, 0]]

# This fixed game draws each of the four cards once
fixed_game_8 = [['Stack 1', 'Suit A', 1, 0],
                ['Stack 2', 'Suit B', 1, 0],
                ['Stack 3', 'Suit C', 1, 0],
                ['Stack 4', 'Suit D', 1, 0]]

# These fixed games each contain a non-zero "extra" value
fixed_game_9 = [['Stack 3', 'Suit D', 4, 4]]
fixed_game_10 = [['Stack 4', 'Suit C', 3, 2]]
fixed_game_11 = [['Stack 5', 'Suit B', 2, 1]]
fixed_game_12 = [['Stack 6', 'Suit A', 5, 5]]

# These fixed games describe some "typical" layouts with multiple
# cards and suits. You can create more such data sets yourself
# by calling function random_game in the shell window

fixed_game_13 = \
 [['Stack 6', 'Suit D', 9, 6],
  ['Stack 4', 'Suit B', 5, 0],
  ['Stack 5', 'Suit B', 1, 1],
  ['Stack 2', 'Suit C', 4, 0]]

fixed_game_14 = \
 [['Stack 1', 'Suit C', 1, 0],
  ['Stack 5', 'Suit D', 2, 1],
  ['Stack 3', 'Suit A', 2, 0],
  ['Stack 2', 'Suit A', 8, 5],
  ['Stack 6', 'Suit C', 10, 0]]

fixed_game_15 = \
 [['Stack 3', 'Suit D', 0, 0],
  ['Stack 6', 'Suit B', 2, 0],
  ['Stack 2', 'Suit D', 6, 0],
  ['Stack 1', 'Suit C', 1, 0],
  ['Stack 4', 'Suit B', 1, 1],
  ['Stack 5', 'Suit A', 3, 0]]

fixed_game_16 = \
 [['Stack 6', 'Suit C', 8, 0],
  ['Stack 2', 'Suit C', 4, 4],
  ['Stack 5', 'Suit A', 9, 3],
  ['Stack 4', 'Suit C', 0, 0],
  ['Stack 1', 'Suit A', 5, 0],
  ['Stack 3', 'Suit B', 5, 0]]

fixed_game_17 = \
 [['Stack 4', 'Suit A', 6, 0],
  ['Stack 6', 'Suit C', 1, 1],
  ['Stack 5', 'Suit C', 4, 0],
  ['Stack 1', 'Suit D', 10, 0],
  ['Stack 3', 'Suit B', 9, 0],
  ['Stack 2', 'Suit D', 2, 2]]

# The "full_game" dataset describes a random game
# containing the maximum number of cards
stacks = ['Stack ' + str(stack_num+1) for stack_num in range(num_stacks)]
shuffle(stacks)
suits = ['Suit ' + chr(ord('A')+suit_num) for suit_num in range(4)]
shuffle(suits)
full_game = [[stacks[stack], suits[stack % 4], max_cards, randint(0, max_cards)]
             for stack in range(num_stacks)]

#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a game
# of Patience to be drawn.  Your program must work for any data set
# returned by this function.  The results returned by calling this
# function will be used as the argument to your deal_cards function
# during marking. For convenience during code development and marking
# this function also prints the game data to the shell window.
#
# Each of the data sets generated is a list specifying a set of
# card stacks to be drawn. Each specification consists of the
# following parts:
#
# a) Which stack is being described, from Stack 1 to num_stacks.
# b) The suit of cards in the stack, from 'A' to 'D'.
# c) The number of cards in the stack, from 0 to max_cards
# d) An "extra" value, from 0 to max_cards, whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#
# There will be up to num_stacks specifications, but sometimes fewer
# stacks will be described, so your code must work for any number
# of stack specifications.
#
def random_game(print_game = True):

    # Percent chance of the extra value being non-zero
    extra_probability = 20

    # Generate all the stack and suit names playable
    game_stacks = ['Stack ' + str(stack_num+1)
                   for stack_num in range(num_stacks)]
    game_suits = ['Suit ' + chr(ord('A')+suit_num)
                  for suit_num in range(4)]

    # Create a list of stack specifications
    game = []

    # Randomly order the stacks
    shuffle(game_stacks)

    # Create the individual stack specifications
    for stack in game_stacks:
        # Choose the suit and number of cards
        suit = choice(game_suits)
        num_cards = randint(0, max_cards)
        # Choose the extra value
        if num_cards > 0 and randint(1, 100) <= extra_probability:
            option = randint(1,num_cards)
        else:
            option = 0
        # Add the stack to the game, but if the number of cards
        # is zero we will usually choose to omit it entirely
        if num_cards != 0 or randint(1, 4) == 4:
            game.append([stack, suit, num_cards, option])

    # Optionally print the result to the shell window
    if print_game:
        print('\nCards to draw ' +
              '(stack, suit, no. cards, option):\n\n',
              str(game).replace('],', '],\n '))

    # Return the result to the student's deal_cards function
    return game

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#

# Constants defining the stacks of cards
stack_base = half_height - 25 # starting y coordinate for the stacks
num_stacks = 6 # how many locations there are for the stacks
stack_width = table_width / (num_stacks + 1) # max width of stacks
stack_gap = (table_width - num_stacks * stack_width) // (num_stacks + 1) # inter-stack gap
max_cards = 10 # maximum number of cards per stack

def deal_cards(card_data):
    # Parameters for drawing the cards
    card_base = 100
    corner_radius = 15

    # X value (horizontal) of coordinates of each stack
    locations = {
        'Stack 1': -449,
        'Stack 2': -270,
        'Stack 3': -91,
        'Stack 4': 88,
        'Stack 5': 267,
        'Stack 6': 446
    }

    # Corresponding suit designs
    suit_designs = {
        'Suit A': 'boxes',
        'Suit B': 'circles',
        'Suit C': 'zigzags',
        'Suit D': 'triangles'
    }

    # Topmost Y coordinate of the card stacks
    base_y_coord = 375

    # Spacing between each card
    card_spacing = 50

    for stack in card_data:
        # Extract the origin x coordinate for each stack
        stored_coordinate = locations[stack[0]]

        # Convert it from center origin to left side origin
        x_coord = stored_coordinate - (card_base/2)

        amount_in_stack = stack[2]

        for card in range(0, amount_in_stack):
            # Spaces out each card in stack evenly
            y_coord = base_y_coord-(card_spacing*card)

            # Convert num in stack to string for later drawing
            identifier = str(card+1)

            # Convert special identifiers to letters (most not used in this program, however...)
            if(identifier == '1'):
                identifier = 'A'
            elif(identifier == '11'):
                identifier = 'J'
            elif(identifier == '12'):
                identifier = 'Q'
            elif(identifier == '13'):
                identifier = 'K'

            # Change design if stack has a joker and it is the current card.
            if(stack[3] != 0 and card == stack[3]-1):
                design = 'joker'
                identifier = "#"
            else:
                # Else just use normal design
                design = suit_designs[stack[1]]


            # Actually draw the card
            draw_outline([x_coord, y_coord], width = card_base, height = 150, linewidth = 2, fillet_width = corner_radius)
            draw_graphics([x_coord, y_coord], design,identifier, card_base, y_offset = corner_radius)
    return

# Draws the card graphics (not including the card numbering)
# Y offset is to offset the y axis because of the circle radius
def draw_graphics(origin, design, identifier, width = 60, height = 150, y_offset=0):

    # Calculate y offset due to circular corners
    origin[1] = origin[1]-y_offset;

    # Reset position
    penup()
    home()
    goto(origin)

    # Call the corresponing function for the graphic to be drawn
    if(design == 'boxes'):
        boxes(width, height)
    elif(design == 'zigzags'):
        zigzag(width, height)
    elif(design == 'circles'):
        circles(width, height)
    elif(design == 'triangles'):
        triangles(width, height)
    elif(design == 'joker'):
        joker(width, height)

    # Reset position
    penup()
    goto(origin)

    # Now draw the identifier (number or A,J,Q,K)
    draw_identifier(identifier, origin)

    return

# Draws the identifier on the card (letter, number) to make it unique in stack
def draw_identifier(identifier, origin, fill_color = 'white', identifier_color = 'black', size = 12):

    # Initialise
    home()
    fillcolor(fill_color)
    pencolor(identifier_color)
    goto(origin)
    right(90)
    begin_fill()
    pendown()

    # Draw the square background
    for side in range(0,4):
        forward(size*2)
        left(90)

    end_fill()
    penup()

    # Reposition to write text in correct spot (horizontally centred)
    forward(size*1.75)
    left(90)
    forward(size)

    # Draw the identifier
    pencolor(identifier_color)
    write(identifier, align='center', font=('Arial', size, 'bold'))

    return

# Draws the joker (enter key) card design (used only by draw_design())
def joker(max_width, max_height, mainColor = 'gray', altColor = 'silver'):

    # Draw the computer key onto the card graphic
    draw_key("Enter", max_width, max_height, mainColor, altColor)

    return

# Draws the triangle card design (used only by draw_design())
def triangles(max_width, max_height, mainColor = 'DeepSkyBlue4', altColor = 'DeepSkyBlue2', num_triangles = 5, row_offset = 0):

    # Initialise and setup Turtle
    penup()
    pencolor(mainColor)
    alternator = 0

    # Calculate side length that will fit onto card
    side_length = max_width/num_triangles

    # Use pythagorean theorem to calculate height from side length (base to vertex)
    triangle_height = sqrt(side_length**2)

    # Calculate number of rows that will fit onto card
    num_rows = int(max_height/(triangle_height + row_offset))

    for line_of_triangles in range(0, num_rows):
        for individual_row in range(0, num_triangles):

            # Alternate colors
            if(alternator == 0):
                pencolor(mainColor)
                alternator = 1
            else:
                pencolor(altColor)
                alternator = 0

            # Draw individual triangle
            pendown()
            for side in range(0,3):
                forward(side_length)
                right(120)
            penup()
            forward(side_length)

        # Move down to next row
        penup()
        right(90)
        forward(triangle_height+row_offset)

        # Reset position back to left side
        right(90)
        forward(num_triangles*side_length)
        right(180)

    # Draw the computer key onto the card graphic
    draw_key("Alt", max_width, max_height, mainColor, altColor)
    return

# Draws the circle card design (used only by draw_design())
def circles(max_width, max_height, mainColor = 'red', altColor = 'orange', num_circles = 7):

    # Initialise variables and setup turtle
    penup()
    pencolor(mainColor)
    alternator = 0

    # Calculate circle radius and spacing to fit them inside the card dimensions
    circle_radius = int(max_width/num_circles)/2
    circle_spacing = circle_radius*2
    circle_rows = int(max_height/circle_spacing)

    for individual_row in range(0, circle_rows):

        # Navigate to the proper position
        right(90)
        forward(circle_spacing)
        left(90)
        forward(circle_radius)

        for individual_circle in range(0, num_circles):

            # Alternate the colors
            if(alternator == 0):
                pencolor(mainColor)
                alternator = 1
            else:
                pencolor(altColor)
                alternator = 0

            # Draw the circle
            pendown()
            circle(circle_radius)
            penup()
            forward(circle_radius*2)

        # Return to start next row
        right(180)
        forward((circle_radius*2)*(num_circles+0.5))
        right(180)

    # Draw the computer key onto the card graphic
    draw_key("Tab", max_width, max_height, mainColor, altColor)
    return

# Draws the zigzag card design (used only by draw_design())
def zigzag(max_width, max_height, mainColor = 'green4', altColor = 'green3', num_zigzags = 9):

    # Initialise and setup variables
    penup()
    pencolor(mainColor)
    alternator = 0

    # Calculates zigzag segment length based on max_width using pythagorean theorem
    sidelengthA = max_width/num_zigzags # opposite & adjacent
    sideLengthC = sqrt(2*(sidelengthA**2)) # hypotenuse

    # Calculates min amount of spacing for zigzags
    zigzag_spacing = max_height/sidelengthA

    for individual_row in range(0, int(max_height/zigzag_spacing)):
        right(45)
        pendown()

        # Alternate the colors
        if(alternator == 0):
            pencolor(mainColor)
            alternator = 1
        else:
            pencolor(altColor)
            alternator = 0

        # Loop through and create each zigzag segment
        for zigzag_segment in range(0, num_zigzags):
            forward(sideLengthC/2)
            left(90)
            forward(sideLengthC/2)
            right(90)

        # Return back to start to begin next zigzag
        penup()
        right(90+45)
        forward(max_width)
        left(90)
        forward(zigzag_spacing)
        left(90)

    # Move to position to draw computer key
    left(90)
    forward(zigzag_spacing/2)
    right(90)

    # Draw the computer key onto the card graphic
    draw_key("Shift", max_width, max_height, mainColor, altColor)
    return

# Draws the boxes card design (used only by draw_design())
def boxes(max_width, max_height, mainColor = 'DeepPink4', altColor = 'DeepPink2', num_boxes = 5):

    # Setup turtle and initilise variables
    pencolor(mainColor)
    penup()
    alternator = 0

    # Boxes will always fit within the card, their size is flexible
    box_width = max_width/num_boxes
    box_height = box_width # These boxes will be square

    # Calculate the maximum number of rows
    num_rows = int(max_height/box_height)

    for box_rows in range(0, num_rows):
        for individual_row in range(0, num_boxes):

            # Alternate the colors
            if(alternator == 0):
                pencolor(mainColor)
                alternator = 1
            else:
                pencolor(altColor)
                alternator = 0

            # Draw the 4 sides of the box
            pendown()
            for individual_box in range(0, 2):
                forward(box_width)
                right(90)
                forward(box_height)
                right(90)
            penup()
            forward(box_width)

        # Return to start a new row
        right(180)
        forward(box_width*num_boxes)
        left(90)
        forward(box_height)
        left(90)

    # Draw the computer key onto the card graphic
    draw_key("Ctrl", max_width, max_height, mainColor, altColor)
    return


# Draws the outline of the cards, with origin at the top left corner of the card
def draw_outline(origin,width = 60, height = 150, color='black', linewidth = 5, fill=True, fillColor = 'white', fillet_width=10):
    # Initialise variables and setup turtle
    penup()
    home()
    goto(origin)

    fillcolor(fillColor)
    pencolor(color)
    pensize(linewidth)

    pendown()
    begin_fill()

    forward(width)

    # Draws each side of the card with filleted edges edges
    for side in range(0,2):
        right(180)
        circle(fillet_width,extent=-90)

        right(180)
        forward(height)

        right(180)
        circle(fillet_width, extent=-90)

        right(180)
        forward(width)

    end_fill()

    # Reset for next drawing
    penup()
    goto(origin)

    return

def draw_enter_key(width, height, key_width, key_height, mainColor, altColor, bg_buffer):
    # Setup turtle
    penup()
    pencolor(mainColor)
    fillcolor(altColor)

    # Reposition to top right corner
    forward(width-bg_buffer)
    right(90)

    # Draw key outline
    pendown()
    begin_fill()
    forward(key_height*2)
    right(90)
    forward(key_width)
    right(90)
    forward(key_height)
    right(90)
    forward(key_width/3)
    left(90)
    forward(key_height)
    right(90)
    forward(key_width*2/3)
    penup()
    end_fill()

    # Move to draw the text
    penup()
    right(90)
    forward(key_height/1.7)
    right(90)
    forward((key_width*2/3)/1.2)

    # Draw the key text and/or symbols
    font=("Arial", 7, 'bold')
    pencolor(mainColor)
    write("Enter", align="left", font=font)

    # Move to draw the arrow
    left(90)
    forward(10)
    left(90)
    forward(((key_width*2/3)/1.1)/2)
    right(90)

    # Draw arrow line
    pendown()
    forward(key_height/2)
    right(90)
    forward((key_width/2)*0.8)

    # Draw arrow head
    left(90)
    forward(4)
    right(90+45)
    forward(7)
    right(90)
    forward(7)
    right(90+45)
    forward(4)

    return

def draw_key(keytext, width, height, mainColor, altColor):
    # Setup for drawing the keys
    key_width = width / 2
    key_height = key_width / 2
    bg_buffer = 5

    # Enter key is shaped differently, so uses a different function
    if(keytext.upper() == "ENTER"):
        draw_enter_key(width, height, key_width, key_height, mainColor, altColor, bg_buffer)
        return

    # Move to top middle
    penup()
    forward(width-(key_width/2))
    left(90)
    forward(height-key_height+bg_buffer)

    # Move to the top left corner of key adding a background buffer
    forward(key_height/2 + bg_buffer)
    left(90)
    forward(key_width/2 + bg_buffer*1.5)
    left(90)

    # Draw a white box background
    fillcolor('white')
    pencolor('white')
    begin_fill()
    pendown()

    # Move in a rectangle
    for segment in range(0,2):
        forward(key_height + bg_buffer*2)
        left(90)
        forward(key_width + bg_buffer*2)
        left(90)

    penup()
    end_fill()

    # Reposition to draw the actual key
    forward(bg_buffer)
    left(90)
    forward(bg_buffer)

    # Draw the dark drop shadow
    fillcolor(mainColor)
    pencolor(mainColor)
    begin_fill()
    pendown()

    for segment in range(0,2):
        forward(key_width+(bg_buffer/2))
        right(90)
        forward(key_height+(bg_buffer/2))
        right(90)
    end_fill()
    penup()

    # Draw the key color background
    fillcolor(altColor)
    pencolor(altColor)
    begin_fill()
    pendown()

    for segment in range(0,2):
        forward(key_width)
        right(90)
        forward(key_height)
        right(90)
    end_fill()

    # Reposition
    penup()
    right(90)
    forward(key_height-bg_buffer)
    left(90)
    forward(bg_buffer)

    # Draw special symbols for some keys (not case sensitive)
    if(keytext.upper() == "SHIFT"):
        # Draw a little vertical arrow symbol for the shift key
        draw_shift_arrow(mainColor)

    elif(keytext.upper() == "TAB"):
        # Draw a horizontal arrow symbol for the tab key
        draw_tab_arrow(mainColor)

    # Draw the key text and/or symbols
    font=("Arial", 8, 'bold')
    pencolor(mainColor)
    write(keytext, align="left", font=font)

    return

# Draws the arrows for thet tab key
def draw_tab_arrow(color):
    pencolor(color)

    # Reposition
    left(90)
    forward(4)
    right(90)

    pendown()
    forward(10)

    # Draw arrow head
    fillcolor(color)
    begin_fill()

    # Draws a small triangle
    right(90)
    forward(3)
    left(90+40)
    forward(7)
    left(100)
    forward(7)
    left(90+40)
    forward(4)

    end_fill()

    # Draw the line on arrow head
    left(90)
    forward(9)
    left(90)
    forward(3)
    left(180)
    forward(6)
    left(180)
    forward(3)

    # Reposition
    penup()
    right(90)
    forward(4)
    right(90)
    forward(6)
    left(90)

    return

# Draws the iconic shift arrow
def draw_shift_arrow(color):
    pencolor(color)

    # Reposition
    left(90)
    forward(2)
    right(90)

    # Bottom of arrow
    forward(3)
    pendown()
    forward(5)
    left(90)

    # Vertical sides
    forward(4)
    right(90)

    # Top side
    forward(3)
    left(90+40)

    # Angled side
    forward(10)
    left(100)
    forward(10)

    # Top side
    left(90+40)
    forward(3)

    # Vertical side
    right(90)
    forward(4)

    left(90)
    forward(3)

    # Reset for other drawings
    penup()

    # Reposition
    right(90)
    forward(2)
    left(90)
    forward(11)

    return

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing the card game.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and stack locations
create_drawing_canvas(show_axes = False)

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your cards' theme
title(" PATIENCE | computer keys with cool backgrounds (shift, ctrl, alt, tab, enter)")

### Call the student's function to draw the game
### ***** While developing your program you can call the deal_cards
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_game()" as the
### ***** argument to the deal_cards function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_game function.
#deal_cards(random_game()) # <-- used for code development only, not marking
# deal_cards(full_game) # <-- used for code development only, not marking
deal_cards(random_game(print_game=False)) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
