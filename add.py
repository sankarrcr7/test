def add(*nums):
    result = 0
    for num in nums:
        result += num
    return result

print(add(1,3))