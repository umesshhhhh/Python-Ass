lst = [int(x) for x in input("Enter the list:").split()]
maximum = minimum = lst[0]
for num in lst:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print("Maximum number:", maximum)
print("Minimum number:", minimum)