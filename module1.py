print('heloo')

def sum(*nums):
    result = 0
    for n in nums:
        result += n
    return result
nums = [1, 2, 3, 4, 5, 6]

print(sum(*nums))