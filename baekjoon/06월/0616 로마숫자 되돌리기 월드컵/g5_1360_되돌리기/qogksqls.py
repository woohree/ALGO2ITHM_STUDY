import sys
sys.stdin = open('B.txt')

N = int(sys.stdin.readline().rstrip())
memory = {}
result = ''
for _ in range(N):
    order, text, sec = sys.stdin.readline().rstrip().split()
    sec = int(sec)
    if order == 'type':
        result += text
    else:
        text = int(text)
        k = list(memory.keys())
        for i in range(len(k)-1, -1, -1):
            if k[i] < sec - text:
                result = memory[k[i]]
                break
        else:
            result = ''
    memory[sec] = result

print(result)
