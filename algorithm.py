import numpy as np

# 11/7/2018 task: create "easy" test state with "nice" county lines & random populations

y = 20
x = 20
distf = 20
state = np.random.negative_binomial(2, 0.003, size = (y, x))

# 11/14/2018 task: create two dictionaries:  1 maps the coordinates of a county to its population and the other maps the coordinates of a county to the coordinates of all neighboring counties

pops = {}
neighbors = {}

for row in range(y):
    for dist in range(x):
        pops[(row, dist)] = state[row][dist]
        if row == 0:
            neighbors[(row, dist)] = [(row+1, dist)]
        elif row == y-1:
            neighbors[(row, dist)] = [(row-1, dist)]
        else:
            neighbors[(row, dist)] = [(row+1, dist), (row-1, dist)]

        if dist == 0:
            neighbors[(row, dist)].append((row, dist+1))
        elif dist == x-1:
            neighbors[(row, dist)].append((row, dist-1))
        else:
            neighbors[(row, dist)].extend([(row, dist+1), (row, dist-1)])
