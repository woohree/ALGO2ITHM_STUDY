import sys
sys.stdin = open('input.txt')


# 이거 뭔가 가지칠 수 있을 거 같은데..
# N이 30,000까지 있어서 시간초과 뜰 줄 알았는데 안뜨넹
def count_numbers(N, n):
    global max_cnt, max_numbers

    numbers = [N, n]
    cnt = 2
    # 앞앞놈보다 앞놈이 더 크면 종료! (다음 항이 음수가 되버림)
    while numbers[cnt-1] <= numbers[cnt-2]:
        new = numbers[cnt-2] - numbers[cnt-1]
        numbers.append(new)
        cnt += 1
    # 최대 갯수의 수 비교
    if cnt > max_cnt:
        max_cnt = cnt
        max_numbers = numbers


max_cnt = 0
max_numbers = []
N = int(input())
for n in range(N+1):
    count_numbers(N, n)
print(max_cnt)
print(' '.join(map(str, max_numbers)))