import turtle as t
size =100

def square(color):
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
def change_posithiony(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
initial_x =-637.8
initial_y = 397.8
t.speed(1000)
for i in range(10):
    # change_posithiony(initial_x,initial_y)
    for j in range(12):
        if (i+j) %2 ==0:
            color='orange'
        else:
            color="black"
        x_coord=size*j+initial_x
        change_posithiony(x_coord,initial_y)
        square(color)
    initial_y=initial_y-size


t.done()