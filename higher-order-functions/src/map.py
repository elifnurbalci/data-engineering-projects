def map(iterable,func):
  if len(iterable)==0:
    return None
  
  iterable_2=[]
  for i in iterable:
    # print(func(i))
    iterable_2.append(func(i))
  return iterable_2
    

  # return iterable_2
  
  # return func(iterable_2)
  pass

def do_something(element):

  return element*2
  pass