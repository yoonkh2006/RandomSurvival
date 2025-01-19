from random import *


perc = 95
cnt = 0
total = 0
reward = 1


def survival() :
  global perc, cnt, reward, total
  n = randint(1, 100)
  if n <= perc:
    perc -= 5
    print("생존!")
    reward *= 2
    cnt += 1
    go_stop = input(f"더 가시겠습니까? (y/n) 생존 확률은 {perc}%입니다. ")
    if go_stop == "y":
      survival()
    else:
      total += reward
      print("게임 종료")
      print(f"누적 보상: {total}")
      perc = 95
      reward = 1
      survival()

  elif perc == 10:
    print("클리어!")
    print(f"시행 횟수는 {cnt}회 입니다.")
    print(f"누적 보상: {total}")

  else:
    reward = 0
    print("사망!")
    print(f"시행 횟수는 {cnt}회 입니다.")
    print(f"누적 보상: {total}")
    again = input("다시하시겠습니까? (y/n) ")

    if again == "y":
      perc = 95
      reward = 1
      survival()
    else:
      print("게임 종료")

survival()