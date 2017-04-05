import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("/Users/DboyLiao/Works/data/faces/15.jpg")
fig, ax = plt.subplots()
ax.imshow(img)

coords = fig.ginput(n = 3, timeout = 0)
print np.floor(coords)