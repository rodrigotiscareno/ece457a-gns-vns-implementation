import numpy as np
import random

from helpers import bound_solution_in_x_range


def local_search(
    neighborhood,
    cost_function,
    max_itr,
    convergence_threshold,
    dimension,
):
    x_range = [neighborhood for i in range(dimension)]

    x_initial = [
        random.uniform(x_range[i][0], x_range[i][1]) for i in range(len(x_range))
    ]

    x_current = x_initial
    cost_current = cost_function(x_current)

    x_history = [x_current]
    cost_history = [cost_current]

    itr = 0
    convergence = False
    while not convergence:
        x_neighbor = [random.gauss(x, 0.1) for x in x_current]
        x_neighbor = bound_solution_in_x_range(x=x_neighbor, x_range=x_range)
        cost_neighbor = cost_function(x_neighbor)
        if cost_neighbor < cost_current:
            x_current = x_neighbor
            cost_current = cost_neighbor
        if (cost_current < convergence_threshold) or (itr >= max_itr):
            convergence = True

        x_history.append(x_current)
        cost_history.append(cost_current)

        itr += 1

    best_cost_index = np.argmin(cost_history)
    best_x = x_history[best_cost_index]
    best_cost = cost_history[best_cost_index]

    return best_x, best_cost, x_history, cost_history
