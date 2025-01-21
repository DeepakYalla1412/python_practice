l1 = list(range(1,11))
print(l1)

print("sum", sum(l1))

print("max", max(l1))

print("min", min(l1))

def seperate_even_odd(l1):
    even = [num for num in l1 if num%2==0 ]
    odd = [num for num in l1 if num%2!=0 ]
    return even, odd 

print(seperate_even_odd(l1))

print("reverse list " , l1[::-1])

def is_sorted(list1):
    if list1 == sorted(list1):
        print("sorted")
    else:
        print("Not sorted")

is_sorted(l1)
is_sorted([2,4,1,5])


def remove_duplicates(list):
    return(set(list))

print("List after removing duplicates", remove_duplicates([1,1,2,3,4,5,5,5]))

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

lst1=[1,1,2,3,4]
lst2=[2,3,3,5]

print("L1 intersect L2", intersection(lst1, lst2))

def rotate_list(lst, k):
    k = k % len(lst1)
    print(k)
    print(lst[-k:])
    print(lst[:-k])
    return lst[-k:] + lst[:-k]

print(rotate_list([1,2,3,4,5,6,7], 2))

lst3=[1,2,3,4,5]
print(lst3[::2])

#lst[start:end:step]
lst4=[1,2,3,4,5,6,7,8,9]
print(lst4[1::3])