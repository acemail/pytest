
# list operations
print('--------------------------------------------------------')
print('List operations')

print('--------------------------------------------------------')
squares = [1,3,5,6,7,8,12]
print(squares)
print(squares[1])
print(squares[-3:])
print(squares[:])
print(squares + [34,56,234,65])

print('--------------------------------------------------------')
cubes = [1, 8, 27, 66, 87, 100]
print(cubes)
print(4**3)
cubes[3] = 4**3
print(cubes)
cubes.append(216)
print(cubes)
cubes.append(7**3)
print(cubes)

print('--------------------------------------------------------')
letters = ['a','b','c','d','e','f','g']
print(letters)
letters[2:5]=['C', 'D', 'E']
print(letters)
letters[:] = []
print(letters)
letters = ['a','b','c','d','e','f','g']
letter_length = len(letters)
print('letters[] = ' + str(letter_length))
print('letters[] = ' + str(len(letters)))

