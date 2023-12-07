def find_admissible_sets(sets, info_graph):
    admissible_sets = []

    # Check if an element is defended
    def is_defended(element, set_):
        # An element defends itself if it attacks someone outside the set
        if any(target not in set_ for target in info_graph[element]['attacks']):
            return True

        # Or it is defended by another element in the set
        for defender in set_:
            if defender != element and element in info_graph[defender]['attacks']:
                return True
        return False

    # Determine admissibility for each set
    for set_ in sets:
        # Ensure no internal attacks within the set
        if any(attacker in set_ for element in set_ for attacker in info_graph[element]['attacked']):
            continue

        # Check if each element is defended
        if all(is_defended(element, set_) for element in set_):
            admissible_sets.append(set_)

    return admissible_sets

# Example usage
sets = [{"0", "2"}, {"0"},{"0","3"}]
info_graph = {'0': {'attacks': ['1'], 'attacked': []}, '1': {'attacks': [], 'attacked': ['0', '2']}, '2': {'attacks': ['1', '3'], 'attacked': ['3']}, '3': {'attacks': ['2', '4'], 'attacked': ['2']}, '4': {'attacks': ['4'], 'attacked': ['3', '4']}}
admissible_sets = find_admissible_sets(sets, info_graph)
print(admissible_sets)

