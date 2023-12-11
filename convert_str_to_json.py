import json

import json
import re


def convert_to_json_and_save(argumentation_str, output_file):
    # Find the indices of the opening and closing curly braces for arguments
    arguments_start = argumentation_str.find("{")
    arguments_end = argumentation_str.find("}", arguments_start + 1)

    # Find the indices of the opening and closing curly braces for attack relations
    attack_relations_start = argumentation_str.find("{", arguments_end + 1)
    attack_relations_end = argumentation_str.find("}", attack_relations_start + 1)

    # Extract arguments
    arguments_str = argumentation_str[arguments_start + 1: arguments_end]
    arguments_list = [arg.strip() for arg in arguments_str.split(",")]

    # Extract attack relations
    attack_relations_str = argumentation_str[attack_relations_start + 1: attack_relations_end]
    attack_relations_list = re.findall(r'\((.*?),\s(.*?)\)', attack_relations_str)

    # Convert attacker's names to numbers in attack relations
    converted_attack_relations = [[str(arguments_list.index(attacker)), str(arguments_list.index(target))] for attacker, target in attack_relations_list]

    # Create a dictionary in the desired format
    argumentation_json = {
        "Arguments": {str(i): arg for i, arg in enumerate(arguments_list)},
        "Attack Relations": converted_attack_relations
    }

    # Save the JSON to the specified file
    with open(output_file, 'w') as json_file:
        json.dump(argumentation_json, json_file, indent=4)

if __name__ == '__main__':
    # Example usage
    argumentation_str = "AF F = ({a, b, c, d, e, k}, {(e, d), (d, b), (b, a), (c, b), (a, k)})"
    # AF F = ({a, b, c, d, e}, {(a, b), (c, b), (c, d), (d, c), (d, e), (e, e)})
    # AF F = ({a, b, c, d, e}, {(a, b), (c, b), (c, d), (d, c), (d, e), (e, e)})
    # AF F = ({a, b, c, d, e}, {(a, b), (b, a), (b, c), (c, d), (d, e), (e, c)})
    output_file = "frameworks/output.json"
    argumentation_str = input("Provide the argumentation framework string")
    output_file = input("Provide output file name")
    convert_to_json_and_save(argumentation_str, output_file)
