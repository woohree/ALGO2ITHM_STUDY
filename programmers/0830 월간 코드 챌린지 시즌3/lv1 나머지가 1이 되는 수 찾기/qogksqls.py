def solution(n):
    x = 1
    while 1:
        if n % x == 1:
            break
        x += 1
    return x
