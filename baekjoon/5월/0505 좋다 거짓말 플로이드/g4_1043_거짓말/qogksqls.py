import sys
sys.stdin = open('B.txt')

'''
30 분
1. 처음 주어진 진실을 아는 자들을 black_list 에 저장
2. parties 를 조회 하면서 black_list 에 저장된 번호가 있으면
   그 파티를 통째로 extend 하면서 pop 해주고 impossible_party 수를 카운트
3. 출력,,,  그리고 통과했는데 왜 됐지?
   골4 줍줍문제
'''

N, M = map(int, sys.stdin.readline().rstrip().split())
fact_check = list(map(int, sys.stdin.readline().rstrip().split()))
parties = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
len_parties = len(parties)


def solution():
    global black_list, impossible_party

    for i in range(len(parties)):
        for black in black_list:
            if black in parties[i]:
                black_list.extend(parties.pop(i))  # 처음부터 튜플로 저장하고 싶었는데 extent 쓰고 싶어서 list로 걍 함
                black_list = set(black_list)  # 중복 제거
                black_list = list(black_list)
                impossible_party += 1
                return


if fact_check[0] == 0:
    print(len_parties)
else:
    for p in parties:
        p.pop(0)

    black_list = []
    for i in range(1, fact_check[0] + 1):
        black_list.append(fact_check[i])

    impossible_party = 0
    while 1:
        temp = impossible_party

        solution()

        # while 탈출
        if impossible_party == temp:
            break
    print(len_parties - impossible_party)