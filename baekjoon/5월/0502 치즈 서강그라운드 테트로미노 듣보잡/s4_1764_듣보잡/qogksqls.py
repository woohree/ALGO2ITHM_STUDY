import sys
sys.stdin = open('B.txt')

N, M = map(int, sys.stdin.readline().rstrip().split())
never_hear = {}
for _ in range(N):
    never_hear[sys.stdin.readline().rstrip()] = 1

never_hear_watch = []
for _ in range(M):
    never_watch = sys.stdin.readline().rstrip()
    if never_hear.get(never_watch):
        never_hear_watch.append(never_watch)

never_hear_watch.sort()
print(len(never_hear_watch))
for a in never_hear_watch:
    print(a)
