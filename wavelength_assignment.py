import random


def path_to_links(path_nodes):
    return [(path_nodes[i], path_nodes[i + 1]) for i in range(len(path_nodes) - 1)]


def random_fit(paths, lambda_count, num_nodes, b, links):
    # For each link, we maintain a list of booleans representing wavelength availability.
    link_wavelengths = {link: [True] * lambda_count for link in links}

    # We'll keep track of connections per wavelength for reporting.
    wavelength_allocation = {w: [] for w in range(1, lambda_count + 1)}

    total_requests = 0
    blocked_requests = 0

    # Try to assign wavelengths for each request
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                continue
            demand = b[i, j]
            if demand > 0:
                node1 = i + 1
                node2 = j + 1

                pair_key = (min(node1, node2), max(node1, node2))
                if pair_key not in paths:
                    # No path defined, cannot route
                    blocked_requests += demand
                    total_requests += demand
                    continue

                route = paths[pair_key]
                route_links = path_to_links(route)

                for _ in range(demand):
                    total_requests += 1

                    # Find available wavelengths on all links of this route
                    available_wavelengths = set(range(lambda_count))
                    for link in route_links:
                        link_avail = {w for w, avail in enumerate(link_wavelengths[link]) if avail}
                        available_wavelengths.intersection_update(link_avail)

                    if available_wavelengths:
                        # Randomly pick one of the available wavelengths
                        chosen_w = random.choice(list(available_wavelengths))

                        # Assign this wavelength to all links in the route
                        for link in route_links:
                            link_wavelengths[link][chosen_w] = False
                        wavelength_allocation[chosen_w + 1].append((node1, node2))
                    else:
                        # No wavelength was found for this request
                        blocked_requests += 1

    # Calculate the blocking percentage
    blocked_percentage = (blocked_requests / total_requests) * 100 if total_requests > 0 else 0
    return blocked_percentage, wavelength_allocation


def first_fit(paths, lambda_count, num_nodes, b, links):
    # For each link, we maintain a list of booleans representing wavelength availability.
    # True means the wavelength is available.
    link_wavelengths = {link: [True] * lambda_count for link in links}

    # We'll keep track of connections per wavelength for reporting.
    wavelength_allocation = {w: [] for w in range(1, lambda_count + 1)}

    total_requests = 0
    blocked_requests = 0

    # Try to assign wavelengths for each request
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                continue
            demand = b[i, j]
            if demand > 0:
                node1 = i + 1
                node2 = j + 1

                pair_key = (min(node1, node2), max(node1, node2))
                if pair_key not in paths:
                    # No path defined, cannot route
                    blocked_requests += demand
                    total_requests += demand
                    continue

                route = paths[pair_key]
                route_links = path_to_links(route)

                for _ in range(demand):
                    total_requests += 1

                    # Instead of finding all available wavelengths at once,
                    # we try them in ascending order, picking the first fit.
                    wavelength_assigned = False
                    for w in range(lambda_count):
                        # Check if wavelength w is free on all links of the route
                        if all(link_wavelengths[link][w] for link in route_links):
                            # Assign this wavelength
                            for link in route_links:
                                link_wavelengths[link][w] = False
                            wavelength_allocation[w + 1].append((node1, node2))
                            wavelength_assigned = True
                            break

                    if not wavelength_assigned:
                        # No wavelength was found for this request
                        blocked_requests += 1

    blocked_percentage = (blocked_requests / total_requests) * 100 if total_requests > 0 else 0
    return blocked_percentage, wavelength_allocation


def least_used(paths, lambda_count, num_nodes, b, links):
    # For each link, we maintain a list of booleans representing wavelength availability (True = available).
    link_wavelengths = {link: [True] * lambda_count for link in links}

    # We'll keep track of connections per wavelength for reporting and usage.
    wavelength_allocation = {w: [] for w in range(1, lambda_count + 1)}
    wavelength_usage = [0] * lambda_count  # Track how many times each wavelength is assigned

    total_requests = 0
    blocked_requests = 0

    # Try to assign wavelengths for each request
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                continue
            demand = b[i, j]
            if demand > 0:
                node1 = i + 1
                node2 = j + 1

                pair_key = (min(node1, node2), max(node1, node2))
                if pair_key not in paths:
                    # No path defined, cannot route
                    blocked_requests += demand
                    total_requests += demand
                    continue

                route = paths[pair_key]
                route_links = path_to_links(route)

                for _ in range(demand):
                    total_requests += 1
                    # Find available wavelengths on all links of this route
                    available_wavelengths = set(range(lambda_count))
                    for link in route_links:
                        link_avail = {w for w, avail in enumerate(link_wavelengths[link]) if avail}
                        available_wavelengths = available_wavelengths.intersection(link_avail)

                    if len(available_wavelengths) == 0:
                        # No wavelength is free for this request
                        blocked_requests += 1
                    else:
                        # Among the available wavelengths, choose the one with the least usage
                        least_used_w = min(available_wavelengths, key=lambda w: wavelength_usage[w])

                        # Assign this wavelength
                        for link in route_links:
                            link_wavelengths[link][least_used_w] = False
                        wavelength_usage[least_used_w] += 1
                        wavelength_allocation[least_used_w + 1].append((node1, node2))

    blocked_percentage = (blocked_requests / total_requests) * 100 if total_requests > 0 else 0
    return blocked_percentage, wavelength_allocation
