# Check if a set is a subset of any other set
def is_subset_of_any(set_, sets):
    return any(set_ < other_set for other_set in sets)#set_ and a list of sets and return True if set_ is a proper subset of any set in sets

def get_preferred_sets(admissible_sets):
    preferred_sets = set()
    # Find preferred (we can also say max admissible) sets
    for set_ in admissible_sets:
        if not is_subset_of_any(set_, admissible_sets):
            preferred_sets.add(set_)
    return preferred_sets

if __name__ == '__main__':
    #ex usage 
    admissible_sets = [{"1", "2"}, {"1", "4"}, {"1"}]
    preferred_sets = get_preferred_sets(admissible_sets)
    print(preferred_sets)
