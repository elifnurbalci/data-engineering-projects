def filter(func,lists):
    if len(lists) == 0:
        return None
    result = []
    for i in lists:
        if func(i) == None:
            pass
        else:
            result.append(func(i))
        # print(result)
    return result

def do_something(i):
    if i > 2:
        return i
    