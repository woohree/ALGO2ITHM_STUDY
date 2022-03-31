import sys
sys.stdin = open('B.txt')

# 1. list 사용해서 인풋받고, dfs로 값 구함 -> 메모리초과
# 2. dict 사용해서 인풋, dfs -> 시간초과
# 3. dict 사용해서 인풋, 조합 -> 메모리초과
# 4. dict 사용, 관계식? 찾아서 계산
# 미칠뻔 ㅎ

T = int(input())
for _ in range(T):
    n = int(input())

    # dict 사용해서 인풋 받기
    # 옷의 이름은 필요 없으므로 카운트만 한다.
    clothes = {}
    for i in range(n):
        cloth, kind = input().split()
        if kind not in clothes:
            clothes[kind] = 1
        else:
            clothes[kind] += 1

    # 옷 같은 종류 당 예를 들어 2개가 있을 경우,
    # 그 옷은 한 번씩 입거나(2), 둘 다 안 입을 경우(1) 가 있으므로
    # 2+1 해서 answer 에 곱한다.
    answer = 1
    for c in clothes:
        answer *= clothes[c] + 1
    print(answer - 1)
