import sys
sys.stdin = open('G.txt')

string = input()
key = input()

stack = []

for i in range(len(string)):
    stack.append(string[i])
    
    # 폭발문자의 마지막 문자가 같을때 앞으로 돌아가서 확인
    if stack[-1] == key[-1] and stack[-len(key):] == list(key):
        for j in range(len(key)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
