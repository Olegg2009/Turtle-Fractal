import turtle
from turtfunc import square
from turtfunc import cycle


turtle.hideturtle()
turtle.speed(100)

colorSquare = input("Цвет квадратов: ")
colorCycle = input("Цвет кругов: ")
dist = float(input("Первичная дистанция: "))
wgt = 1
rad = 0.5
tp = input("Тип(1 или 2): ")
while not (tp == "1" or tp == "2"):
    tp = input("Тип должен быть обязательно равен 1 или 2: ")
angle = int(input("Угол:"))

while True:
    if tp == 1:
        square(wgt, wgt, colorSquare)
        cycle(rad, colorCycle)
    else:
        cycle(rad, colorCycle)
        square(wgt, wgt, colorSquare)
    turtle.right(angle)
    turtle.penup()
    turtle.forward(dist)
    turtle.pendown()
    dist += dist / 16
    wgt += wgt / 16
    rad += rad / 16

