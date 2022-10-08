import sys
sys.stdin = open('G.txt')

N = int(input())
numbers = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_value = -999999999999999999999
min_value = 99999999999999999999999999

def solution(number, idx, plus, minus, mul, div):
    global max_value, min_value
    if idx == N :
        max_value = max(max_value, number)
        min_value = min(min_value, number)
        return
    
    if plus > 0:
        solution(number + numbers[idx], idx+1, plus-1, minus, mul, div)
    if minus > 0:
        solution(number - numbers[idx], idx+1, plus, minus-1, mul, div)
    if mul > 0:
        solution(number * numbers[idx], idx+1, plus, minus, mul-1, div)
    if div > 0:
        solution(int(number / numbers[idx]), idx+1, plus, minus, mul, div-1)


solution(numbers[0], 1, plus, minus, mul, div)
print(max_value)
print(min_value)