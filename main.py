import json
import random
import time

import admissible
import conflict_free
import graph
import preferred


def print_arguments(framework):
    for k, v in framework["Arguments"].items():
        print(k+": "+v)

def print_arguments_with_id(framework, list):
    for k, v in framework["Arguments"].items():
        if k in list:
            print(k+": "+v)

def find_attackers(framework, arg_id):
    attackers = []
    for attack in framework["Attack Relations"]:
        if attack[1] == arg_id:
            attackers.append(attack[0])
    return attackers


def get_preferred_extension(framework, init_arg):
    framework_alt = graph.convert_data_structure(framework)
    cf_sets = conflict_free.conflict_free_sets_containing_arg(framework_alt)
    cf_sets_with_arg = (item for item in cf_sets if init_arg in item)
    admissible_sets_with_arg = admissible.find_admissible_sets(cf_sets_with_arg, framework_alt)
    preferred_sets_with_arg = preferred.find_preferred_sets(admissible_sets_with_arg)
    return preferred_sets_with_arg


def find_attackers_of_set(framework, args_computer):
    result = set()
    for item in args_computer:
        for attacker in find_attackers(framework, item):
            result.add(attacker)
    return result

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

    print("Displaying arguments in the framework:")
    print_arguments(framework)
    # get input argument
    round_cnt = 0
    print("ROUND",round_cnt)
    init_arg = input("Please type the number of the initial argument the computer should claim: ")

    # Check if Preferred Extension exists
    prefset = get_preferred_extension(framework, init_arg)
    print(prefset)

    if len(prefset)>0:
        defendable = True

    # necessary structures:
    ## args_player: list of player's arguments
    ## args_computer: list of computer's arguments
    args_player = set()
    args_computer = set(init_arg)

    attackers_init = find_attackers_of_set(framework, args_computer)

    attackers_comp = attackers_init
    game_continues = True
    while(game_continues):
        if not attackers_comp:
            print("You have no choices, player! You suck!")
            win = "computer"
            break
        print("Player, here are your choices: ")
        print_arguments_with_id(framework, attackers_comp)
        player_choice = input("Please type the number of your chosen argument: ")
        if player_choice in args_player:
            print("You used this argument before, idiot!")
            win = "computer"
            break
        if player_choice in args_computer:
            print("The computer used this argument before.")
            print("Idiot computer loses")
            win = "player"
            break
        args_player.add(player_choice)

        attackers_player = find_attackers(framework, player_choice)

        # TODO the brain of the computer
        computer_choices = []
        # this for loop eliminates the choices already made by the player
        for x in attackers_player:
            if x not in args_player:
                computer_choices.append(x)

        computer_preferred_choices = []
        # TODO if any argument in real choices is in pref. extension, pick that
        for arg in computer_choices:
            if any(arg in s for s in prefset):
                computer_preferred_choices.append(arg)


        # !!! if the computer doesn't have any choices not already made by the player, they lose
        if not computer_choices:
            print("The computer can make no more moves, you win!")
            win = "player"
            break

        round_cnt += 1
        print("ROUND", round_cnt)
        print("Computer! Your turn!\n")
        time.sleep(1)
        print("Is this the end for you, player? You will find out soon!\n")
        time.sleep(1)

        if computer_preferred_choices:
            computer_choice = computer_preferred_choices[0]
        else:
            computer_choice = random.choice(computer_choices)

        print("Computer: I have chosen "+computer_choice+".")
        args_computer.add(computer_choice)

        attackers_comp = find_attackers_of_set(framework, args_computer).difference(args_player)

    if win == "player":
        print("Congratulations! You won! You're amazing!!!")
    if win == "computer":
        print("Congratulations! You lost! You're terrible!!!")

    # round loop: check if player can make attacks.
    ## after player has made their move, check if their argument was used by computer before
    ### if so, computer wins
    ### if not, computer continues
    ## check if computer can make an attack.
    ## check if their argument was used by player before
    ### if so, player wins
    ### if not, player continues (next loop)
    ## before start of next loop:

if __name__ == '__main__':
    main()