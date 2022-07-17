import sys
sys.stdin = open('W.txt')


S, P = input(), input()     # 주석 뭐..
if S.find(P) == -1:         # 그냥 find 메소드..
    print(0)
else:
    print(1)