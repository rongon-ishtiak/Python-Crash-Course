motorcycles: list[str] = ['honda', 'yamaha', 'ducati']

print("List of motorcycles are given below:- ")
for motor in motorcycles:
    print(f"\t{motor.capitalize()}")

# Appending elements to the end of the list
motorcycles.append('suzuki')


# Empty list
new_motorcycles: list[str] = []

new_motorcycles.append('suzuki')
new_motorcycles.append('honda')
new_motorcycles.append('hornet')
new_motorcycles.append('audi bike')

print("New motorcycle brand list:- ")
for motor in new_motorcycles:
    print(f"\t{motor.title()}")

# Inserting elements into the list by addressing the position of a list
new_motorcycles.insert(0, 'rtr')
print(new_motorcycles)

# Removing an item from the list by using del Statement
del new_motorcycles[0]
print(new_motorcycles)

# Removing an item using pop() Method
popped_motorcycle: str = new_motorcycles.pop()
print(f"The last motorcycle I owned was {popped_motorcycle.title()}.")



