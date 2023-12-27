users = ['Aarav', 'Dave', 'Sarah']

data = ['Aarav', 'Sarah', '42']

emptylist = []

print('Aarav' in emptylist)

print(users[0])
print(users[-2])

print(users.index('Sarah'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Emmanuel')

users += ['Jason']

users.extend(['Robert', 'Jimmy'])

users.insert(0, 'Bob')

users[2:2] = ['Eddie', 'Alex']

users[1:3] = ['Robert', 'JPJ']
print(users)

del users[0]

users.sort(key=str.lower)
print(users)

nums = [14, 19, 25, 37, 94]
# nums.sort(reverse=True)
# print(nums)
print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
anothertuple = (1, 4, 2, 8)
mytuple = tuple((1, True, 'Aarav'))
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))