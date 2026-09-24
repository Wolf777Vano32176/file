
import turtle as t


t.speed(100)
def change_posithiony(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
initial_x =-637.8
initial_y = 397.8
size = 10
number=29
color = "black"
color2 = "white"
def square(color):
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
# change_posithiony(a1,b1)
def first_row(x,y):
    change_posithiony(x, y)
    for i in range(number):
        square(color=color2)
        t.forward(size)
        square(color=color)
        t.forward(size)
def second_row(x,y):
    change_posithiony(x, y)
    for i in range(number):
        square(color=color)
        t.forward(size)
        square(color=color2)
        t.forward(size)
# first_row(-600,297)
# second_row(-600,197)
# first_row(-600,97)
# second_row(-600,-3)
# first_row(-600,-103)
# second_row(-600,-203)
# first_row(-600,-300)
# second_row(-600,-400)
for i in range(number):
    first_row(initial_x,initial_y)
    initial_y -= size
    second_row(initial_x,initial_y)
    initial_y -= size
# for i in range(4):
#     square(color = "black")
#     t.forward(100)
#     square(color = "orange")
#     t.forward(100)
# change_posithiony(-640,siz)
# for i in range(4):
#     square(color = "orange")
#     t.forward(100)
#     square(color = "black")
#     t.forward(100)
# change_posithiony(-640,197)
# for i in range(4):
#     square(color="black")
#     t.forward(100)
#     square(color="orange")
#     t.forward(100)
# change_posithiony(-640, 97)
# for i in range(4):
#     square(color="orange")
#     t.forward(100)
#     square(color="black")
#     t.forward(100)
# change_posithiony(-640, -3)
# for i in range(4):
#     square(color="black")
#     t.forward(100)
#     square(color="orange")
#     t.forward(100)
# change_posithiony(-640, -103)
# for i in range(4):
#         square(color="orange")
#         t.forward(100)
#         square(color="black")
#         t.forward(100)
# change_posithiony(-640, -203)
# for i in range(4):
#         square(color="black")
#         t.forward(100)
#         square(color="orange")
#         t.forward(100)
# change_posithiony(-640, -303)
# for i in range(4):
#         square(color="orange")
#         t.forward(100)
#         square(color="black")
#         t.forward(100)
# change_posithiony(-640, -403)
# for i in range(4):
#         square(color="black")
#         t.forward(100)
#         square(color="orange")
#         t.forward(100)
# change_posithiony(-640, -503)
# for i in range(4):
#         square(color="orange")
#         t.forward(100)
#         square(color="black")
#         t.forward(100)
t.done()
