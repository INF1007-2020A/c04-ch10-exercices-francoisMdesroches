#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as plt

# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(-1.3, 2.5, num=64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:

    return np.array([(np.sqrt(elt[0] ** 2 + elt[1] ** 2), np.arctan2(elt[1], elt[0])) for elt in cartesian_coordinates ])


def find_closest_index(values: np.ndarray, number: float) -> int:

    return (np.abs(values - number)).argmin()


def faire_graphique():

    les_x = np.linspace(-1, 1, num=250)
    les_y = les_x ** 2 * np.sin(1 / les_x ** 2) + les_x
    plt.plot(les_x, les_y)
    # plt.scatter(les_x, les_y)
    plt.show()
    return

def estimer_pi():


    return

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
    faire_graphique()
    estimer_pi()
    pass
