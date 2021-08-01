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
