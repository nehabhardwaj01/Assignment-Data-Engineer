def if_duplicate_exists(numbers):
    numbers.sort()
    if len(numbers) <= 1:
        return False
    prev = 0
    next = 1

    while next < len(numbers):
        if numbers[prev] == numbers[next]:
            return True
        else:
            prev += 1
            next += 1

    return False

# initializing nums and calling the function

nums = [1, 4, 6, 7, 2, 3, 2, 1, 4, 4, 5]

print(if_duplicate_exists(nums))
print(if_duplicate_exists([2,3,4,5,4,2]))
print(if_duplicate_exists([2]))
print(if_duplicate_exists([]))
print(if_duplicate_exists([2,2]))