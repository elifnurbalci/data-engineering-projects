from src.some import some,is_even

def test_if_inner_func_evoked():
  is_func_evoked=False
  def test_func(x):
    nonlocal is_func_evoked
    is_func_evoked=True
  

  some(["e","E"],test_func)
  assert is_func_evoked

def test_if_even_or_not():
 
 def test_func(num):
   return num % 2 == 0
 
 expected = some([1,5,3,8],test_func)
 assert expected == some([1,5,3,8],is_even)


# def test_if_no_even_inner_func():
#   is_func_evoked= False
#   def test_func(x):
#     nonlocal is_func_evoked
#     is_func_evoked=False
#     return is_func_evoked
  
#   some([1,3,5],test_func)
#   assert False
