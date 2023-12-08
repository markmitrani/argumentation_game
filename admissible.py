 # Check if an element is defended
def is_defended(element, set_, framework):

    # get all attackers of the element
    attackers = framework[element]['attacked']

    if len(attackers) == 0:
        return True

    for attacker in attackers:
        # Check if the attacker is in the set
        # if attacker in set_:
        #     assert False, "Internal attacks within the set"
        # -----Commented out since we since we use this function also to check if an argument outside the set is defended by it, not if a set is admissible----
        
        # Check if another node within the set attacks the attacker
        if any(attacker in framework[element]['attacks'] for element in set_):
            return True  

    return False

    # # An element defends itself if it attacks someone outside the set
    # if any(target not in set_ for target in framework[element]['attacks']):
    #     return True

    # # Or it is defended by another element in the set
    # for defender in set_:
    #     if defender != element and element in framework[defender]['attacks']:
    #         return True
    # return False


def find_admissible_sets(sets, framework):
    admissible_sets = set()

    # Determine admissibility for each set
    for set_ in sets:

        # Check if each element is defended
        if all(is_defended(element, set_, framework) for element in set_):
            admissible_sets.add(set_)

    return admissible_sets

if __name__ == '__main__':
    # Example usage
    sets = {frozenset({"0", "2"}), frozenset({"0"}),frozenset({"0","3"})}
    framework = {'0': {'attacks': ['1'], 'attacked': []}, '1': {'attacks': [], 'attacked': ['0', '2']}, '2': {'attacks': ['1', '3'], 'attacked': ['3']}, '3': {'attacks': ['2', '4'], 'attacked': ['2']}, '4': {'attacks': ['4'], 'attacked': ['3', '4']}}
    admissible_sets = find_admissible_sets(sets, framework)
    print(admissible_sets)

