def convert_data_structure(input_data):
    """ 
    # Example input data
    input_data = {
        "Arguments": {
            "0": "a",
            "1": "b",
            "2": "c",
            "3": "d",
            "4": "e"
        },
        "Attack Relations": [
            ["0", "1"],
            ["2", "1"],
            ["2", "3"],
            ["3", "2"],
            ["3", "4"],
            ["4", "4"]
        ]
    }

    # Convert the data

    """
    #  dictionary for the new structure
    converted = {}

    # going through the attack relations
    for attack in input_data["Attack Relations"]:#iterate over each item in the list input_data
        attacker, attacked = attack #Here, the two elements of each attack list are unpacked into two variables: attacker and attacked.

        # If the attacker is not in the converted structure, add it,
        if attacker not in converted:
            converted[attacker] = {"attacks": [], "attacked": []}

        # If the attacked is not in the converted structure, add it
        if attacked not in converted:
            converted[attacked] = {"attacks": [], "attacked": []}

        # Add the attack relation to the converted structure
        converted[attacker]["attacks"].append(attacked)
        converted[attacked]["attacked"].append(attacker)

    return converted

if __name__ == '__main__':
    

    input_data = {
        "Arguments": {
            "0": "a",
            "1": "b",
            "2": "c",
            "3": "d",
            "4": "e"
        },
        "Attack Relations": [
            [
                "0",
                "1"
            ],
            [
                "2",
                "1"
            ],
            [
                "2",
                "3"
            ],
            [
                "3",
                "2"
            ],
            [
                "3",
                "4"
            ],
            [
                "4",
                "4"
            ]
        ]
    }
#     input_data = {
#     "Arguments" : {
#         "0": "We should go to the cinema.",
#         "1": "We should go to the gym.",
#         "2": "The gym is better for the health than the cinema.",
#         "3": "We have no time for evening activities, since there is an exam coming up.",
#         "4": "The exam is in a few weeks.",
#         "5": "We have no money for cinema or gym.",
#         "6": "We just got our sallaries."
#     },
    
#     "Attack Relations" : [
#         ["0","1"], ["1","0"], ["2","0"], 
#         ["3","0"], ["3","1"], ["4","3"],
#         ["5","0"], ["5","1"], ["6","5"]
#     ]
# }

    converted_data = convert_data_structure(input_data)
    print(converted_data)