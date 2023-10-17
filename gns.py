from concurrent.futures import ProcessPoolExecutor
from vns import variable_neighborhood_search


def _vns_helper(args):
    return variable_neighborhood_search(*args)


def generalized_neighborhood_search(
    dimensions,
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

    inputs = [
        (
            dimensions,
            neighborhood_range,
            neighborhoods,
            local_search_maximum_iterations,
            vns_maximum_neighborhood_iterations,
            convergence_threshold,
        )
        for neighborhood_range in defined_neighborhoods
    ]

    with ProcessPoolExecutor(max_workers=len(defined_neighborhoods)) as executor:
        results = list(executor.map(_vns_helper, inputs))

    print(results)

    return results


if __name__ == "__main__":
    results = generalized_neighborhood_search(2, [-500, 500], 2, 40, 10, 0.01)
