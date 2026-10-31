import math
import turtle
import random
import time

screen = turtle.Screen()
screen.title("Love Heart")
screen.bgcolor("black")
screen.setup(width=1000, height= 850)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

love = [
    "I Love you", "Te amo", "Je t'aime", "Eu te amo",
    "Ti amo", "Ich liebe dich", "Aku cinta kamu",
    "愛你", "愛している", "Люблю тебя", "তোমাকে ভালোবাসি"
    "사랑해요", "Älskar dig", "Aku mencintaimu",
    "Kontan twa", "Elsker dig"
    "爱你", "ⵃⴻⵎⵎⵍⴻⵖⵯⴽⴻⵎ", "Älskar dig",
    "Уазын дæ", "Yêu bạn"
]


def inside_heart(x,y):
    x = x / 280
    y = y / 280

    return (x*x + y*y - 1)**3 - x*x*y**3
<= 0


random.seed(10)