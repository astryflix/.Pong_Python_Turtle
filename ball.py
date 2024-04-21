from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 7
        self.y_move = 7

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def increase_speed(self):
        # You can adjust the speed increment to your preference
        if self.x_move > 0:
            self.x_move += 1.5
        else:
            self.x_move -= 1

        if self.y_move > 0:
            self.y_move += 1.5
        else:
            self.y_move -= 1

    def bounce_paddle(self):
        self.x_move *= -1
        self.increase_speed()
