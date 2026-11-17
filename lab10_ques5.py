def simple_interest(p, r, t=1):
    si = (p * r * t) / 100
    return si

amt = float(input())
rate = float(input())

print("1 year:", simple_interest(amt, rate))
print("3 years:", simple_interest(amt, rate, 3))