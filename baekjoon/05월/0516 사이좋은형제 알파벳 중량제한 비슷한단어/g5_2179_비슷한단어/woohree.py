import sys
sys.stdin = open('L.txt')


N = int(input())
strs = [(sys.stdin.readline().rstrip(), i) for i in range(N)]   # [(문자열, 인덱스)]로 인풋받음
sorted_strs = sorted(strs)                                      # 문자열 기준 정렬

max_len = 0
check = [0] * N
for i in range(N-1):
    a, b = sorted_strs[i], sorted_strs[i+1]
    idx = 0
    while idx < min(len(a[0]), len(b[0])):                      # 앞에서부터 같은 문자인지 비교,
        if a[0][idx] == b[0][idx]:                              # 다른 문자 나오면 break!
            idx += 1
        else:
            break

    max_len = max(idx, max_len)                                 # idx = 접두사 길이, 최대 접두사 길이 갱신
    check[a[1]] = max(check[a[1]], idx)                         # a, b의 문자열 접두사 길이 각각 갱신해 저장
    check[b[1]] = max(check[b[1]], idx)

cnt = 0
ans = ''
for i in range(N):
    if check[i] == max_len:                                     # 접두사 길이가 최대 길이와 같으면,
        if ans:                                                 # 정렬안한 문자열 리스트에서 찾아다가 출력, 인덱스가 같음
            if strs[i][0][:max_len] == ans[:max_len]:
                print(strs[i][0])
                break
        else:
            ans = strs[i][0]
            print(ans)
