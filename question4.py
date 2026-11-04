my_set = {10, 20, 30, 40, 50}
num = int(input("Enter a number: "))
if num in my_set:
    print(f"{num} exists")
else:
    print(f"{num} does not exist")