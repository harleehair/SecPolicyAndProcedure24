import numpy as np
import matplotlib.pyplot as plt

rows = 10
cols = 10
iterations = 100

def mandelbrot(c, z):
   global iterations ;
   count = 0
   for a in range(iterations):
      z = z**2 + c
      count += 1
      if(abs(z) > 4):
         break
   return count

def mandelbrot_set(x, y):
   m = np.zeros((len(x), len(y)))
   for i in range(len(x)):
      for j in range(len(y)):
         c = complex(x[i], y[j])
         z = complex(0, 0)
         count = mandelbrot(c, z)
         m[i, j] = count
   return m

#creating our x and y arrays
#I assumed we were only changing x an y, so that is what i did! 
x = np.linspace( -4, 2, rows)
y = np.linspace( 0, -1, cols)

#create our mandelbrot set
m = mandelbrot_set(x, y) 

#plot the set (best colors: binary, hot, bone, magma)

plt.imshow(m.T, cmap = "magma")
plt.axis("off")
plt.show()

#this can help keep track of the fractals, just change the number on the file
#I'm sure there is a more intuitive way to loop this 
plt.imshow(m.T, cmap="magma")
plt.axis("off")
plt.savefig('mandelbrot_fractal_10.png')  # Save the plot as an image file
plt.show()

