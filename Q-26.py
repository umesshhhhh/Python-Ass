lst = [int(x) for x in input("Enter the list;").split()]
if len(lst) < 2:
    print("List must have at least two elements.")
else:
    largest = lst[0]
    second = None
    for num in lst[1:]:
        if num > largest:
            second = largest
            largest = num
        elif second is None or (num > second and num != largest):
            second = num
    if second is None:
        print("No second largest element (all elements are same).")
    else:
        print("Second largest element:", second)