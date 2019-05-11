# Let a grah be :
# V = {a, b, c, d, e}
# E = {ab , ac, cd, bd, de}

# python implementation

graph = { 'a': ['b', 'c'], 'b': ['a', 'd'], 'c': ['a','d'],\
'd': ['e'], 'e': ['d']}

#printing the graph

print(graph)
