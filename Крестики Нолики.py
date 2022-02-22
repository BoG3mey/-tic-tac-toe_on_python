#Подключение модулей
from turtle import *
from random import randint
from math import *
#Создание переменных
game = 1
#Нолики
def a1():
    penup()
    goto(-45, 20)
    pendown()
    circle(30)
    setheading(0)
def a2():
    penup()
    goto(55, 20)
    pendown()
    circle(30)
    setheading(0)
def a3():
    penup()
    goto(155, 20)
    pendown()
    circle(30)
    setheading(0)
def a4():
    penup()
    goto(-45, -80)
    pendown()
    circle(30)
    setheading(0)
def a5():
    penup()
    goto(55, -80)
    pendown()
    circle(30)
    setheading(0)
def a6():
    penup()
    goto(155, -80)
    pendown()
    circle(30)
    setheading(0)
def a7():
    penup()
    goto(-45, -180)
    pendown()
    circle(30)
    setheading(0)
def a8():
    penup()
    goto(55, -180)
    pendown()
    circle(30)
    setheading(0)
def a9():
    penup()
    goto(155, -180)
    pendown()
    circle(30)
    setheading(0)
#Крестики
def b1():
    penup()
    goto(-85, 85)
    pendown()
    right(45)
    forward(100)
    penup()
    goto(-15, 85)
    pendown()
    right(90)
    forward(100)
    setheading(0)
def b2():
    penup()
    goto(25, 85)
    pendown()
    right(45)
    forward(100)
    penup()
    goto(85, 85)
    pendown()
    right(90)
    forward(100)
    setheading(0)
def b3():
    penup()
    goto(125, 85)
    pendown()
    right(45)
    forward(100)
    penup()
    goto(185, 85)
    pendown()
    right(90)
    forward(100)
    setheading(0)
def b4():
    penup()
    goto(-85, -15)
    pendown()
    right(45)
    forward(100)
    penup()
    goto(-15, -15)
    pendown()
    right(90)
    forward(100)
    setheading(0)
def b5():
    penup()
    goto(25, -15)
    pendown()
    right(45)
    forward(100)
    penup()
    goto(85, -15)
    pendown()
    right(90)
    forward(100)
    setheading(0)
def b6():
    penup()
    goto(125, -15)
    pendown()
    right(45)
    forward(100)
    penup()
    goto(185, -15)
    pendown()
    right(90)
    forward(100)
    setheading(0)
def b7():
    penup()
    goto(-85, -115)
    pendown()
    right(45)
    forward(100)
    penup()
    goto(-15, -115)
    pendown()
    right(90)
    forward(100)
    setheading(0)
def b8():
    penup()
    goto(25, -115)
    pendown()
    right(45)
    forward(100)
    penup()
    goto(85, -115)
    pendown()
    right(90)
    forward(100)
    setheading(0)
def b9():
    penup()
    goto(125, -115)
    pendown()
    right(45)
    forward(100)
    penup()
    goto(185, -115)
    pendown()
    right(90)
    forward(100)
    setheading(0)
def c1():
    penup()
    goto(-100, 50)
    pendown()
    forward(300)
    setheading(0)
def c2():
    penup()
    goto(-100, -50)
    pendown()
    forward(300)
    setheading(0)
def c3():
    penup()
    goto(-100, -150)
    pendown()
    forward(300)
    setheading(0)
def c4():
    penup()
    goto(-50, 100)
    right(90)
    pendown()
    forward(300)
    setheading(0)
def c5():
    penup()
    goto(50, 100)
    right(90)
    pendown()
    forward(300)
    setheading(0)
def c6():
    penup()
    goto(150, 100)
    right(90)
    pendown()
    forward(300)
    setheading(0)
def c7():
    penup()
    goto(-100, 100)
    right(45)
    pendown()
    forward(425)
    setheading(0)
def c8():
    penup()
    goto(200, 100)
    right(135)
    pendown()
    forward(425)
    setheading(0)
