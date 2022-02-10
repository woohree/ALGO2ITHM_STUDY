# 21:50 시작/ 22:20 1,2,3만 쓰는거 깨달음/ 23:00 1,2,3에서 자기 숫자만 있는 경우를 생각해냄 / 24:30 포기
# 재도전, 22:40 시작 / 24:20 끝
def plusman(number):
    result = 1 + (number//2) + (number//3) + (number//5)  #
    if number > 5:
        if number % 5 == 0:
            result += 3*((number//5)-1)
        elif number % 5 == 2:
            result += (number//5)
        elif number % 5 == 3:
            result += 2*(number//5)
        elif number % 5 == 4:
            result += 3*(number//5)
    return result

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    ans = plusman(n)
    print(ans)
