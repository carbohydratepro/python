"""
def modelConversion(mlist, punctuate=False):
    if punctuate:
        mlist = mlist.split(" ")
    return [int(n) for n in mlist]

lista = input()
print(modelConversion(lista, True))
"""
table = [
        [False, False, False, False],
        [True , False, False, False],
        [False, True , False, False],
        [False, False, True , False],
        [False, False, False, True ],
        [True , True , False, False],
        [False, True , True , False],
        [False, False, True , True ],
        [True , False, False, True ],
        [True , True , True , False],
        [False, True , True , True ],
        [True , False, True , True ],
        [True , True , False, True ],
        [True , False, True , False],
        [False, True , False, True ],
        [True , True , True , True ]
]
a=[False, False, True, True]
b=[False, True, False, True]
c = [False, False, False, False]

for i in range(4):
    c[i] = ((not a[i] or b[i]) and (a[i] and b[i]) or not(a[i] or not b[i]))

print(c)

#202230130記述
import io
import sys
from itertools import permutations

# input here
_INPUT = """\
まむし
むしのようちゅうまむ
うんこ
"""
sys.stdin = io.StringIO(_INPUT)

str = []

while True:
    try:
        str.append(input())
    except:
        break


combine_str = []
while True:
    max_length = 0
    for pattern in list(permutations(range(len(str)), 2)):
        str1 = str[pattern[0]]
        str2 = str[pattern[1]]

        str1 += ' '
        n = min([len(str1), len(str2)])

        for i in range(n):
            if str1[-n+i-1:-1] == str2[0:n-i]:
                # print('共通部分は ’', str1[-n+i-1:-1], '’')
                if max_length <= len(str1[-n+i-1:-1]):
                    max_length = len(str1[-n+i-1:-1])
                    combine_str.clear()
                    combine_str = [str1, str2]
                break

    if max_length == 0:
        break
    else:
        str1 = combine_str[0]
        str2 = combine_str[1]
        
        n = min([len(str1), len(str2)])
        for i in range(n):
            if str1[-n+i-1:-1] == str2[0:n-i]:
                combined_str = (str1 + str2.replace(str1[-n+i-1:-1], '')).replace(' ', '')
                break

        str.remove(combine_str[0].replace(' ', ''))
        str.remove(combine_str[1])
        str.append(combined_str)


print(len(max(str)))
print(max(str))
