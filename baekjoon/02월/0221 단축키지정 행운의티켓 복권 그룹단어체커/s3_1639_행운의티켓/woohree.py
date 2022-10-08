import sys
sys.stdin = open('L.txt')

# 20분

def longest_lucky_number(ticket):
    length = len(ticket)

    if length % 2 == 0:  # 길이가 짝수
        # 가장 긴 길이의 행운 티켓 번호부터 체크
        for l in range(length, 1, -2):
            for idx in range(length - l + 1):
                # 행운의 티켓 길이의 절반을 각각 더해 비교하고 같다면 종료!
                if my_sum(ticket[idx:idx+(l//2)]) == my_sum(ticket[idx+(l//2):idx+l]):
                    return l
    else:  # 홀수
        # 가장 긴 길이의 행운 티켓 번호는 전체 길이 - 1
        for l in range(length-1, 1, -2):
            for idx in range(length - l + 1):
                if my_sum(ticket[idx:idx+(l//2)]) == my_sum(ticket[idx+(l//2):idx+l]):
                    return l
    return 0


def my_sum(numbers):
    ssum = 0
    for n in numbers:
        ssum += n
    return ssum

ticket = list(map(int, input()))
ans = longest_lucky_number(ticket)
print(ans)
