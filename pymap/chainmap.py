import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict1, dict2)
res1 = collections.ChainMap(dict2, dict1)
# Creating a single dictionary
print('Map1 \n')
print(res.maps, '\n')
print('Map2 \n')
print(res1.maps, '\n')

print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))

print()


# Print all the elements from the result

print('elements:')
for key, val in res.items():
	print('{} = {}'.format(key, val))
print()

# Find a specific value in the result
print('day3 in res: {}'.format(('day3' in res)))
print('day4 in res: {}'.format(('day4' in res)))


print('day3 in res1: {}'.format(('day3' in res1)))
print('day4 in res1: {}'.format(('day4' in res1)))
