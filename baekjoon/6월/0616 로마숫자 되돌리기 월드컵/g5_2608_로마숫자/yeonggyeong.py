import sys
sys.stdin = open('G.txt')

string1 = input()
string2 = input()

dic = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' :1000}

def string_to_number(string):
    string = [dic[i] for i in string]
    if sorted(string, reverse=True) == string:
        return sum(string)
    else:
        lst = []
        for j in range(1, len(string)):
            if string[j] > string[j-1]:
                string[j-1] = string[j] - string[j-1]
                lst.append(j)
        for k in lst[::-1]:
            string.pop(k)
        return sum(string)

# 두 수 더하기 
total = string_to_number(string1) + string_to_number(string2)
print(total)
# 아라비아 숫자 만들기
# 결과 / 자릿수
result = ''
digit = len(str(total))

for number in range(digit, 0, -1):
    n = total // 10 ** (number-1)
    if number == 4:
        result += 'M' * n
    elif number == 3:
        if n == 4:
            result += 'CD'
        elif n == 9:
            result += 'CM'
        else:
            if n >= 5:
                result += 'D'
            result += 'C' * (n % 5)
    elif number == 2:
        if n == 4:
            result += 'XL'
        elif n == 9:
            result += 'XC'
        else:
            if n >= 5:
                result += 'L'
            result += 'X' * (n % 5)
    else:
        if n == 4:
            result += 'IV'
        elif n == 9:
            result += 'IX'
        else:
            if n >= 5:
                result += 'V'
            result += 'I' * (n % 5)

    total %= 10 ** (number-1)
print(result)    
