word = input()
f = {}

for i in word:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1

print(f)