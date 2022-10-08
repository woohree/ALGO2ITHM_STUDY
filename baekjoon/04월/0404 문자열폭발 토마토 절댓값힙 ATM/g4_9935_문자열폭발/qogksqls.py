import sys
sys.stdin = open('B.txt')

# 1. while 과 for 문 사용해서 풀이 -> 안에 slice를 사용하였는데 시간복잡도가 N**2가 나오므로 시간 초과
# 2. stack을 이용해서 풀이 -> pass

strings = list(sys.stdin.readline().rstrip())
bomb = list(sys.stdin.readline().rstrip())

stack = []
for string in strings:
    stack.append(string)
    # stack 뒤에 폭탄 있는 경우
    if stack[-len(bomb):] == bomb:
        # 폭탄 길이만큼 stack 에서 pop
        for _ in range(len(bomb)):
            stack.pop()

print(''.join(stack)) if stack else print('FRULA')

''' 시간 복잡도가 N**2 이 나온다.
i = len(bomb) - 1  # 1
while i != len(strings):
    if bomb[-1] == strings[i]:
        if bomb == strings[i-len(bomb)+1:i+1]:  # strings[0:2]
            for _ in range(len(bomb)):
                strings.pop(i - len(bomb) + 1)
            i -= len(bomb) - 1
        else:
            i += 1
    else:
        i += 1
        
if strings:
    answer = ''.join(strings)
    print(answer)
else:
    print('FRULA')
'''
