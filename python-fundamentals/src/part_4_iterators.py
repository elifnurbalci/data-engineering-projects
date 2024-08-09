def indexer(text):
    if text and text[0] not in " \t\n" :
        yield 0
    for index, char in enumerate(text[1:],1):
        try:
            if text[index-1] in " \t\n" and char not in " \t\n":
                yield index
        except StopIteration:
            raise StopIteration

def cool_cat(*items):
    for item in items:
        if isinstance(item,dict):
            try:
                for key, value in item.items():
                    yield (key, value)
            except StopIteration:
                raise StopIteration
        else:
            try:
                for i in item:
                    yield i
            except StopIteration:
                raise StopIteration
