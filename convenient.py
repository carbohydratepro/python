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