import sys
sys.stdin = open('L.txt')


# 생각보다 오래 걸린 이유: 진실을 아는 애들이랑 같이 있던 모르는 애들이 다시 알게 되는 점...
# 문제가 생각보다 까다로웠다.
N, M = map(int, input().split())
len_trumans, *trumans = list(map(int, input().split()))
trumans = set(trumans)
cnt = 0
party_people = []
for _ in range(M):
    len_party, *people = list(map(int, sys.stdin.readline().rstrip().split()))
    party_people.append(set(people))    # 집합타입으로 push

for _ in range(M):                      # 파티 수 만큼 반복하면서,
    for people in party_people:         # people 집합과
        if people & trumans:            # trumans의 교집합이 존재한다면,
            trumans |= people           # trumans에 더해주기(합집합)

for people in party_people:             # 파티 피플들 보면서,
    if not people & trumans:            # trumans와 교집합이 존재하지 않는다면,
        cnt += 1                        # 갈 수 있는 파티

print(cnt)


# 집합 안쓰고 하니까 순서에 따라서 변수가 너무 많았음
# trumans = {}
# party_people = []
# cnt = 0
# for i in range(len_trumans):
#     trumans[temp[i]] = 1
# for _ in range(M):
#     len_party, *people = list(map(int, sys.stdin.readline().rstrip().split()))
#     for j in range(len_party):
#         if trumans.get(people[j]):
#             for k in range(len_party):
#                 if not trumans.get(people[k]):
#                     trumans[people[k]] = 1
#             break
#     party_people.append(people)
# for people in party_people:
#     for p in people:
#         if trumans.get(p):
#             break
#     else:
#         cnt += 1
# print(cnt)
