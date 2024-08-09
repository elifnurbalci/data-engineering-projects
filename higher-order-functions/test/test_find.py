from src.find import find, is_multiple_of_five

def test_if_inner_func_evoked():
  is_func_evoked=False
  def test_func(x):
    nonlocal is_func_evoked
    is_func_evoked=True
  

  find(["e","E"],test_func)
  assert is_func_evoked

def test_if_multiple_of_5():
 
  def test_func(num):
    return num % 5 == 0
  
  expected= find([1,5,3,8],test_func)
  assert expected == find([1,5,3,8],is_multiple_of_five)