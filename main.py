import matplotlib.pyplot as plt
import numpy as np


def rastrigin(x, y):
    return (
        20
        + (np.pow(x, 2) - 10 * np.cos(2 * np.pi * x))
        + (np.pow(y, 2) - 10 * np.cos(2 * np.pi * y))
    )


def main():
    x = np.linspace(-3, 7, 100)
    y = np.linspace(-3, 7, 100)
    x, y = np.meshgrid(x, y)
    z = rastrigin(x, y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(x, y, z, cmap="viridis")

    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_zlabel("Eje Z")
    ax.set_title("Rastrigin (n=2)")

    plt.show()


if __name__ == "__main__":
    main()
