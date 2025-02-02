import random

answer = random.randint(1, 100)

while True:
    num = int(input("정답을 입력하세요 >> "))

    if num > answer:
        print("Down!")

    elif num < answer:
        print("UP!")

    elif num == answer :
        print("정답입니다!")
        break