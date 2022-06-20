import sys
sys.stdin = open('B.txt')

sik = input()
result = ''
temp = []
for char in sik:
    if char.isalpha():
        result += char
    elif char == '(':
        temp.append(char)
    elif char == ')':
        while temp and temp[-1] != '(':
            result += temp.pop()
        temp.pop()
    elif char in ('*', '/'):
        while temp and temp[-1] in ('*', '/'):
            result += temp.pop()
        temp.append(char)
    else:
        while temp and temp[-1] != '(':
            result += temp.pop()
        temp.append(char)
while temp:
    result += temp.pop()
print(result)
