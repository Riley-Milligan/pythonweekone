def is_crowded(people):
    if len(people) > 5:
        print("there's a mob in this room")
    elif len(people) <= 5 & len(people) > 3:
        print("this room is quite crowded")
    elif len(people) <= 3 & len(people) != 0:
        print("this room's not too crowded")
    else:
        print("this room is empty")


people_in_room = ["john", "paul", "george", "ringo", "pete", "brian"]

is_crowded(people_in_room)

del people_in_room[0:2]

is_crowded(people_in_room)

del people_in_room[0:2]

is_crowded(people_in_room)

del people_in_room[0:2]

is_crowded(people_in_room)