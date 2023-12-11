import copy
import json

def find_attackers(framework, arg_id):
    attackers = set()
    for attack in framework["Attack Relations"]:
        if attack[1] == arg_id:
            attackers.add(attack[0])
    return attackers

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

def is_arg_in_adm(framework, argument):
    arguments = framework["Arguments"]
    rels = framework["Attack Relations"]

    # Initialize label dictionary with each argument labeled undec initially
    labels = {arg: "undec" for arg in arguments}

    # Argument is sent as string. Get the corresponding key by inverse dict search
    argument_id = "default"
    for id, name in arguments.items():
        if argument == name:
            argument_id = id

    # Set the claimed argument's label to in.
    labels[argument_id] = "in"
    print("our argument:",argument_id,"is in.")

    changed = True
    while changed:
        arguments_in = [x for x in labels if labels[x] == "in"]


        # for every argument labeled in: the attackers must be labeled out.
        for inside in arguments_in:
            attackers = find_attackers(framework, inside)
            for attacker in attackers:
                # these are the ones that need to be changed
                if attacker not in arguments_in:
                    labels[attacker] = "out"
                    changed = True
                    print("Since",inside,"is labeled in,",attacker,"must be labeled out.")
                else:
                    return {}

        arguments_out = [x for x in labels if labels[x] == "out"]
        for outside in arguments_out:
            attackers = find_attackers(framework, outside)
            print("Since",outside,"is labeled out, it must have an attacker that is labeled in.")
            # if we can find an argument that is labeled in, then it's justified to out this argument.
            # the attackers have to be smart enough.

        changed = False

    print(labels[argument_id])
    print(labels)


def admissible_labeling(framework, ins, outs, undecs):
    if len(ins.intersection(outs)) > 0:
        print(ins, outs)
        return (set(), set(), set())
    arguments = framework["Arguments"]
    rels = framework["Attack Relations"]

    # base case: checking for completeness
    complete = True
    for inside in ins:
        attackers = find_attackers(framework, inside)
        for attacker in attackers:
            if attacker not in outs:
                print('hit')
                complete = False
    for outside in outs:
        attackers = find_attackers(framework, outside)
        if len(attackers.intersection(ins)) < 1:
            complete = False
    if complete:
        return copy.deepcopy(ins), copy.deepcopy(outs), copy.deepcopy(undecs)

    # normal case
    for inside in ins:
        attackers = find_attackers(framework, inside)
        for attacker in attackers:
            if attacker not in outs:
                outs.add(attacker)

    interim_results = []
    for outside in outs:
        attackers = find_attackers(framework, outside)
        if len(ins.intersection(attackers)) == 0:
            for attacker in attackers:
                ins_copy = copy.deepcopy(ins)
                ins_copy.add(attacker)
                interim_results.append(admissible_labeling(framework, ins_copy, copy.deepcopy(outs), copy.deepcopy(undecs)))

    max_len = 0
    max_set = (set(), set(), set())
    for r in interim_results:
        if len(r[0]) > max_len:
            max_len = len(r[0])
            max_set = r

    return max_set

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

    #get_conflict_free(framework)
    #is_arg_in_adm(framework, "a")
    # TODO check this thing until its fixed
    result = admissible_labeling(framework, set("3"), set(), set())
    print(result[0], result[1])

if __name__ == '__main__':
    main()