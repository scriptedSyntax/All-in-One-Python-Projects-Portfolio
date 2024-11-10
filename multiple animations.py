from tkinter import *
import time


# This is the class function we will use
class Ball:
    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, colour):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, x + diameter, y + diameter, fill=colour)
        # Diameter passed twice since (height = width) in circles
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        # Get current coordinates of the ball
        coordinates = self.canvas.coords(self.image)
        print(coordinates)

        # Move the ball
        new_x = coordinates[0] + self.xVelocity
        new_y = coordinates[1] + self.yVelocity

        # Check for wall collisions and reverse direction if necessary
        if new_x < 0 or new_x + (coordinates[2] - coordinates[0]) > self.canvas.winfo_width():
            self.xVelocity = -self.xVelocity
        if new_y < 0 or new_y + (coordinates[3] - coordinates[1]) > self.canvas.winfo_height():
            self.yVelocity = -self.yVelocity

        # Update the position of the ball
        self.canvas.move(self.image, self.xVelocity, self.yVelocity)


# Set up the main window
window = Tk()
WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

# Create an instance of Ball
volley_ball = Ball(canvas, 0, 0, 70, 1, 1, "white")
basket_ball =  Ball(canvas, 0,10,120,3,4,"blue")
foot_ball =  Ball(canvas, 20,5,40,7,8,"black")
# Main loop to move the ball
while True:
    volley_ball.move()
    basket_ball.move()
    foot_ball.move()
    window.update()
    time.sleep(0.01)

# The following line is unreachable and should be removed(or not it doesn't matter)
# window.mainloop()

if __name__ == "__main__":
    # The instantiation here is unnecessary since it's already created above.
    pass