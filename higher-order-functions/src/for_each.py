def for_each(lst,func):
    our_list = ['danika','cat']
    if len(lst) == 0:
        return our_list
    for i in lst:
        func(i)
def do_some_stuff(item):
    print(f'{item} gets printed')



# def do_some_stuff(arg):
#     # This function could be doing anything!
#     # However it does not have a return value
#     pass

# for_each(['danika', 'cat'], do_some_stuff) 
# # do_some_stuff() is invoked twice
# # The first time it is invoked with 'danika' 
# # The second time it is invoked with 'cat'
# # The function passed to for_each will be 
#   invoked once for each element of 
# #  the list