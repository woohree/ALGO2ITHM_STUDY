import sys
sys.stdin =open('input.txt')

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a = sorted(a) #정렬!
b.sort(reverse=True) #뒤집어!

print(a)
print(b)
summ = 0
for i in range(n):
    summ += a[i]*b[i] #곱해!

print(summ)