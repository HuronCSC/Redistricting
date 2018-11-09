import numpy as np

# 11/7/2018 task: create "easy" test state with "nice" county lines & random populations

y = 20
x = 20
distf = 20
state = np.random.negative_binomial(2, 0.003, size = (y, x))

# 11/14/2018 task: create two dictionaries:  1 maps the coordinates of a county to its population and the other maps the coordinates of a county to the coordinates of all neighboring counties
