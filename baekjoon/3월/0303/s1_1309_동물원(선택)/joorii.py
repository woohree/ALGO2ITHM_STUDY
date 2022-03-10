import sys
sys.stdin = open('M.txt')


def lion_hen():
    count = 1
    count_three = 0
    count_two = 0

    for n in range(N + 1):
        if n == 0:
            continue
        elif n == 1:
            count_three = 1
        else:
            count_three, count_two = count_three + count_two, count_two + (count_three * 2)

        count = (3 * count_three) + (2 * count_two)

    return count


N = int(input())

print(lion_hen() % 9901)
