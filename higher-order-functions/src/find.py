def find(nums,func):
  for num in nums:
    if func(num):
      return num
  pass

def is_multiple_of_five(num):
    return num % 5 == 0