import numpy as np
import matplotlib.pyplot as plt
infile = open("oppgave_1b.txt", "r")
n = 0
u = []
for line in infile:
    words = line.split()
    u.append(float(words[0]))
    n += 1
x = np.linspace(0, 1, n)    
f = 1 - (1 - np.exp(-10))*x - np.exp(-10*x)
u.reverse()
plt.plot(x, u, "-", x, f, "-")
plt.legend(["calculated", "exact solution"])
plt.xlabel("x")
plt.ylabel("u(x)")
plt.title("Oppgave 1b (n=%i)" %(n+1))
plt.show()
