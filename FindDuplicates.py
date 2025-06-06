
arr = input("Enter a list of numbers in list").split(",")
arr = [int(num) for num in arr]

seen = set()
duplicates = set()

for num in arr:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicates:", duplicates)
