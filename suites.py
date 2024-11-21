import numpy as np
import matplotlib.pyplot as plt

def burning_ship(c, max_iter=1000):
    z = 0
    n_iter = 0
    while abs(z) <= 2 and n_iter < max_iter:
        z = (abs(z.real) + 1j * abs(z.imag))**2 + c
        n_iter += 1
    return n_iter

def plot_burning_ship(xmin, xmax, ymin, ymax, width, height, max_iter=1000):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = np.array([burning_ship(complex(xx, yy), max_iter) for xx, yy in zip(X.ravel(), Y.ravel())])
    Z = Z.reshape(X.shape)

    plt.figure(figsize=(8, 8))
    plt.imshow(Z, extent=(xmin, xmax, ymin, ymax), cmap="twilight", aspect="auto")
    plt.title("Burning Ship")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.colorbar()
    plt.show()

plot_burning_ship(-2.0, 1.0, -2.0, 1.0, 800, 800)
