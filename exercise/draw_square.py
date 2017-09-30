# -*- coding: utf-8 -*-
import turtle


def draw():
    window = turtle.Screen()
    window.bgcolor("red")  # 设置画布背景色

    paint1 = turtle.Turtle()
    paint1.shape("turtle")  # 可以是arrow、turtle、circle、square、triangle、classic
    paint1.color("yellow")  # 设置画笔颜色
    paint1.speed(5)  # 0到10的范围，逐渐变快，默认为3

    for i in range(0, 36):
        i = 0
        while i < 4:
            paint1.forward(100)
            paint1.right(90)
            i = i + 1
        paint1.right(10)

    paint2 = turtle.Turtle()
    paint2.shape("arrow")
    paint2.color("blue")
    paint2.circle(100)

    window.exitonclick()


draw()
