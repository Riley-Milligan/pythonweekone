to_count = input("Please enter a series of numbers")

retrieved_list = to_count.split(", ")

print(retrieved_list)

odd_count = 0
even_count = 0

for x in retrieved_list:
    if int(x) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers: " + str(even_count))
print("Number of odd numbers: " + str(odd_count))
