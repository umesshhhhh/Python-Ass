string = input("Enter a string: ")
reversed_str = ""
index = len(string) - 1
while index >= 0:
    reversed_str += string[index]
    index -= 1
print("Reversed string:", reversed_str)