import sys
sys.stdin = open('M.txt')


def lucky_ticket():

    max_n = len(ticket_numbers) // 2
    max_result = result = 0
    for i in range(max_n, 0, -1):
        for j in range(0, len(ticket_numbers) - (2 * i) + 1):
            front_sum = back_sum = 0
            for k in range(i):
                front_sum += ticket_numbers[j + k]
                back_sum += ticket_numbers[j + i + k]

            if front_sum == back_sum:
                result = 2 * i
                break
        if max_result < result:
            max_result = result
            break

    return max_result


T = int(input())

for tc in range(T):
    ticket_numbers = list(map(int, input()))

    print(lucky_ticket())