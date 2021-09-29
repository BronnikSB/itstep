# from turtle import *
# color('red','yellow')
# begin_fill()
# while True:
#     forward(100)
#     left(170)
#     if abs(pos())<1:
#         break
# end_fill()
# mainloop()
#---------------------------------------------
# from turtle import *
# speed(100)
# for i in range (1, 300, 2):
#     forward(i)
#     left(i)
#--------------------------------------------
# from turtle import *
#
# shape("turtle")
# speed(0.6)
# forward(50)
# left(180)
# right(53.13)
# forward(30)
# left(90)
# forward(40)
#--------------------------------------------
# Движение черепахи
# ---------------------------- Двигаться и рисовать
# forward() | fd()
# backward() | bk() | back()
# right() | rt()
# left() | lt()
# goto() | setpos() | setposition()
# setx()
# sety()
# setheading() | seth()
# home() ---------------------- Переместить черепаху в исходную точку
# circle() ------------------- круг
# dot() ---------------------------- нарисовать точку в аргументах передавать размер и цвет
#
# speed()
# -------------------------- Рассказать о состоянии Черепахи
# position() | pos()
#
# distance()
# Управление Pen
# --------------------------- Состояние рисования
# pendown() | pd() | down() ----------------------- опустить карандаш
# penup() | pu() | up() ----------------- поднять карандаш
# pensize() | width() ------------------ размер карандаша
#
#
# -------------------------- Управление цветом
# color()
# pencolor()
# fillcolor()
# --------------------------- Заполнение
# filling()
# begin_fill()
# end_fill()
# ---------------------------- Больше контроля рисования
# reset()
# clear()
# write()
# Состояние черепахи
# --------------------------Видимость
# showturtle() | st()
# hideturtle() | ht()
# isvisible()
# Внешний вид
# shape() --------------------------- форма
#
# shapesize() | turtlesize() -------------------- размер формы
#
#
# Методы TurtleScreen/Screen¶
#-------------------------------------- Управление окном
# bgcolor() ---------------------- цвет фона
# bgpic() ------------------------- картинка фона
# clear() | ----------------------- clearscreen()
# reset() | ----------------------- resetscreen()
# screensize() ---------------- размер экрана
# -------------------Управление анимацией
# delay()
# tracer()
# update()
#
# mainloop() | done() задержка экрана
from turtle import *
fillcolor("black")
begin_fill()
speed(5)
forward(300)
left(90)
forward(200)
right(90)
forward(30)
right(90)
forward(200)
left(90)
forward(20)
left(90)
forward(200)
right(90)
forward(40)
left(150)
forward(400)
left(90)
forward(232)
left(120)
forward(52)
right(90)
forward(199)
left(90)
forward(20)
up()
goto(20, 100)
down()
for i in range(4):
    forward(60)
    left(90)
up()
goto(100, 100)
down()
for i in range(4):
    forward(60)
    left(90)
up()
goto(180, 200)
down()
forward(100)
right(90)
forward(190)
right(90)
forward(100)
right(90)
forward(190)
mainloop()