import sys
sys.stdin = open('G.txt')

def get_present_count(string):
    present = 0
    # EW가 나란히 있다면 그곳에 선물 놓기
    for idx in range(len(string)):
        if string[idx-1] == 'E' and string[idx] == 'W':
            present += 1
    return present


n = int(input())
strings = list(input())
answer = get_present_count(strings)
print(answer)
