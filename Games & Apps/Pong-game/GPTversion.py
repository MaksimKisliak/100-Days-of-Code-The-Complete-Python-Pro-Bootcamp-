import turtle

class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.dx = 2
        self.dy = 2

    def move(self):
        x = self.xcor()
        y = self.ycor()
        x += self.dx
        y += self.dy
        self.goto(x, y)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score_a = 0
        self.score_b = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Player A: {self.score_a}  Player B: {self.score_b}", align="center", font=("Courier", 24, "normal"))

    def point_to_a(self):
        self.score_a += 1
        self.clear()
        self.update_scoreboard()

    def point_to_b(self):
        self.score_b += 1
        self.clear()
        self.update_scoreboard()

class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Pong")
        self.screen.bgcolor("black")
        self.screen.setup(width=600, height=400)
        self.screen.tracer(0)

        self.paddle_a = Paddle((-250, 0))
        self.paddle_b = Paddle((250, 0))
        self.ball = Ball()
        self.score = Score()

        self.screen.listen()
        self.screen.onkeypress(self.paddle_a.up, "w")
        self.screen.onkeypress(self.paddle_a.down, "s")
        self.screen.onkeypress(self.paddle_b.up, "Up")
        self.screen.onkeypress(self.paddle_b.down, "Down")

    def play(self):
        while True:
            self.screen.update()
            self.ball.move()

            # Check for collision with top/bottom walls
            if self.ball.ycor() > 190 or self.ball.ycor() < -190:
                self.ball.bounce_y()

            # Check for collision with paddles
            if (self.ball.xcor() > 240 and self.ball.distance(self.paddle_b) < 50) or (self.ball.xcor() < -240 and self.ball.distance(self.paddle_a) < 50):
                self.ball.bounce_x()

            # Check for point scoring
            if self.ball.xcor() > 290:
                self.ball.reset_position()
                self.score.point_to_a()

            if self.ball.xcor() < -290:
                self.ball.reset_position()
                self.score.point_to_b()

if __name__ == "__main__":
    game = Game()
    game.play()
