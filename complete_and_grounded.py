from admissible import is_defended

def characteristic_function(framework, set_):
    result = set()
    all_args = framework.keys()
    for arg in all_args:
        if is_defended(arg, set_, framework):
            result.add(arg)
    return frozenset(result)

def get_complete_sets(framework, admissible_sets):
    complete_sets = set()
    for set_ in admissible_sets:
        if characteristic_function(framework, set_) == set_:
            complete_sets.add(set_)
    return complete_sets

def get_grounded_sets(framework, complete_sets):
    # All the sets that are subsets of all the other sets
    grounded_sets= set()
    for set_ in complete_sets:
        if not any(other_set <= set_ for other_set in complete_sets):
            grounded_sets.add(set_)

    return grounded_sets
    
