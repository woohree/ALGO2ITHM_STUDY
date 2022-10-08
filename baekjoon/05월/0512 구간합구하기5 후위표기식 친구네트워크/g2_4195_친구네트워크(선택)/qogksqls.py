import sys
sys.stdin = open('B.txt')


def find_set():
    return


def union():
    return


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    F = int(sys.stdin.readline().rstrip())
    friends = {}
    for f in range(F):
        f1, f2 = sys.stdin.readline().rstrip().split()



'''
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    F = int(sys.stdin.readline().rstrip())
    friends = {}
    for f in range(F):
        f1, f2 = sys.stdin.readline().rstrip().split()
        if f == 0:
            friends[0] = {f1: 1}
            friends[0][f2] = 1
        else:
            for i in range(len(friends)):
                if friends[i].get(f1) or friends[i].get(f2):
                    friends[i][f2] = 1
                    friends[i][f1] = 1
                else:
                    friends[i+1] = {f1: 1}
                    friends[i+1][f2] = 1

        numbers = []
        for i in range(len(friends)):
            if friends[i].get(f1) or friends[i].get(f2):
                numbers.append(i)
        temp = set()
        for number in numbers:
            a = set(friends[number].keys())
            temp = temp | set(a)
        print(len(temp))
        ttemp = {}
        for t in temp:
            ttemp[t] = 1
        friends[numbers[0]] = ttemp
'''
'''
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    F = int(sys.stdin.readline().rstrip())
    friends = {}
    for f in range(F):
        f1, f2 = sys.stdin.readline().rstrip().split()
        len_friends = len(friends)
        if f == 0:
            friends[0] = set(f1)
            friends[0].add(f2)
        else:
            flag = 1
            for i in range(len_friends):
                if f1 in friends[i] or f2 in friends[i]:
                    friends[i].add(f1)
                    friends[i].add(f2)
                    flag = 0
            if flag:
                friends[len_friends] = set(f1)
                friends[len_friends].add(f2)

        numbers = [1, 2]
        for i in range(len(friends)):
            if f1 in friends[i] or f2 in friends[i]:
                numbers.append(i)
        temp = set()
        for number in numbers:
            temp = temp | friends[number]
        friends[numbers[0]] = temp
        print(len(temp))
'''