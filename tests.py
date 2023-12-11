import os
from credulous_acceptance import credulous_acceptance_from_file

import cProfile
import pstats

def get_framework_files():
    # get the path of the folder containing the frameworks
    folder_path = os.path.join(os.path.dirname(__file__), 'frameworks')

    # get all the JSON framework files in the folder
    files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

    # remove the non-json files
    files = [file for file in files if file.endswith(".json")]


    return files
def test_over_all_files():
    # List of arguments to check
    #arguments_to_check = ['1', '2', '3', '4', '5', '6']

    # get all the framework files
    files = get_framework_files()
    

    for file in files:
        # get the name of the file
        filename = os.path.basename(file)
        
        
        print(f"Credulous acceptance for {filename}:")
        print("")
        
        credulous_acceptance_from_file(file)
    
        print("-"*50)
        print("-"*50)


def get_computation_times(file):

    with cProfile.Profile() as pr:
        credulous_acceptance_from_file(file, argument='0')

    ps = pstats.Stats(pr)
    ps.precision = 10 
    ps = ps.sort_stats(pstats.SortKey.TIME)
    
    ps.print_stats()

    functions = ["get_conflict_free_sets", "get_admissible_sets", "get_complete_sets", "get_grounded_sets", "credulous_acceptance", "get_stable_extensions", "get_preferred_sets","argument_contained"]

    computation_times = {}

    for key, (cc, nc, tt, ct, callers) in ps.stats.items():
        file_path = key[0]  # key[0] is the file name with its path
        if "argumentation_game" in file_path:

            if key[-1] not in functions:
                continue

            # You can process func_stats here as needed, for example, print them
            if not cc == nc:
                continue


            print(f"{key[-1]}: ", f"total calls: {cc}, Cumulative time: {ct/cc}")

            computation_times[key[-1]] = (cc, ct)
    
    return computation_times
if __name__ == '__main__':
    test_over_all_files()
    #get_computation_times(get_framework_files()[0])
    
    