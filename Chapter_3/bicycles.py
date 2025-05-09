# INTRODUCING LISTS IN PYTHON

bicycles: list[str] = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing elements in list
print(bicycles[0].capitalize())

# Return last item form a list
print(bicycles[-1].capitalize())

message = f"My first bicycle was a {bicycles[2].capitalize()}."
print(message)

