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

tgtpop = sum(state.values()) / distf

def findMerge(dist):
    nbp = {}
    for neighbor in neighbors[dist]:
        nbp[neighbor] = pops[neighbor]
    popDif = {}
    for key in nbp:
        popDif[key] = abs(tgtpop - (nbp[key] + pops[dist]))
    merge = min(popDif, key=popDif.get)
    return merge


def doMerge(dist, merge, history):

    # Update the history information
    history[merge] = dist
    for k, v in history:
        if v == merge:
            history[k] = dist

    # Make sure that merge and dist are neighbors of each other
    assert(dist in neighbors[merge])
    assert(merge in neighbors[dist])
    assert(dist not in neighbors[dist])
    assert(merge not in neighbors[merge])

    # combine dist and merge populations under dist's key in pops dictionary
    pops[dist] += pops[merge]

    # remove merge key in pops dictionary
    del pops[merge]
    
    # Everything that was a neighbor of merge now needs to become a neighbor of dist
    neighbors[dist].update(neighbors[merge])
    neighbors[dist].remove(dist)
    
    # replace all occurences of merge in all values in neighbors dictionary with dist
    for neighbor in neighbors[merge]:
        neighbors[neighbor].remove(merge)
        if neighbor != dist:
            neighbors[neighbor].add(dist)
            
    # remove merge key from neighbors dictionary
    del neighbors[merge]


while len(pops) > distf:
    dist = min(pops, key=pops.get)
    doMerge(dist, findMerge(dist))
