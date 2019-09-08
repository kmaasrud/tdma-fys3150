import matplotlib.pyplot as plt
import numpy as np
import sys

if len(sys.argv) < 2:
    print("This program takes one input. That is the filename of the file to be plotted.")
    sys.exit()
if 2 < len(sys.argv):
    print("This program takes only one input. That is the filename of the file to be plotted.")
    sys.exit()



f = open(sys.argv[1],"r")
lines=f.readlines()
x = np.zeros(len(lines))
y = np.zeros_like(x)
y1 = np.zeros_like(x)
i=0
for line in lines:
    x[i] = float(line.split()[0])
    y[i] = float(line.split()[1])
    y1[i] = float(line.split()[2])
    i += 1
plt.plot(x,y, label = "C++ computed")
plt.plot(x,y1, label = "Analytical")
plt.legend()

plt.show()
