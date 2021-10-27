# these are the term counts calculated in the lab
import matplotlib.pyplot as plt
lab_dict = {'trump': 13924, 'russia': 412,
            'obama': 2712, 'fake news': 333, 'mexico': 199}

terms = lab_dict.keys()
counts = lab_dict.values()


# the order of results in .keys() and .values() is nondeterministic == 'random'
# however the terms and counts will always correspond


# this code generates a plot
fig, ax = plt.subplots()
ax.bar(terms, counts)
plt.show()
