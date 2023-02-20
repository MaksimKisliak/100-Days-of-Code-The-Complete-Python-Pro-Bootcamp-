import turtle
import random

# Base class for game elements
class GameElement(turtle.Turtle):
    def __init__(self, x, y, shape, color):
        super().__init__()
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.shape(shape)
        self.color(color)
        self.speed = 1

    def move(self):
        self.forward(self.speed)

    def is_collision(self, other):
        if self.distance(other) < 20:
            return True
        else:
            return False

# Subclass for player-controlled turtle
class Player(GameElement):
    def __init__(self, x, y):
        super().__init__(x, y, "turtle", "green")
        self.speed = 2
        self.setheading(90)
        
    def move_up(self):
        self.setheading(90)
        self.move()
        
    def move_down(self):
        self.setheading(270)
        self.move()

# Subclass for car obstacles
class Car(GameElement):
    def __init__(self, x, y):
        super().__init__(x, y, "square", "red")
        self.speed = random.randint(1, 3)
        self.setheading(180)

# Create the game screen and player
wn = turtle.Screen()
wn.title("Turtle Crossing")
wn.bgcolor("white")
wn.setup(width=600, height=600)

player = Player(0, -250)

# Create cars at random positions
cars = []
for i in range(10):
    x = random.randint(-280, 280)
    y = random.randint(-200, 200)
    cars.append(Car(x, y))

# Keyboard bindings for player movement
wn.listen()
wn.onkeypress(player.move_up, "Up")
wn.onkeypress(player.move_down, "Down")

# Main game loop
while True:
    for car in cars:
        car.move()

        if player.is_collision(car):
            player.color("red")
            print("Game Over")
            wn.update()
            wn.mainloop()
            break

        if car.xcor() < -300:
            car.goto(300, random.randint(-200, 200))

    wn.update()
