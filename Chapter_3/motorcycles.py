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

