import sys
sys.stdin = open('G.txt')

def get_case(N):
    clothes = dict()

    for _ in range(N):
        # 이름, 종류
        name, cat = input().split()

        # 종류가 딕셔너리에 없다면 종류에 해당하는 리스트 생성
        if cat not in clothes.keys():
            clothes[cat] = []

        clothes[cat].append(name)

    # 경우의 수 구하기 : (개수 + 1) * (개수 + 1)
    count = 1 
    for v in clothes.values():
        count *= (len(v) + 1)
    
    # 전체 경우 빼주기
    return count - 1

T = int(input())

for tc in range(T):
    N = int(input())
    answer = get_case(N)
    print(answer)