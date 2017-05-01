__author__ = 'xyx'
#投掷三个骰子，让用户猜大小。骰子总和11-18为大，3-10为小。用户初始资金1000，每次猜要下注，猜对加这笔钱，猜错扣掉，本钱为0时结束。
import random

def  roll_dice(numbers=3,points=None):
    if points==None:
        points=[]
    while numbers>0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers-1
    return points

def roll_result(points):
        big  =   11<=sum(points)<=18
        small= 3<=sum(points)<=10
        if big:
            return 'big'
        if small:
            return 'small'

def game(money):
    while money>0:
        print('pay?')
        pay = int(input())
        print('big or small?')
        choice=input()


        if choice == 'big'or choice=='small':
            points = roll_dice()
            print(sum(points))
            result = choice == roll_result(points)
            if result:
                print('win')
                money = money + pay
                print(money)
            else:
                print('lose')
                money = money - pay
                print(money)
        else:
            print('error')
            game(money)
money=1000
game(money)


