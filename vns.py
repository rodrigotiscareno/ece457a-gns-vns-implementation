import sys

from local_search import local_search
from helpers import schwefel


def variable_neighborhood_search(
    dimension,
    x_range,
    neighborhoods,
    local_search_maximum_iterations,
    vns_maximum_neighborhood_iterations,
    convergence_threshold,
):
    absolute = abs(x_range[0]) + abs(x_range[1])
    splits = absolute / neighborhoods

    defined_neighborhoods = [
        [x_range[0] + splits * i, x_range[0] + splits * (i + 1)]
        for i in range(neighborhoods)
    ]

    best_solution = sys.maxsize
    converged = False
    neighborhood_index = 0
    iterations = 0

    while not converged:
        if (neighborhood_index + 1) > neighborhoods:
            neighborhood_index = 0

        iterations += 1

        current_neighborhood = defined_neighborhoods[neighborhood_index]

        current_solution = local_search(
            current_neighborhood,
            schwefel,
            local_search_maximum_iterations,
            convergence_threshold,
            dimension,
        )[1]

        if current_solution < best_solution:
            best_solution = current_solution
            if neighborhood_index != 0:
                neighborhood_index -= 1
        else:
            neighborhood_index += 1

        if (
            iterations == vns_maximum_neighborhood_iterations
            or best_solution < convergence_threshold
        ):
            converged = True

        return (-1, -1)
