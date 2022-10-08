import sys
sys.stdin = open('M.txt')


N = int(sys.stdin.readline())
results = [(0, '')]

for _ in range(N):
    command, text, time = sys.stdin.readline().split()
    if command == 'type':
        results.append((int(time), results[-1][1] + text))
    else:
        t = int(time) - int(text) - 1
        if t <= 0:
            results.append((int(time), ''))
        for i in range(len(results) - 1, -1, -1):
            if results[i][0] <= t:
                results.append((int(time), results[i][1]))
                break
print(results[-1][1])
