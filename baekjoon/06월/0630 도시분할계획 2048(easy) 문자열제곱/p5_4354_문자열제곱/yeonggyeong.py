import sys
sys.stdin = open('G.txt')


while True:
    strings = sys.stdin.readline().rstrip()
    if strings == '.':
        break

    set_str = set(strings)
    set_length, length = len(set_str), len(strings)
    # 'abcdef' 처럼 다 다른 문자열일때
    if set_length == length:
        print(1)
    # 'aaaa' 같은 경우
    elif set_length == 1:
        print(length)
    else:
        # 문자열 길이가 2인 패턴부터 length//2까지의 패턴 반복
        for num in range(2, length//2 + 1):
            # 약수일때
            if not length % num:
                cnt = length // num
                # num = 2 / strings = abcdabcd / pattern = abababab
                pattern = strings[:num] * cnt
                if pattern == strings:
                    print(cnt)
                    break
        else:
            print(1)