from admissible import find_admissible_sets
from cf_single_argument import conflict_free_sets_containing_arg
from preferred import find_preferred_sets


def credulous_acceptance(framework, argument):
    pass # TODO


if __name__=='__main__':
    arg = '1'
    framework = {
        '0': {'attacks': ['1'], 'attacked': []},
        '1': {'attacks': [], 'attacked': ['0', '2']},
        '2': {'attacks': ['1', '3'], 'attacked': ['3']},
        '3': {'attacks': ['2', '4'], 'attacked': ['2']},
        '4': {'attacks': ['4'], 'attacked': ['3', '4']}
    }
    

    print("-"*50)
    print(f"Conflict-free sets containing the argument: {arg}")
    cf_sets = conflict_free_sets_containing_arg(framework, arg)
    print(cf_sets)

    print("-"*50)
    print(f"Admissible sets containing the argument: {arg}")
    admissible_sets = find_admissible_sets(cf_sets, framework)
    print(admissible_sets)

    print("-"*50)
    print(f"Preferred sets containing the argument: {arg}")
    preferred_sets = find_preferred_sets(admissible_sets)
    print(preferred_sets)