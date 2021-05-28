# 1: r from hello world

print("hello_world"[-3])

# 2: ink from thinker

print("thinker"[2:5])

# 3: output of "hello"[1] = e

print("hello"[1])

# 4: not entirely sure what we were supposed to do here? going to get a list of unique characters from "mississippi"

print(set("mississippi"))

# 5: palindrome

print("input data")

palindrome_strings = ["stars", "O, a kak Uwakov lil vo kawu kakao!", "Some men interpret nine memos", "not a palindrome"]

print(palindrome_strings[0])
print(palindrome_strings[1])
print(palindrome_strings[2])
print(palindrome_strings[3])

for x in palindrome_strings:
    y = "".join([char for char in x if char.isalnum()]).lower()
    z = y[::-1].lower()
    if y == z:
        print("y")
    else:
        print("n")
