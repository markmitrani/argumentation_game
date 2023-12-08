from admissible import find_admissible_sets
from conflict_free import conflict_free_sets_containing_arg
from preferred import find_preferred_sets
from complete_and_grounded import get_complete_sets, get_grounded_sets
from stable import find_stable_extensions


def credulous_acceptance(framework, argument):
    pass # TODO

def argument_contained(sets, argument):
    for set_ in sets:
        if argument in set_:
            return True
    return False

if __name__=='__main__':
    arg = '1'
    framework = {
        '0': {'attacks': ['1'], 'attacked': ['1']},
        '1': {'attacks': ['0'], 'attacked': ['0', '2']},
        '2': {'attacks': ['1', '3'], 'attacked': ['3']},
        '3': {'attacks': ['2', '4'], 'attacked': ['2']},
        '4': {'attacks': ['4'], 'attacked': ['3', '4']}
    }
    

    print("-"*50)
    print("Conflict-free sets:")
    cf_sets = conflict_free_sets_containing_arg(framework)
    print(cf_sets)
    is_arg_contained = argument_contained(cf_sets, arg)
    if is_arg_contained:
        print(f"{arg} is contained in at least one conflict-free set")
    else:
        print(f"{arg} is not contained in any conflict-free set")

    
    print("-"*50)
    print("Admissible sets:")
    admissible_sets = find_admissible_sets(cf_sets, framework)
    print(admissible_sets)
    is_arg_contained = argument_contained(admissible_sets, arg)
    if is_arg_contained:
        print(f"{arg} is contained in at least one admissible set")
    else:
        print(f"{arg} is not contained in any admissible set")

    print("-"*50)
    print("Stable extensions:")
    stable_extensions = find_stable_extensions(admissible_sets, framework)
    print(stable_extensions)
    is_arg_contained = argument_contained(stable_extensions, arg)
    if is_arg_contained:
        print(f"{arg} is contained in at least one stable extension")
    else:
        print(f"{arg} is not contained in any stable extension")


    print("-"*50)
    print("Preferred sets:")
    preferred_sets = find_preferred_sets(admissible_sets)
    print(preferred_sets)
    is_arg_contained = argument_contained(preferred_sets, arg)
    if is_arg_contained:
        print(f"{arg} is contained in at least one preferred set")
    else:
        print(f"{arg} is not contained in any preferred set")

    print("-"*50)
    print("Complete sets:")
    complete_sets = get_complete_sets(framework, admissible_sets)
    print(complete_sets)
    is_arg_contained = argument_contained(complete_sets, arg)
    if is_arg_contained:
        print(f"{arg} is contained in at least one complete set")
    else:
        print(f"{arg} is not contained in any complete set")

    print("-"*50)
    print("Grounded sets:")
    grounded_set = get_grounded_sets(framework, complete_sets)
    print(grounded_set)
    is_arg_contained = argument_contained(grounded_set, arg)
    if is_arg_contained:
        print(f"{arg} is contained in at least one grounded set")
    else:
        print(f"{arg} is not contained in any grounded set")



