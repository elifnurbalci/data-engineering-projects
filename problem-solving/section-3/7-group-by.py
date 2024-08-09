# This function takes an list of dictionaries and a string which should
#  match a key of the dictionaries in the list

# coders = [
#   { name: 'cat', location: 'manchester' },
#   { name: 'liam', location: 'york' },
#   { name: 'jim', location: 'leeds' },
#   { name: 'haz', location: 'manchester' },
#   { name: 'dave', location: 'leeds' },
# ];

# group_by(coders, 'location');

# The function returns an dictionary where the keys represent the matching
#  values and each matching dictionary is in an list.

#  // result

# {
#   manchester: [
#     { name: 'cat', location: 'manchester' },
#     { name: 'haz', location: 'manchester' },
#   ],
#   york: [
#     { name: 'liam', location: 'york' },
#   ],
#   leeds: [
#     { name: 'jim', location: 'leeds' },
#     { name: 'dave', location: 'leeds' },
#   ]
# }


def group_by(list, key):
    pass


def test_group_by_returns_coders_group_by_location():
    coders = [{"name": "cat", "location": "manchester"},
                   {"name": "liam", "location": "york"},
                   {"name": "jim", "location": "leeds"},
                   {"name": "haz", "location": "manchester"},
                   {"name": "dave", "location": "leeds"}]

    assert group_by(coders, "location") == {
        "manchester": [
            {"name": "cat", "location": "manchester"},
            {"name": "haz", "location": "manchester"}
        ],
        "york": [
            {"name": "liam", "location": "york"}
        ],
        "leeds": [
            {"name": "jim", "location": "leeds"},
            {"name": "dave", "location": "leeds"}
        ]
    }
