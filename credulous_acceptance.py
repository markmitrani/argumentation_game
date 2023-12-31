from admissible import get_admissible_sets
from conflict_free import get_conflict_free_sets
from preferred import get_preferred_sets
from complete_and_grounded import get_complete_sets, get_grounded_sets
from stable import get_stable_extensions

from graph import convert_data_structure
import json
import os
import sys

def credulous_acceptance(framework, argument = None, labels = None):
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
        
        if None, all arguments will be evaluated.

        labels (dict): The labels of the arguments.

        It should be in the following format:
        {
            '0': 'a',
            '1': 'b',
            '2': 'c',
            '3': 'd',
            '4': 'e'
        }
        Where the key is the argument identifier and the value is the label.

    Returns:
        None
    """

    arguments = framework.keys()

    if argument is not None:
        arguments = [argument]
        if argument not in framework:
            raise(f"Argument id {argument} does not exist in the framework.")
            

    print("Conflict-free sets:")
    cf_sets = get_conflict_free_sets(framework)
    print(cf_sets)
   
    for argument in arguments:
        is_arg_contained = argument_contained(cf_sets, argument)
        arg_str = labels[argument]+f" (id: {argument})" if labels is not None else argument
        if is_arg_contained:
            print(f"{arg_str} is contained in at least one conflict-free set")
        else:
            print(f"{arg_str} is not contained in any conflict-free set")
    
    print("-"*50)
    print("Admissible sets:")
    admissible_sets = get_admissible_sets(cf_sets, framework)
    print(admissible_sets)
    
    for argument in arguments:
        is_arg_contained = argument_contained(admissible_sets, argument)
        arg_str = labels[argument]+f" (id: {argument})" if labels is not None else argument
        if is_arg_contained:
            print(f"{arg_str} is credously accepted w.r.t. the admissible semantics")
        else:
            print(f"{arg_str} is not credously accepted w.r.t. the admissible semantics")

    print("-"*50)
    print("Stable extensions:")
    stable_extensions = get_stable_extensions(admissible_sets, framework)
    print(stable_extensions)
    
    for argument in arguments:
        is_arg_contained = argument_contained(stable_extensions, argument)
        arg_str = labels[argument]+f" (id: {argument})" if labels is not None else argument
        if is_arg_contained:
            print(f"{arg_str} is credously accepted w.r.t. the stable semantics")
        else:
            print(f"{arg_str} is not credously accepted w.r.t. the stable semantics")


    print("-"*50)
    print("Preferred sets:")
    preferred_sets = get_preferred_sets(admissible_sets)
    print(preferred_sets)
  
    for argument in arguments:
        is_arg_contained = argument_contained(preferred_sets, argument)
        arg_str = labels[argument]+f" (id: {argument})" if labels is not None else argument
        if is_arg_contained:
            
            print(f"{arg_str} is credously accepted w.r.t. the preferred semantics")
        else:
            print(f"{arg_str} is not credously accepted w.r.t. the preferred semantics")

    print("-"*50)
    print("Complete sets:")
    complete_sets = get_complete_sets(framework, admissible_sets)
    print(complete_sets)
    is_arg_contained = argument_contained(complete_sets, argument)
    for argument in arguments:
        is_arg_contained = argument_contained(complete_sets, argument)
        arg_str = labels[argument]+f" (id: {argument})" if labels is not None else argument
        if is_arg_contained:
            print(f"{arg_str} is credously accepted w.r.t. the complete semantics")
        else:
            print(f"{arg_str} is not credously accepted w.r.t. the complete semantics")

    print("-"*50)
    print("Grounded sets:")
    grounded_sets = get_grounded_sets(framework, complete_sets)
    print(grounded_sets)
    is_arg_contained = argument_contained(grounded_sets, argument)
    for argument in arguments:
        is_arg_contained = argument_contained(grounded_sets, argument)
        arg_str = labels[argument]+f" (id: {argument})" if labels is not None else argument
        
        if is_arg_contained:
            print(f"{arg_str} is credously accepted w.r.t. the grounded semantics")
        else:
            print(f"{arg_str} is not credously accepted w.r.t. the grounded semantics")

def credulous_acceptance_from_file(path_to_framework, argument=None, include_labels=True):
    """
    Load an argumentation framework from a JSON file and perform credulous acceptance.

    Args:
        path_to_framework (str): The path to the JSON file containing the argumentation framework.
        argument (str, optional): The specific argument to evaluate for credulous acceptance. Defaults to None.
        include_labels (bool, optional): Whether to include labels for the arguments in the framework. Defaults to True.

    Raises:
        Exception: If the provided JSON file does not exist or is not a valid JSON file.

    Returns:
        None

    Example JSON format:
    {
        "Arguments": {
            "0": "We should go to the cinema.",
            "1": "We should go to the gym.",
            "2": "The gym is better for the health than the cinema.",
            "3": "We have no time for evening activities, since there is an exam coming up.",
            "4": "The exam is in a few weeks.",
            "5": "We have no money for cinema or gym.",
            "6": "We just got our salaries."
        },
        "Attack Relations": [
            ["0","1"], ["1","0"], ["2","0"],
            ["3","0"], ["3","1"], ["4","3"],
            ["5","0"], ["5","1"], ["6","5"]
        ]
    }
    """
    if not os.path.exists(path_to_framework):
        raise Exception("Please enter a valid JSON file, the file you provided does not exist.")
    if not path_to_framework.endswith(".json"):
        raise Exception("Please enter a valid JSON file, the file you provided is not a JSON file.")
    
    # load JSON
    with open(path_to_framework, "r") as file:
        input_data = json.load(file)

    if include_labels:
        # perform credulous acceptance
        if "Arguments" not in input_data:
            raise Exception("Please enter a valid json file with Arguments key")
        labels = input_data["Arguments"]

    framework = convert_data_structure(input_data)
    
    credulous_acceptance(framework, argument, labels)
    
        

def argument_contained(sets, argument):
    for set_ in sets:
        if argument in set_:
            return True
    return False

def handle_cli_call(args):
    if len(args) != 2:
        print("Please enter the correct number of arguments.")
        print("Usage: python credulous_acceptance.py FULL_PATH_TO_FRAMEWORK ARGUMENT_IDENTIFIER")
        sys.exit(1)

    framework_path = args[0]
    argument_id = args[1]

    if not os.path.exists(framework_path):
        print(f"File {framework_path} does not exist.")
        print("Usage: python credulous_acceptance.py FULL_PATH_TO_FRAMEWORK ARGUMENT_IDENTIFIER")
        sys.exit(1)

    if not framework_path.endswith(".json"):
        print("The file provided is not a json file.")
        print("You provided: ", framework_path)
        print("Usage: python credulous_acceptance.py FULL_PATH_TO_FRAMEWORK ARGUMENT_IDENTIFIER")
        sys.exit(1)
    
    return framework_path, argument_id

if __name__ == '__main__':
    args = sys.argv[1:]

    framework_path = 'frameworks/example_2.json' #provide full path if not working
    arg_id = '0'
    
    if len(args) == 0:
        pass
    else:
        framework_path, arg_id = handle_cli_call(args)
    

    try:
        credulous_acceptance_from_file(framework_path, arg_id)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
