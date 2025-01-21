l= [44,54, 10, 4, 5, 6, 10,5, 7, 8, 10 ]
dict1 = {}
for i in l:
    if i in dict1:
        dict1[i] = dict1[i] + 1
    else:
        dict1[i] = 1
print(dict1)

dict2 = dict(sorted(dict1.items(), key=lambda x: x[1], reverse=True))

print(dict2)