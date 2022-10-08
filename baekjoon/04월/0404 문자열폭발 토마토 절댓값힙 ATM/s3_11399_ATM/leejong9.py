N = int(input())
nums = list(map(int, input().split()))

nums.sort()
sum = 0
for i in nums:
    sum += i*N
    N -= 1 #1명 빼줌

print(sum)