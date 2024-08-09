from src.map import map,do_something

def test_input_not_mutate():
  input=[1,2,3,4]
  expected=[1,2,3,4]
  # def test_func():
  #   pass
  map(input,do_something)
  assert expected == input

def test_output_isnot_input():
  input=[1,2,3,4]
 
  # def test_func():
  #   pass
  output=map(input,do_something)
  assert output is not input

def test_if_nums_empty():
  input=[]
  
  # def test_func():
  #   pass
  output=map(input,do_something)
  assert None==output
  
def test_if_interator_is_transformed_by_func():
  input=[1,2,4]

  # def test_func(element):
  #   return element*2
  
  expected=[2,4,8]
  output = map(input,do_something)
  assert expected ==output
  



