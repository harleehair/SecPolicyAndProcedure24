import numpy as np
import matplotlib.pyplot as plt

rows = 10
cols = 10
iterations = 100  # Declare the global variable outside the function

def mandelbrot(c, z):
    global iterations  # Correct global variable declaration
    count = 0
    for a in range(iterations):  # Correct loop range
        z = z**2 + c
        count += 1
        if abs(z) > 4:
            break
    return count

def mandelbrot_set(x, y):
    m = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            c = complex(x[i], y[j])
            z = complex(0, 0)
            count = mandelbrot(c, z)
            m[j, i] = count  # Correct array indexing
    return m

# creating our x and y arrays
x = np.linspace(-2, 1, rows)
y = np.linspace(-1, 1, cols)
# create our mandelbrot set
m = mandelbrot_set(x, y)
# plot the set (best colors: binary, hot, bone, magma)
plt.imshow(m.T, cmap="magma")
plt.axis("off")
plt.show()
