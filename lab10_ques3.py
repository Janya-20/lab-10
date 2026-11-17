votes = input().split()

dct = {}
for i in votes:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1

winner = ""
max_votes = 0

for i in dct:
    print(i + ":", dct[i])
    if dct[i] > max_votes:
        max_votes = dct[i]
        winner = i

print("Winner:", winner)