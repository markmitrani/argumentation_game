# Check if a set is a subset of any other set
def is_subset_of_any(set_, sets):
    return any(set_ < other_set for other_set in sets)#set_ and a list of sets and return True if set_ is a proper subset of any set in sets

def find_preferred_sets(admissible_sets):
    preferred_sets = []
    # Find preferred (we can also say max admissible) sets check each set
    for set_ in admissible_sets:
        if not is_subset_of_any(set_, admissible_sets):
            preferred_sets.append(set_)
    return preferred_sets

#ex usage 
admissible_sets = [{"1", "2"}, {"1", "4"}, {"1"}]
preferred_sets = find_preferred_sets(admissible_sets)
print(preferred_sets)
