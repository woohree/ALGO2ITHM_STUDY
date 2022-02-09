
def plus(number):

    answer = [[1, 0, 0],
            [1, 1, 0],
            [1, 1, 1], ]

    for _ in range(number-3):
        answer.append([0,0,0])

    for num in range(3,number):
        answer[num][0] = 1
        answer[num][1] = answer[num-2][0] + answer[num-2][1]
        answer[num][2] = answer[num-3][0] + answer[num-3][1] + answer[num-3][2]

    return sum(answer[number-1])

inp = int(input())

for i in range(inp):
    n = int(input())
    print(plus(n))