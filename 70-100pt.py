##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

House = drawpad.create_rectangle (200,500, 600,200,fill='red')
roof = drawpad.create_line (200,200, 400, 100)
roof = drawpad.create_line (600,200, 400, 100)
door = drawpad.create_rectangle (350, 500, 450, 350,fill = 'chocolate')
knob = drawpad.create_oval (450,400, 400,420,fill = 'gold')
Grass = drawpad.create_rectangle (0,600, 800,500,fill='forest green') 
chimney = drawpad.create_line (400,400, 500,100)

root.mainloop()
