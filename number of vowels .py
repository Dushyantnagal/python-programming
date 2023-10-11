string = input("Enter a string: ")
count = 0
for i in string:
    if i in "aeiouAEIOU":
        count += 1
print("Number of vowels in the string is", count)