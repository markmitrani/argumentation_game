from admissible import find_admissible_sets
from conflict_free import conflict_free_sets_containing_arg
from preferred import find_preferred_sets
from complete_and_grounded import get_complete_sets, get_grounded_sets


def credulous_acceptance(framework, argument):
    pass # TODO

def argument_contained(sets, argument):
    for set_ in sets:
        if argument in set_:
            return True
    return False

def convert_data_structure(input_data):
    converted = {}
    for attack in input_data["Attack Relations"]:
        attacker, attacked = attack
        if attacker not in converted:
            converted[attacker] = {"attacks": [], "attacked": []}
        if attacked not in converted:
            converted[attacked] = {"attacks": [], "attacked": []}
        converted[attacker]["attacks"].append(attacked)
        converted[attacked]["attacked"].append(attacker)
    return converted

if __name__ == '__main__':
    arg = '1'

    # Define the input data for the attack relations
    input_data = {
        "Attack Relations": [
            ('0', '1'), 
            ('1', '0'), ('1', '2'),
            ('2', '1'), ('2', '3'),
            ('3', '2'), ('3', '4'),
            ('4', '3'), ('4', '4')
        ]
    }
    framework = convert_data_structure(input_data)
    
    print("-"*50)
    print("Conflict-free sets:")
    cf_sets = conflict_free_sets_containing_arg(framework, arg)
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

