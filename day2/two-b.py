# 1: output of list with one number, one word, and one float

list_one = [1, "one", 1.1]

print(list_one)

# 2: value of 2 from [1, 1, [1, 2]]

list_two = [1, 1, [1, 2]]

print(list_two[2][1])

# 3: result of lst[1:] for lst = lst=['a','b','c'] is ['b', 'c']

lst = ['a', 'b', 'c']

print(lst[1:])

# 4: assign weekdays and index numbers to dictionary variable

week_dictionary = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}

# 5: given D={‘k1’:[1,2,3]} output of d[k1][1] is 2

d = {"k1": [1, 2, 3]}

print(d["k1"][1])

# 6: list to tuple

list_six = [1, [2, 3]]

tuple_six = tuple(list_six)

# 7: repeat of two-a #4, adjusted for #8

set_seven = set("mississippi")

# 8: add x to set created in #7

set_seven.add("x")

# 9: output of given set([1,1,2,3])

set_nine = ([1, 1, 2, 3])

print(set_nine)
