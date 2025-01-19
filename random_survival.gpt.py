from random import randint

def survival_game():
    perc = 95  # 초기 생존 확률
    reward = 1  # 현재 라운드 보상
    total = 0  # 누적 보상
    cnt = 0  # 총 시행 횟수 (누적 유지)

    while True:
        # 게임 상태 간단히 표시
        print(f"[생존 확률: {perc}% | 라운드 보상: {reward} | 누적 보상: {total} | 총 시행 횟수: {cnt}]")
        n = randint(1, 100)  # 1~100 사이의 랜덤 숫자 생성

        if n <= perc:  # 생존 성공
            print("▶ 생존!")
            perc -= 5  # 생존 확률 감소
            reward *= 2  # 라운드 보상 두 배 증가
            cnt += 1  # 시행 횟수 증가

            go_stop = input("계속하시겠습니까? (y: 계속, n: 보상 저장 후 새 게임): ").lower()
            if go_stop == "n":
                total += reward  # 현재 보상을 누적 보상에 추가
                print(f"보상을 저장했습니다. [누적 보상: {total}]")
                perc = 95  # 생존 확률 초기화
                reward = 1  # 라운드 보상 초기화
                continue

        else:  # 생존 실패
            print("✘ 사망!")
            reward = 0
            print(f"총 시행 횟수: {cnt}회 | [누적 보상: {total}]")
            again = input("다시 시작하시겠습니까? (y: 새 게임, n: 종료): ").lower()
            if again == "y":
                perc = 95
                reward = 1
            else:
                print(f"게임 종료! 총 시행 횟수: {cnt}회 | 최종 누적 보상: {total}")
                break

        if perc < 10:  # 생존 확률 10% 도달
            print("★ 클리어!")
            total += reward
            print(f"총 시행 횟수: {cnt}회 | 최종 누적 보상: {total}")
            break

# 게임 실행
survival_game()
