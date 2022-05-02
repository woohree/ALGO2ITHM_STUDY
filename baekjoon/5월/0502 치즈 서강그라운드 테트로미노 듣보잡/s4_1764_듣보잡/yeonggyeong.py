import sys
sys.stdin = open('G.txt')

# input -> 3972
# sys.stdin.readline -> 132
N, M = map(int, sys.stdin.readline().split())
no_listen = set(sys.stdin.readline().rstrip() for _ in range(N))
no_see = set(sys.stdin.readline().rstrip() for _ in range(M))
# set들을 합집합한 후 정렬하기 위해 list
answer = list(no_listen & no_see)
answer.sort()
print(len(answer))
for i in answer:
    print(i)
