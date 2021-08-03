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

x = ['Nana','Muco', 24] #lists can mix data types
print(f'lists: {x}') #Print the list
print(f'len: {len(x)}') #Print the length

#Index and positisioning - zero based
print(f'Zero: {x[0]}') #First item is Zero
print(f'Slice: {x[1:2]}') #Slice the list

#Adding Items - append, insert
x.append('Pizza') #Adds at the end
x.append('Beer') #Adds at the end
x.insert(1,'Cats') #Adds at a specific position
print(f'lists: {x}')

 #Removing items - remove, pop, delete
x.remove('Cats') #Remove an item
print(f'Lists: {x}')

i = x.index('Pizza') #Will raise an error if not
print(f'Food: {x.pop(i)}') #Pop removes or returns the item
print(f"List: {x}")

i = x.index('Beer') #Will raise an error if not found
del x[i] #Delete a specific item without returning it
print(f"List: {x}")

#Extending - Adds elements from another list
y = ['Cats','Dogs','Birds']
x.extend(y)
print(f"Extend: {x}")

#Sort ascending - sort descending, reverse
x.remove(24)
x.sort() #Will throw error if there is a mix type
print(f"Sort: {x}")
x.reverse()
print(f"Reverse: {x}")

#Copy
y = x.copy() #Copies the elements into a new list
y.reverse()
y.append('Apples')
print(f"Original: {x}")
print(f"New: {y}")

#Delete the whole thing
del y
#print(y)

#clear
x.clear()
print(f"Cleared: {x}")
print(f"len: {len(x)}")

#lists can contain other lists [[],[],[]]
x = []
y = [1,2,3]
z = ['Nana','Muco']
x.append(y)
x.insert(0,z)

print(f"Lists in lists: {x}")
print(f"0: {x[0][0]}")
print(f"1: {x[1][2]}")

#Changing items -positional and assigning them value
x = [1,2,3,4,5]
x[2] = 'TEST'
print(x)

# Sets {}
# Sets contains unordered, unique, immutable data types in a hash table

# Creating a set
s = {1, 2, 2, 2, 3, 4, 5}
print(s)

l = ['Nana', 'Muco', 24]
s = set(l)
print(s)

# Adding items to a set
s.add('Hello')
s.update([1, 2, 3, 'Hello'])
print(s)

# Removing items
s.discard('Hello') # will not throw an error
s.remove(1) # will throw an error
v =s.pop() # pop removes a value and gives it to you
print(s)

# Can not change items - remove and add
# s[0] = 'A' # Error
#print(s[0]) # Error
print(3 in s)
s.remove(3)
s.add(12)
print(s)

x = set('abcd')
y = set('cdefg')

s = x.union(y) # All the elements that are in either sets
print(f'Union {s}')

s = x.intersection(y) # All the elements that are in both sets
print(f'Intersection {s}')

s = x.difference(y) # All the elements that are in x not y
print(f'difference {s}')

s = x.symmetric_difference(y) # All the elements that are in one of the sets
print(f'symmetric {s}')

# Tuple
# Tuple is fast list that can not be modified

# Create a tuple
t = (1,2,3,4)
print(t)

# Access the elements
print(f'index: {t[0]}')
print(f'Slice: {t[2:]}')
print(f'bool: {3 in t}')

# Assignemnt use the range tuple
(x,y,z) = (1,2,3)
print(x)
print(y)
print(z)

(x,y,z) = range(1,4)
print(x)
print(y)
print(z)

# Dictionary {k:v,k:v}
# Indexed by keys, which can be any immutable type (changeable)

# Create a dictionary
d = {'pet': 'dog', 'age': 5, 'name': 'spot'}
print(d)
d = dict(pet='dog', age=5, name='spot')
print(d)

# Keys and Values, When you go look something up we cant do it by index have to do it by keys
print(f'Items:{d.items()}')
print(f'Keys: {d.keys()}')
print(f'Values:{d.values()}')

# Getting a value from the key
print(f'name:{d["name"]}')
#print(f'Test: {d["bla"]}') Will throw an error if the is not found

# Add an item
d['trick'] = 'sit'
print(d)
d ['trick'] = 'Suck'
print(d)

# Removing an item
del d['trick']
print(d)

# Testing for existence
if 'name' in d:
    print(d['name'])

# Looping
for key in d.keys():
    print(f'{key} = {d[key]}')
# Printing Existence within the library
