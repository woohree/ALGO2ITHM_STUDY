import sys
sys.stdin = open('input.txt')
import re
# x+() 는 최소 1개 x의 반복으로 이루어진 전파의 집합
# (xyx)+() 는 괄호 내의 xyx의 반복으로 이루어진 전파의 집합
# { x | y } 는 x 혹은 y 를 의미하는 것으로,
# { 0+ | 1+ } 는 { 0 , 1 , 00 , 11 , 000 , 111 , … } 의 집합

# 즉 100+1+는 0과 1이 한 번 이상 반복되어야 하고
# | 는 01 또는 0+1+이 둘 중 하나 반복되어야 함을 말한다(혹은 둘 다).
# 그리고 그것이 반복되어야 한다.
tc = int(input())
for i in range(tc):
    A = input()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(A)
    if m: print("YES")
    else: print('NO')