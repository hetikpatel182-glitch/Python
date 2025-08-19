fruits = ['apple', 'banana', 'mango', 'orange', 'grape']

search_item = input("Enter fruit name to search: ")

found = False

for item in fruits:
    if item == search_item:
        found = True
        break

if found:
    print("Fruit found in the list.")
else:
    print("Fruit not found in the list.")
