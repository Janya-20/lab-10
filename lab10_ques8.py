n = int(input())
dct = {}

for i in range(n):
    lst = input().split()
    nation = lst[0]
    city = lst[1]
    dct[nation] = city

s = input()

if s in dct:
    print(dct[s])
else:
    print("Not found")