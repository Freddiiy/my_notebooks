import numpy as np
import matplotlib.pyplot as plt


def ex_one():
    with open("../data/befkbhalderstatkode.csv", "r") as file_obj:
        neighb = np.genfromtxt(file_obj, delimiter=",", dtype=np.uint, skip_header=1)
        neighb_2015 = neighb
        neighb_2015_mask = (neighb_2015[:, 0] == 2015)
        masked = neighb_2015[neighb_2015_mask]

        print(neighb_2015[:, 0])


if __name__ == "__main__":
    ex_one()
