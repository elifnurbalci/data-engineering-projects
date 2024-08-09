def flatten(lst, depth=1):
    result = []
    for item in lst:
        if isinstance(item, list) and depth > 0:
            result.extend(flatten(item, depth-1))
        else:
            result.append(item)
    return result

def deep_entries(input_dict):
    result = []
    for key, value in input_dict.items():
        if isinstance(value, dict):
            result.append((key, deep_entries(value)))
        else:
            result.append((key, value))
    
    return tuple(result)

