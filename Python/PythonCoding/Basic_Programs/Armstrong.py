n = int(input('Enter a number to check for armstrong'))

temp = n
count = len(str(n))
s = 0

while temp > 0:
    last = temp % 10
    s += last ** count
    temp //= 10

if s == n:
    print('The no is armstrong number')
else:
    print('The no is not an armstrong number')