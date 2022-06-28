import sys
sys.stdin = open('B.txt')


def factorization():
    for k in range(2, int(length**0.5) + 1):
        if not length % k:
            factors.append(k)
            if length // k not in factors:
                factors.append(length // k)
    return


while 1:
    text = sys.stdin.readline().rstrip()
    if text == '.':
        break
    length = len(text)
    factors = [1, length]
    factorization()
    factors.sort()
    my_max = 0
    for L in factors:
        count, flag = 0, 1
        t = text[:L]
        for i in range(0, length - L + 1, L):
            b = text[i:i + L]
            if t == text[i:i + L]:
                count += 1
            else:
                flag = 0
                break
        if flag:
            my_max = max(my_max, count)
        if my_max >= length // L:
            break
    print(my_max)
