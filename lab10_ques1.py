nums = list(map(int, input().split()))
v = int(input())

t = tuple(nums)

print("Tuple:", t)
print("Length:", len(t))
print("Count of v:", t.count(v))

if v in t:
    print("First index of:", v, t.index(v))
else:
    print("v is not in the tuple")