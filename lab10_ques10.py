def stats(nums):
    low = nums[0]
    high = nums[0]
    total = 0
    count = 0
    
    for i in nums:
        if i < low:
            low = i
        if i > high:
            high = i
        total += i
        count += 1
        
    avg = total / count
    return (low, high, avg)

lst = list(map(int, input().split()))
result = stats(lst)
print(result)

