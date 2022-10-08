import sys
sys.stdin =open('input.txt')

N = int(input())
cnt = 0
for n in range(N):
    A = input()
    alpha = []  # 지금까지 나온 알파벳 있는 곳
    current = 0 # 직전에 확인한 알파벳
    cnt_idx = 0 # 글자 길이 확인,종료조건
    binary = 1 # 1이면 cnt에 +1 0이면 +0
    for i in A:
        cnt_idx += 1
        if i != current: #지난번에 본 글자와 지금 본 글자가 다를때
            if i in alpha: #알파벳 리스트 안에 지금 글자가 있으면
                binary = 0 #false로 변경
            else: #알파벳 리스트 안에 지금 글자가 없으면
                alpha += [i] #알파벳 리스트 안에 추가하고
                current = i #지금 보고있는 글자가 어떤건지 기록을 남긴다
                if cnt_idx == len(A) and binary == 1: #글자 길이와 종료조건이 일치하면서 True면
                    cnt+= 1 #+1
        elif cnt_idx == len(A) and binary == 1: #글자 길이와 종료조건이 일치하면서 True면 +1
            cnt += 1
print(cnt)