def is_crowded(people):
    if len(people) > 3:
        print("this room is quite crowded")
    else:
        print("this room's not too crowded")


people_in_room = ["john", "paul", "george", "ringo"]

is_crowded(people_in_room)

del people_in_room[0:1]

is_crowded(people_in_room)
