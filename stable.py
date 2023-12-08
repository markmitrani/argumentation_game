# Check if the set attacks all elements not in the set
def is_stable(set_, framework):

    # Get all elements from the framework
    all_elements = set(framework.keys())
    outside_elements = all_elements - set_
    return all(any(attacked in framework[attacker]['attacks'] for attacker in set_) for attacked in outside_elements)


def find_stable_extensions(sets, framework):
    stable_extensions = set()

    for set_ in sets:  
        if is_stable(set_, framework):
            stable_extensions.add(set_)

    return stable_extensions

if __name__ == '__main__':
    # ex usage
    sets = {frozenset({'0', '2'}), frozenset({'0', '3'}), frozenset({'0'})}  # this would be the input of conflict-free sets(like for my calculations)
    framework = {'0': {'attacks': ['1'], 'attacked': []}, '1': {'attacks': [], 'attacked': ['0', '2']}, '2': {'attacks': ['1', '3'], 'attacked': ['3']}, '3': {'attacks': ['2', '4'], 'attacked': ['2']}, '4': {'attacks': ['4'], 'attacked': ['3', '4']}}
    stable_extensions = find_stable_extensions(sets, framework)
    print(stable_extensions)
