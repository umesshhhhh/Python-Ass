lst = [int(x) for x in input("Enter the list:").split()]
LISTT = []
for num in lst:
    if num not in LISTT:
        LISTT.append(num)
print("List after removing numbers:", LISTT)