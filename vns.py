import sys

from utils.local_search import local_search
from utils.helpers import schwefel


def variable_neighborhood_search(
    dimension,
    x_range,
    neighborhoods,
    local_search_maximum_iterations,
    vns_maximum_neighborhood_iterations,
    convergence_threshold,
):
    absolute = abs(x_range[0] - x_range[1])
    splits = absolute / neighborhoods
    print(absolute)

    defined_neighborhoods = [
        [x_range[0] + splits * i, x_range[0] + splits * (i + 1)]
        for i in range(neighborhoods)
    ]

    x_history = []
    cost_history = []
    best_solution = sys.maxsize
    best_x = []

    converged = False
    neighborhood_index = 0
    iterations = 0

    while not converged:
        iterations += 1

        current_neighborhood = defined_neighborhoods[neighborhood_index]

        local_search_results = local_search(
            current_neighborhood,
            schwefel,
            local_search_maximum_iterations,
            convergence_threshold,
            dimension,
        )

        current_x = local_search_results[0]
        current_solution = local_search_results[1]

        x_history.append(current_x)
        cost_history.append(current_solution)

        if current_solution < best_solution:
            best_solution = current_solution
            best_x = current_x
            neighborhood_index = 0
        else:
            neighborhood_index += 1

        if (
            iterations == vns_maximum_neighborhood_iterations
            or best_solution < convergence_threshold
        ):
            converged = True

        if (neighborhood_index + 1) > neighborhoods:
            neighborhood_index = 0

    return best_x, best_solution, x_history, cost_history
