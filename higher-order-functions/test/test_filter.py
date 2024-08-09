from src.filter import filter, do_something

def test_input_not_mutate():
  input=[1,2,3,4]
  expected=[1,2,3,4]
 
  filter(do_something,input)
  assert expected == input

def test_output_isnot_input():
  input=[1,2,3,4]

  output=filter(do_something,input)
  assert output is not input

def test_if_nums_empty():
  input=[]
  
  output=filter(do_something,input)
  assert None==output
  
def test_if_interator_is_transformed_by_func():
  input=[1,2,4]
  
  expected=[4] #more than 2 
  output = filter(do_something,input)
  assert expected ==output
  