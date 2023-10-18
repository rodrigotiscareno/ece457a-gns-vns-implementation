from vns import variable_neighborhood_search
import sys


def generalized_neighborhood_search(
    dimensions,
    x_range,
    regions,
    local_search_maximum_iterations,
    vns_maximum_neighborhood_iterations,
    vns_neighborhoods,
    convergence_threshold,
):
    absolute = abs(x_range[0] - x_range[1])
    splits = absolute / regions
    print(absolute)

    defined_regions = [
        [x_range[0] + splits * i, x_range[0] + splits * (i + 1)] for i in range(regions)
    ]

    x_history = []
    cost_history = []
    best_solution = sys.maxsize
    best_x = []

    for region in defined_regions:
        print(region)
        (
            current_x,
            current_solution,
            x,
            y,
        ) = variable_neighborhood_search(
            dimensions,
            region,
            vns_neighborhoods,
            local_search_maximum_iterations,
            vns_maximum_neighborhood_iterations,
            convergence_threshold,
        )

        if current_solution < best_solution:
            best_solution = current_solution
            best_x = current_x

        cost_history.append(current_solution)
        x_history.append(current_x)

    return best_x, best_solution, x_history, cost_history
