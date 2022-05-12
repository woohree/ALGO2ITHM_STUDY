import sys
sys.stdin = open('B.txt')

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

        numbers = []
        for i in range(len(friends)):
            if f1 in friends[i] or f2 in friends[i]:
                numbers.append(i)
        temp = set()
        for number in numbers:
            temp = temp | friends[number]
        friends[numbers[0]] = temp
        print(len(temp))
