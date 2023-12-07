def find_stable_extensions(sets, info_graph):
    stable_extensions = []

    # Get all elements from the info_graph
    all_elements = set(info_graph.keys())

    # Check if the set attacks all elements not in the set
    def attacks_all_outside(set_):
        outside_elements = all_elements - set_
        return all(any(attacked in info_graph[attacker]['attacks'] for attacker in set_) for attacked in outside_elements)

    for set_ in sets:
        set_as_set = set(set_)  # Convert to a set for set operations
        if attacks_all_outside(set_as_set):
            stable_extensions.append(set_as_set)

    return stable_extensions

# ex usage
sets = [{'0', '2'}, {'0', '3'}, {'0'}]  # this would be the input of conflict-free sets(like for my calculations)
info_graph = {'0': {'attacks': ['1'], 'attacked': []}, '1': {'attacks': [], 'attacked': ['0', '2']}, '2': {'attacks': ['1', '3'], 'attacked': ['3']}, '3': {'attacks': ['2', '4'], 'attacked': ['2']}, '4': {'attacks': ['4'], 'attacked': ['3', '4']}}
stable_extensions = find_stable_extensions(sets, info_graph)
print(stable_extensions)
