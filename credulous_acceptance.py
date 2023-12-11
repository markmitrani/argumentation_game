from admissible import get_admissible_sets
from conflict_free import get_conflict_free_sets
from preferred import get_preferred_sets
from complete_and_grounded import get_complete_sets, get_grounded_sets
from stable import get_stable_extensions

from graph import convert_data_structure
import json
import os


def credulous_acceptance(framework, argument = None):
    """
    Determines the acceptance of an argument in different sets of an argumentation framework.

    Args:
        framework (dict): The argumentation framework in the converted data structure.
                        
        It should be in the following format:
        {
            '0': {'attacks': ['1'], 'attacked': []},
            '1': {'attacks': [], 'attacked': ['0', '2']},
            '2': {'attacks': ['1', '3'], 'attacked': ['3']},
            '3': {'attacks': ['2', '4'], 'attacked': ['2']},
            '4': {'attacks': ['4'], 'attacked': ['3', '4']}
        }                  

        argument (str): The argument to be evaluated.

    Returns:
        None
    """

    arguments = framework.keys()

    if argument is not None:
        arguments = [argument]

    print("Conflict-free sets:")
    cf_sets = get_conflict_free_sets(framework)
    print(cf_sets)
   
    for argument in arguments:
        is_arg_contained = argument_contained(cf_sets, argument)
        if is_arg_contained:
            print(f"{argument} is contained in at least one conflict-free set")
        else:
            print(f"{argument} is not contained in any conflict-free set")
    
    print("-"*50)
    print("Admissible sets:")
    admissible_sets = get_admissible_sets(cf_sets, framework)
    print(admissible_sets)
    
    for argument in arguments:
        is_arg_contained = argument_contained(admissible_sets, argument)
        if is_arg_contained:
            print(f"{argument} is credously accepted w.r.t. the admissible semantics")
        else:
            print(f"{argument} is not credously accepted w.r.t. the admissible semantics")

    print("-"*50)
    print("Stable extensions:")
    stable_extensions = get_stable_extensions(admissible_sets, framework)
    print(stable_extensions)
    
    for argument in arguments:
        is_arg_contained = argument_contained(stable_extensions, argument)
        if is_arg_contained:
            print(f"{argument} is credously accepted w.r.t. the stable semantics")
        else:
            print(f"{argument} is not credously accepted w.r.t. the stable semantics")


    print("-"*50)
    print("Preferred sets:")
    preferred_sets = get_preferred_sets(admissible_sets)
    print(preferred_sets)
  
    for argument in arguments:
        is_arg_contained = argument_contained(preferred_sets, argument)
        if is_arg_contained:
            print(f"{argument} is credously accepted w.r.t. the preferred semantics")
        else:
            print(f"{argument} is not credously accepted w.r.t. the preferred semantics")

    print("-"*50)
    print("Complete sets:")
    complete_sets = get_complete_sets(framework, admissible_sets)
    print(complete_sets)
    is_arg_contained = argument_contained(complete_sets, argument)
    for argument in arguments:
        is_arg_contained = argument_contained(preferred_sets, argument)
        if is_arg_contained:
            print(f"{argument} is credously accepted w.r.t. the complete semantics")
        else:
            print(f"{argument} is not credously accepted w.r.t. the complete semantics")

    print("-"*50)
    print("Grounded sets:")
    grounded_set = get_grounded_sets(framework, complete_sets)
    print(grounded_set)
    is_arg_contained = argument_contained(grounded_set, argument)
    for argument in arguments:
        is_arg_contained = argument_contained(preferred_sets, argument)
        if is_arg_contained:
            print(f"{argument} is credously accepted w.r.t. the grounded semantics")
        else:
            print(f"{argument} is not credously accepted w.r.t. the grounded semantics")

def credulous_acceptance_from_file(path_to_framework, argument = None):
    # Define the input data for the attack relations
    if not path_to_framework.endswith(".json"):
        print("Please enter a valid json file")
        return

    # load json
    with open(path_to_framework, "r") as file:
        input_data = json.load(file)
        #print(type(input_data))
        #print(input_data)
        #print("Argumentation framework loaded.")

    # Convert the dictionary to have the attackers and attacked for each argument
    # 
        
    framework = convert_data_structure(input_data)
    
    credulous_acceptance(framework, argument)
    
        

def argument_contained(sets, argument):
    for set_ in sets:
        if argument in set_:
            return True
    return False


if __name__ == '__main__':
    # List of arguments to check
    #arguments_to_check = ['1', '2', '3', '4', '5', '6']

    pass
