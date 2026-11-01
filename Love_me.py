import turtle
import math
import random
import time
import pygame
import sys

screen = turtle.Screen()
screen.title("Love Heart")
screen.bgcolor("black")
screen.setup(width=1000, height= 850)
screen.tracer(0)
clock = pygame.time.Clock()

RED = (255, 65, 65)
BLACK =(0, 0, 0)

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


def heart(x,y):
    x = x / 280
    y = y / 280

    return (x*x + y*y - 1)**3 - x*x*y**3 <= 0

random.seed(10)
letters = []

for y in range(220, -290, -23):
    x = -340

while x < 370:
    word = random.choice(love)
    width = font_size(word)[0]
    if all(heart(px, y)
        for px in (x, x + width / 2, x + width)):

        message = random.choice(love)
        font_size = 11

        text_width = len(message) * 7

        central_x = x + text_width / 2

        if (heart(x, y) and heart(x + text_width, y) and heart(central_x, y)):

            pen.goto(x, y)
            pen.color(random.choice([
                "#ff3333",
                "#ff4444",
                "#ff5555",
                "#ff2222",
                "#ff6666",
            ]))

pen.write( message, align="left", font=("Arial", font_size, "bold"))
x += text_width + 11

current = 0
frame = 0
running = True


while running:
    clock.tick(60)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 


screen.update()
turtle.done()