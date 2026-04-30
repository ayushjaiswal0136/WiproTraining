import re

#Beginning and ending
# bpat = input('Enter beginning pattern') #India
# epat = input('Enter ending pattern') #Country
# text = input('Enter a text') #India is my country
#
# bpat = '^' + bpat
# epat = epat + '$'
#
# if re.search(pattern=bpat,string=txt):
#     print('Beginning pattern available')
# else:
#     print('Beginning pattern not available')
#
# if re.search(pattern=epat,string=txt):
#     print('Ending pattern available')
# else:
#     print('Ending pattern not available')

#digit
mbno = input('Enter a text')
pat = '[0-9]'

if re.fullmatch(pattern=pat, string=mbno):
    print('Only digits')
else:
    print('Other char available')