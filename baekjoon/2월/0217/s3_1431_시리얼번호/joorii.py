import sys
sys.stdin = open('M.txt')


def sorted_by_serial():
    for i in range(N - 1):
        for j in range(i + 1, N):
            # 길이순으로 정렬하기
            if len(serials[i]) > len(serials[j]):
                serials[i], serials[j] = serials[j], serials[i]

            # 길이가 같다면
            elif len(serials[i]) == len(serials[j]):
                sum_i = sum_j = 0
                # 숫자끼리 더해서 작은 순으로 정렬
                for k in range(len(serials[i])):
                    if serials[i][k].isdigit():
                        sum_i += int(serials[i][k])
                    if serials[j][k].isdigit():
                        sum_j += int(serials[j][k])
                if sum_i > sum_j:
                    serials[i], serials[j] = serials[j], serials[i]

                # 자릿수의 합이 같다면, 사전순 정렬
                elif sum_i == sum_j:
                    for k in range(len(serials[i])):
                        if serials[i][k] > serials[j][k]:
                            serials[i], serials[j] = serials[j], serials[i]
                            break   # 가장 먼저 나온 문자로 사전 순 정렬하기 위함
                        elif serials[i][k] < serials[j][k]:
                            break   # 순서 바꿀 필요 없음

    for serial in serials:
        print(''.join(serial))


T = int(input())

for tc in range(T):
    N = int(input())
    serials = [list(map(str, input())) for _ in range(N)]

    print('0x08'.isdigit())
