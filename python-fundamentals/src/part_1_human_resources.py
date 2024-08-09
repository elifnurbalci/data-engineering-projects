def make_name_tags(guests):
    if len(guests) > 0:
        for guest in guests:
            name_tag = f"{guest['title']} {guest['forename']} {guest['surname']}, {guest['company']}"
            guest['name_tag'] = name_tag
        return guests
    return []


def create_poll(lst):
    if len(lst) > 0:
        poll = {}
        for i in lst:
            if i in poll:
                poll[i] += 1
            else:
                poll[i] = 1
        return poll
    return []

