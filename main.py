import yaml
from vns import variable_neighborhood_search


def main(config):
    # Get the search algorithm
    if config["search_algorithm"] == "vns":
        best_x, best_cost = variable_neighborhood_search(
            config["dimension"],
            config["vns"]["x_range"],
            config["vns"]["neighborhoods"],
            config["vns"]["local_search_maximum_iterations"],
            config["vns"]["vns_maximum_neighborhood_iterations"],
            config["vns"]["convergence_threshold"],
        )

    # if len(best_x) == 2:
    #     # If the dimensionality is 2, visualize the results.
    #     plot_utils.plot_results(best_x=best_x, best_cost=best_cost,
    #                             x_history=x_history, cost_history=cost_history,
    #                             cost_function=cost_function, x_range=x_range)


if __name__ == "__main__":
    with open("config.yml", "r") as f:
        config = yaml.safe_load(f)
    main(config=config)
