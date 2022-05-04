import sys
sys.stdin = open('G.txt')


def solution(people, parties):
    pop_index = []
    while parties:
        for idx, party in enumerate(parties):
            # 진실을 아는 사람들이 가는 파티
            if set(people) & set(party[1:]):
                # 그 파티에 가는 모든 사람들을 포함해주기
                people.extend(party[1:])
                # 그 파티 삭제
                pop_index.append(idx)
        if not pop_index:
            break
        for idx in pop_index[::-1]:
            parties.pop(idx)
            pop_index = []
    return len(parties)


N, M = map(int, sys.stdin.readline().split())
person = list(map(int, sys.stdin.readline().split()))
parties = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]

if person[0] == 0:
    print(M)
else:
    # 진실을 아는 사람 수/ 번호
    cnt, people = person[0], person[1:]
    answer = solution(people, parties)
    print(answer)