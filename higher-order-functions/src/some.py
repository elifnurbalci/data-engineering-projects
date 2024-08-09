def some(nums,func):
  for num in nums:
    if func(num):
      return True
  return False

def is_even(num):
  return num % 2 == 0


# result=some([1,2,3],is_even) 
# print(result)



