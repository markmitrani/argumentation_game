from itertools import chain, combinations

def all_subsets(ss):
    """ Generate all subsets of a set.

        -the combination function generates all subsets of a given size
        -the map function applies the combination function to all sizes
        -chain combines all the subsets of different sizes
        -the star operator unpacks the chain object into a list of arguments for the set constructor

        Parameters:
        ss (iterable): An iterable (like a list or set) for which all possible subsets need to be generated.

        Returns:
        itertools.chain: An iterator that yields all subsets of 'ss'. Each subset is represented as a tuple.
    """
    return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))

def is_conflict_free(subset, framework):
    """ Check if a subset is conflict-free in the given framework. """
    for arg in subset:
        # Check if the argument attacks any other in the subset
        if any(attacked in subset for attacked in framework[arg]['attacks']):
            return False
    return True

def conflict_free_sets_containing_arg(framework, argument):
    """ Find all conflict-free sets containing the specified argument. """
    all_args = set(framework.keys())
    conflict_free_sets = set()

    for subset in all_subsets(all_args):

        if is_conflict_free(subset, framework):
            conflict_free_sets.add(frozenset(subset))

    return conflict_free_sets


if __name__ == '__main__':

    # Example framework
    framework = {
        '0': {'attacks': ['1'], 'attacked': []},
        '1': {'attacks': [], 'attacked': ['0', '2']},
        '2': {'attacks': ['1', '3'], 'attacked': ['3']},
        '3': {'attacks': ['2', '4'], 'attacked': ['2']},
        '4': {'attacks': ['4'], 'attacked': ['3', '4']}
    }
    
    print("All subsets:")
    print(list(all_subsets(framework.keys())))
    for subset in all_subsets(framework.keys()):
        assert type(subset) == tuple, "all_subsets should return tuples"
        break

    subset = ('1', '4')
    print(f"Is the subset {subset} conflict-free?")
    print(is_conflict_free(("1","4"), framework))

    print("Conflict-free sets containing the argument:")
    cf_set = conflict_free_sets_containing_arg(framework, '1')

    print(cf_set)

    
