import json

def get_conflict_free(framework):
    arguments = framework["Arguments"]
    rels = framework["Attack Relations"]
    cfset = set(frozenset())
    for arg in arguments:
        if [arg, arg] not in rels:
            cfset.add(frozenset(arg))

    prevset = set(frozenset())
    while prevset != cfset:
        prevset = cfset.copy()
        for set1 in prevset:
            not_cf = False
            for set2 in prevset:
                for elems1 in set1:
                    for elems2 in set2:
                        if [elems1, elems2] in rels or [elems2, elems1] in rels:
                            print(elems1, elems2)
                            not_cf = True
                if not not_cf:
                    cfset.add(frozenset(set1.union(set2)))
                not_cf = False

    transformed_set = {frozenset(framework["Arguments"][item] for item in frozenset_item) for frozenset_item in cfset}
    print(transformed_set)

    return cfset

def main():
    filename = input("choose your framework:")
    if not filename.endswith(".json"):
        filename = filename+".json"

    # load json
    with open("frameworks/"+filename, "r") as file:
        framework = json.load(file)
        print(type(framework))
        print(framework)
        print("Argumentation framework loaded.")

    get_conflict_free(framework)


if __name__ == '__main__':
    main()