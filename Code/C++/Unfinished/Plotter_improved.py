import matplotlib.pyplot as plt
import numpy as np
import sys

"""
if len(sys.argv) < 2:
    print("This program takes one input. That is the filename of the file to be plotted.")
    sys.exit()
if 2 < len(sys.argv):
    print("This program takes only one input. That is the filename of the file to be plotted.")
    sys.exit()
"""
f = np.zeros(len(sys.argv))
line = np.zeros_like(f)
x = np.zeros_like(f)
y = np.zeros_like(f)
for i in range(1,len(sys.argv)):
    f[i] = open(sys.argv[i],"r")
    lines[i] = f[i].readlines()

    i=0
    for line in lines:
        x[i][i] = float(line.split()[0])
        y[i][i] = float(line.split()[1])
        i += 1
        plt.plot(x[i],y[i], label = "TDMA n=&g" % len(x[i]))
plt.plot(x,y1, label = "Analytical")
plt.legend()

plt.show()
