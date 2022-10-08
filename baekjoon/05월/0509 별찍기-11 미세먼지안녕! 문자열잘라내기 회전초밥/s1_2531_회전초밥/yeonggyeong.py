import sys
sys.stdin = open('G.txt')


def solution(sushi):
    dic = dict()
    for i in range(N):
        # 연속된 k개 선택
        start = i
        end = (i + K) % N
        if end < start:
            eat = sushi[start:] + sushi[:end]
        else:
            eat = sushi[start:end]

        # 쿠폰번호 추가
        eat.append(c)
        kind = len(set(eat))

        # 최댓값일때
        if kind == K + 1:
            return K + 1
        
        # 갯수 딕셔너리 형태로 만들기
        if dic.get(kind):
            dic[kind] += 1
        else:
            dic[kind] = 1

    return max(dic.keys())


# 초밥 접시 수 / 가짓 수 / 연속해서 먹는 접시 수 / 쿠폰번호
N, d, K, c = map(int, sys.stdin.readline().split())

sushi = [int(sys.stdin.readline()) for _ in range(N)]
print(solution(sushi))
