# Python drawing application
# Takes a filename from the command line, reads the file
# and processes the file contents by executing the commands
# listed in the file
# The commands will be instructions on what to draw on the screen
#

# Sprint - weekly objectives for fixes and features
import turtle

WELCOME = ("Python Drawing Application")

def initialize_turtle():
    return turtle.Turtle()

def main():
    print(WELCOME)
    main_turtle = initialize_turtle()
    main_turtle.forward(100)
    main_turtle.left(90)
    main_turtle.forward(100)
    turtle.Screen().exitonclick()

if __name__ == '__main__':
    main()
