import sys
sys.stdin = open('B.txt')

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

# 1. 첫 번째 문자열을 문자 별로 인덱스를 저장하는 dict를 만들었다.
#    => {'A': [0, 2], 'C': [1], 'Y': [3], 'K': [4], 'P': [5]}
# 2. 두 번째 문자열에서 단어 하나씩 꺼내 확인
sentence1 = {}
for s in range(len(s1)):
    if sentence1.get(s1[s]):
        sentence1[s1[s]].append(s)
    else:
        sentence1[s1[s]] = [s]

# 3. 첫 번째 문자열에 존재하는 단어이면 저장되어 있는 index를 확인하여, 뒷 순서부터 dp에 저장한다.
# 4. 저장하는 방식은 0번째부터 해당 index 번 까지 중 최댓값을 구하여 1을 더한 값을 dp에 저장한다.
# 5. max안에 slice 설정 때문에 index가 0인 경우만 따로 계산해준다.
dp = [0] * len(s1)
for s in s2:
    if sentence1.get(s):
        for i in range(len(sentence1[s])-1, -1, -1):
            # index가 0보다 큰 경우
            if sentence1[s][i] > 0:
                dp[sentence1[s][i]] = max(dp[0:sentence1[s][i]]) + 1

            # index가 0인 경우
            else:
                if sentence1[s][i] != -1:
                    dp[sentence1[s][i]] += 1
                    sentence1[s][i] = -1
                    # => {'A': [-1, 2], 'C': [1], 'Y': [3], 'K': [4], 'P': [5]}
                    break

# 결과: pypy 로 2000ms 소요
#      python3는 95%쯤에서 시간초과
print(max(dp))
