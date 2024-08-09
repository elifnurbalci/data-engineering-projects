

def every(nums, func):
    for num in nums:
        if not func(num):
            return False
    return True

def is_even(num):
    return num % 2 == 0