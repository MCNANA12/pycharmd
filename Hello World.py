# Basic string Operation
str = 'Hello World, this is a string!'
print(len(str))  # Get the length
print(str * 3)  # Repeat
print(str.replace('Hello', 'Hola'))  # Replace
print(str.split(','))  # Split
print(str.startswith('H'))  # starts with
print(str.endswith('!'))
print(str.lower())
print(str.upper())

# slicing - or getting a sub string
print(str[0:4])  # Get the fisrt 5 - zero based
print(str[6:])  # Get the 6th to the end
print(str[-7:])  # Get the last 7
print(str[6:11])  # Get the 6 to 11

# indexs - the position of
l = ','
c = str.find(l) # -1 if not found
print(f'Find returned {c}')

i = str.index(l) # Will throw an error!
print(f'Find returned {i}')

x = str[:i]
print(x)

#lists you create with square brackets