#Меню и сама игра
while game == 1:
    #Создание переменных
    a11 = 0 
    a12 = 0
    a13 = 0
    a14 = 0 
    a15 = 0
    a16 = 0 
    a17 = 0 
    a18 = 0 
    a19 = 0
    a21 = 0
    a22 = 0
    a23 = 0
    a24 = 0
    a25 = 0
    a26 = 0
    a27 = 0
    a28 = 0
    a29 = 0
    b21 = 0
    b22 = 0
    b23 = 0
    b24 = 0
    b25 = 0
    b26 = 0
    b27 = 0
    b28 = 0
    b29 = 0
    bot1 = 0
    bot = 0
    bot2 = 0
    you = 0
    #Игровое поле
    color('black')
    pensize(3)
    penup()
    goto(-100, -100)
    pendown()
    forward(300)
    penup()
    goto(-100, 0)
    pendown()
    forward(300)
    penup()
    goto(0, 100)
    pendown()
    right(90)
    forward(300)
    penup()
    goto(100, 100)
    pendown()
    forward(300)
    color('red')
    pensize(10)
    left(90)
    print('Привет, ты попал в игру "Крестики Нолики"')
    print('Выбери место куда походить цифрами от 1 - 9(0 - завершить)\n 1 2 3\n 4 5 6\n 7 8 9')
    t = int(input(' '))
    while t !=0:
        #Ваши ходы
        while you == 0:
            if t == 1 and a11 >= 1:
                print('Это место занято')
                print('Выбери место куда походить цифрами от 1 - 9(0 - завершить)\n 1 2 3\n 4 5 6\n 7 8 9')
                t = int(input(' ')) 
            if t == 2 and a12 >= 1:
                print('Это место занято')
                print('Выбери место куда походить цифрами от 1 - 9(0 - завершить)\n 1 2 3\n 4 5 6\n 7 8 9')
                t = int(input(' ')) 
            if t == 3 and a13 >= 1:
                print('Это место занято')
                print('Выбери место куда походить цифрами от 1 - 9(0 - завершить)\n 1 2 3\n 4 5 6\n 7 8 9')
                t = int(input(' ')) 
            if t == 4 and a14 >= 1:
                print('Это место занято')
                print('Выбери место куда походить цифрами от 1 - 9(0 - завершить)\n 1 2 3\n 4 5 6\n 7 8 9')
                t = int(input(' ')) 
            if t == 5 and a15 >= 1:
                print('Это место занято')
                print('Выбери место куда походить цифрами от 1 - 9(0 - завершить)\n 1 2 3\n 4 5 6\n 7 8 9')
                t = int(input(' ')) 
            if t == 6 and a16 >= 1:
                print('Это место занято')
                print('Выбери место куда походить цифрами от 1 - 9(0 - завершить)\n 1 2 3\n 4 5 6\n 7 8 9')
                t = int(input(' ')) 
            if t == 7 and a17 >= 1:
                print('Это место занято')
                print('Выбери место куда походить цифрами от 1 - 9(0 - завершить)\n 1 2 3\n 4 5 6\n 7 8 9')
                t = int(input(' ')) 
            if t == 8 and a18 >= 1:
                print('Это место занято')
                print('Выбери место куда походить цифрами от 1 - 9(0 - завершить)\n 1 2 3\n 4 5 6\n 7 8 9')
                t = int(input(' ')) 
            if t == 9 and a19 >= 1:
                print('Это место занято')
                print('Выбери место куда походить цифрами от 1 - 9(0 - завершить)\n 1 2 3\n 4 5 6\n 7 8 9')
                t = int(input(' ')) 
            else:
                if t == 1 and a11 < 1:
                    a1()
                    a11 += 1
                    a21 += 1
                    break
                if t == 2 and a12 < 1:
                    a2()
                    a12 += 1
                    a22 += 1
                    break
                if t == 3 and a13 < 1:
                    a3()
                    a13 += 1
                    a23 += 1
                    break
                if t == 4 and a14 < 1:
                    a4()
                    a14 += 1
                    a24 += 1
                    break
                if t == 5 and a15 < 1:
                    a5()
                    a15 += 1
                    a25 += 1
                    break
                if t == 6 and a16 < 1:
                    a6()
                    a16 += 1
                    a26 += 1
                    break
                if t == 7 and a17 < 1:
                    a7()
                    a17 += 1
                    a27 += 1
                    break
                if t == 8 and a18 < 1:
                    a8()
                    a18 += 1
                    a28 += 1
                    break
                if t == 9 and a19 < 1:
                    a9()
                    a19 += 1
                    a29 += 1
                    break
        if a21 == 1 and a22 == 1 and a23 == 1:
            print('Вы победили')
            c1()
            break
        if a21 == 1 and a24 == 1 and a27 == 1:
            print('Вы победили')
            c4()
            break
        if a21 == 1 and a25 == 1 and a29 == 1:
            print('Вы победили')
            c7()
            break
        if a22 == 1 and a25 == 1 and a28 == 1:
            print('Вы победили')
            c5()
            break
        if a23 == 1 and a26 == 1 and a29 == 1:
            print('Вы победили')
            c6()
            break
        if a23 == 1 and a25 == 1 and a27 == 1:
            print('Вы победили')
            c8()
            break
        if a24 == 1 and a25 == 1 and a26 == 1:
            print('Вы победили')
            c2()
            break
        if a27 == 1 and a28 == 1 and a29 == 1:
            print('Вы победили')
            c3()
            break
        #Ходы бота
        while bot1 == 0:
            bot = randint(1,9)
            print('BOT ходит', bot)
            if bot == 1 and a11 < 1:
                b1()
                a11 += 1
                b21 += 1
                break
            if  bot == 2 and a12 < 1:
                b2()
                a12 += 1
                b22 += 1
                break
            if  bot == 3 and a13 < 1:
                b3()
                a13 += 1
                b23 += 1
                break
            if bot == 4 and a14 < 1:
                b4()
                a14 += 1
                b24 += 1
                break
            if bot == 5 and a15 < 1:
                b5()
                a15 += 1
                b25 += 1
                break
            if bot == 6 and a16 < 1:
                b6()
                a16 += 1
                b26 += 1
                break
            if bot == 7 and a17 < 1:
                b7()
                a17 += 1
                b27 += 1
                break
            if bot == 8 and a18 < 1:
                b8()
                a18 += 1
                b28 += 1
                break
            if bot == 9 and a19 < 1:
                b9()
                a19 += 1
                b29 += 1
                break
                
        if b21 == 1 and b22 == 1 and b23 == 1:
            print('BOT победил')
            c1()
            break
        if b21 == 1 and b24 == 1 and b27 == 1:
            print('ВOT победил')
            c4()
            break
        if b21 == 1 and b25 == 1 and b29 == 1:
            print('ВOT победил')
            c7()
            break
        if b22 == 1 and b25 == 1 and b28 == 1:
            print('ВOT победил')
            c5()
            break
        if b23 == 1 and b26 == 1 and b29 == 1:
            print('ВOT победил')
            c6()
            break
        if b23 == 1 and b25 == 1 and b27 == 1:
            print('ВOT победил')
            c8()
            break
        if b24 == 1 and b25 == 1 and b26 == 1:
            print('ВOT победил')
            c2()
            break
        if b27 == 1 and b28 == 1 and b29 == 1:
            print('ВOT победил')
            c3()
            break
        print('Выбери место куда походить цифрами от 1 - 9(0 - завершить)\n 1 2 3\n 4 5 6\n 7 8 9')
        t = int(input(' ')) 
        if a21 == 1 and a22 == 1 and a23 == 1:
            print('Вы победили')
            c1()
            break
        if a21 == 1 and a24 == 1 and a23 == 1:
            print('Вы победили')
            c4()
            break
        if a21 == 1 and a25 == 1 and a29 == 1:
            print('Вы победили')
            c7()
            break
        if a22 == 1 and a25 == 1 and a28 == 1:
            print('Вы победили')
            c5()
            break
        if a23 == 1 and a26 == 1 and a29 == 1:
            print('Вы победили')
            c6()
            break
        if a23 == 1 and a25 == 1 and a27 == 1:
            print('Вы победили')
            c8()
            break
        if a24 == 1 and a25 == 1 and a26 == 1:
            print('Вы победили')
            c2()
            break
        if a27 == 1 and a28 == 1 and a29 == 1:
            print('Вы победили')
            c3()
            break

    print('Хочешь сыграть ещё раз?')
    print('1 - Да, 2 - Нет')
    game = int(input(' '))
    clear()
