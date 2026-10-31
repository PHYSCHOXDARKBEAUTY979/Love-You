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



random.seed(10)

for y in range(220, -290, -23):
    x = -340

    while x < 340:
        message = random.choice(love)
        font_size = 11

        text_width = len(message) * 7

        central_x = x + text_width / 2

        if (inside_heart(x, y) and inside_heart(x + text_width, y) and inside_heart(central_x, y)):

            pen.goto(x, y)
            pen.color(random.choice([
                "#ff3333"
                "#ff4444"
                "#ff2222"
                "#ff6662"
            ]))