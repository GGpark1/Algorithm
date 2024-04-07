import turtle
import random

# 스크린 설정
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Aquarium")

t = turtle.Turtle()
t.speed(0)

# 물고기 그리기 함수, 조건에 따른 색상 변화
def draw_fish(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    # 크기에 따른 조건부 색상
    if size > 20:
        t.color("orange")
    else:
        t.color("gold")
    # 물고기 몸체 그리기
    t.begin_fill()
    for _ in range(3):  # 삼각형 몸체
        t.forward(size)
        t.left(120)
    t.end_fill()
    # 눈 그리기
    t.penup()
    t.forward(size * 0.5)
    t.left(90)
    t.forward(size * 0.2)
    t.pendown()
    t.color("black")
    t.dot(size * 0.1)
    t.right(90)  # 방향 초기화


# 해초 그리기 함수
def draw_algae(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("green")
    t.left(90)
    for _ in range(5):
        t.forward(20)
        t.right(20)
        t.forward(20)
        t.left(40)
    t.right(90)  # 방향 초기화


# 바위 그리기 함수
def draw_rock(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("gray")
    t.begin_fill()
    t.circle(size)
    t.end_fill()


# 물방울 그리기 함수
def draw_water_droplet(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    t.circle(5)
    t.end_fill()


# 메인 그리기 함수
def draw_aquarium():
    # 물고기 그리기, 수 증가
    for _ in range(10):  # 물고기 수 증가
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        size = random.randint(10, 30)
        draw_fish(x, y, size)

    # 해초 그리기
    for _ in range(10):
        x = random.randint(-300, 300)
        y = random.randint(-300, -100)
        draw_algae(x, y)

    # 바위 그리기, 수 감소
    for _ in range(10):  # 바위 수 감소
        x = random.randint(-300, 300)
        y = random.randint(-350, -250)
        size = random.randint(10, 20)
        draw_rock(x, y, size)

    # 물방울 그리기
    for _ in range(20):
        x = random.randint(-300, 300)
        y = random.randint(-100, 100)
        draw_water_droplet(x, y)


draw_aquarium()

t.hideturtle()
turtle.done()
