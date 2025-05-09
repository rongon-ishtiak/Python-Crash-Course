# ORGANIZING A LIST
cars: list[str] = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Sorting a list temporarily with a sorted() function
print("Here is the original list: ")
for i in cars:
    print(f"\t{i.title()}.")

sorted_cars: list[str] = sorted(cars)
print("\nHere is the sorted list: ")
for sort in sorted_cars:
    print(f"\t{sort.title()}")

# Printing a list in a reverse order
sorted_cars.reverse()
print(sorted_cars)

# Finding a length in a list
total_cars: int = len(sorted_cars)
print(total_cars)



