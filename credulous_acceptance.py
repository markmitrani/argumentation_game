from admissible import find_admissible_sets
from conflict_free import conflict_free_sets_containing_arg
from preferred import find_preferred_sets
from complete_and_grounded import get_complete_sets, get_grounded_sets
from stable import find_stable_extensions

from graph import convert_data_structure
import json
import os

def credulous_acceptance(framework, argument):
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
    print("Conflict-free sets:")
    cf_sets = conflict_free_sets_containing_arg(framework)
    print(cf_sets)
    is_arg_contained = argument_contained(cf_sets, argument)
    if is_arg_contained:
        print(f"{argument} is contained in at least one conflict-free set")
    else:
        print(f"{argument} is not contained in any conflict-free set")
    
    print("-"*50)
    print("Admissible sets:")
    admissible_sets = find_admissible_sets(cf_sets, framework)
    print(admissible_sets)
    is_arg_contained = argument_contained(admissible_sets, argument)
    if is_arg_contained:
        print(f"{argument} is contained in at least one admissible set")
    else:
        print(f"{argument} is not contained in any admissible set")

    print("-"*50)
    print("Stable extensions:")
    stable_extensions = find_stable_extensions(admissible_sets, framework)
    print(stable_extensions)
    is_arg_contained = argument_contained(stable_extensions, argument)
    if is_arg_contained:
        print(f"{argument} is contained in at least one stable extension")
    else:
        print(f"{argument} is not contained in any stable extension")


    print("-"*50)
    print("Preferred sets:")
    preferred_sets = find_preferred_sets(admissible_sets)
    print(preferred_sets)
    is_arg_contained = argument_contained(preferred_sets, argument)
    if is_arg_contained:
        print(f"{argument} is contained in at least one preferred set")
    else:
        print(f"{argument} is not contained in any preferred set")

    print("-"*50)
    print("Complete sets:")
    complete_sets = get_complete_sets(framework, admissible_sets)
    print(complete_sets)
    is_arg_contained = argument_contained(complete_sets, argument)
    if is_arg_contained:
        print(f"{argument} is contained in at least one complete set")
    else:
        print(f"{argument} is not contained in any complete set")

    print("-"*50)
    print("Grounded sets:")
    grounded_set = get_grounded_sets(framework, complete_sets)
    print(grounded_set)
    is_arg_contained = argument_contained(grounded_set, argument)
    if is_arg_contained:
        print(f"{argument} is contained in at least one grounded set")
    else:
        print(f"{argument} is not contained in any grounded set")


def credulous_acceptance_from_file(path_to_framework, argument):
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
    framework = convert_data_structure(input_data)

    credulous_acceptance(framework, argument)


    

def argument_contained(sets, argument):
    for set_ in sets:
        if argument in set_:
            return True
    return False


if __name__ == '__main__':
    argument = '1'

    # get the path of the folder containing the frameworks
    folder_path = os.path.join(os.path.dirname(__file__), 'frameworks')

    # get all the JSON framework files in the folder
    files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

    # remove the non-json files
    files = [file for file in files if file.endswith(".json")]

    for file in files:
        
        # get the name of the file
        filename = os.path.basename(file)
        
        print(f"Credulous acceptance for {filename}:")
        print("")
        
        credulous_acceptance_from_file(file, argument)
    
        print("-"*50)
        print("-"*50)