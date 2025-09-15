lst = [3, 2, 3, 5, 2, 5, 3]
freq = {}
for item in lst:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
print(freq)