import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


class Baby:
    def __init__(self, height: float, weight: float, age_in_months: int):
        self.height = height
        self.weight = weight
        self.age_in_months = age_in_months


def make_babies(amount: int):
    baby_1 = Baby(0.6, 2.4, 6)
    baby_2 = Baby(0.4, 1.6, 1)
    baby_3 = Baby(0.8, 3.1, 26)

    center = [[baby_1.height, baby_1.weight, baby_1.age_in_months],
              [baby_2.height, baby_2.weight, baby_2.age_in_months],
              [baby_3.height, baby_3.weight, baby_3.age_in_months]]
    baby_3d, _ = make_blobs(n_samples=amount, centers=center, cluster_std=0.56)
    return baby_3d


def plotter(baby_3d):
    x, y, z = baby_3d[:, 0], baby_3d[:, 1], baby_3d[:, 2]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(x, y, z, linewidths=0.2)
    plt.show()


if __name__ == "__main__":
    babies = make_babies(5000)
    plotter(babies)
