import turtle as trl


class My_turtle(trl.Turtle):
    def __init__(
        self,
        color = "#000000",
        pensize = 3,
        shape = "turtle",
        speed = 3
    ):
        super().__init__(shape)
        self.color(color)
        self.pensize(pensize)
        self.shape(shape)
        self.speed(speed)

    def draw_square(self, side_lenght):
        for i in range(4):
            self.forward(side_lenght)
            self.left(90)


t1 = My_turtle(
    color="blue",
    pensize = 2,
    shape = "turtle",
    speed = 15
)

t2 = My_turtle(
    color="green",
    pensize = 1,
    shape = "turtle",
    speed = 15
    )

t1.penup()
t1.goto(1000, 1000)
t2.penup()
t2.goto(300, 300)
t2.pendown()
t2.left(180)


for i in range(1, 10000 , 2):
    t2.draw_square(i)



trl.mainloop()
