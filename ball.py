from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 20
        self.y_move = 20
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def detect_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            return True
        return False

    def detect_paddle(self, paddle):
        if self.distance(paddle) < 50 and (self.xcor() > 320 or self.xcor() < -320):
            return True
        return False

    def restart(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = 0.1

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
