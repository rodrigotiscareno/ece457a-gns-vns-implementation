import numpy as np
import random

from local_search import local_search
from helpers import schwefel


RANGE = [-500, 500]
DIMENSIONS = 2
NEIGHBORHOODS = 7
MAX_ITERATIONS_LS = 500
COST_FUNC = schwefel


def variable_neighborhood_search():
    absolute = abs(RANGE[0]) + abs(RANGE[1])
    splits = absolute / NEIGHBORHOODS

    defined_neighborhoods = [
        [RANGE[0] + splits * i, RANGE[0] + splits * (i + 1)]
        for i in range(NEIGHBORHOODS)
    ]

    for i in defined_neighborhoods:
        print(local_search(i, schwefel))


variable_neighborhood_search()
