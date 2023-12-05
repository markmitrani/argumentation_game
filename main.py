import json
import random
import time

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
    init_arg = input("Please type the number of the initial argument the computer should claim: ")

    # necessary structures:
    ## args_player: list of player's arguments
    ## args_computer: list of computer's arguments
    args_player = []
    args_computer = [init_arg]

    attackers_init = find_attackers(framework, init_arg)

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
        args_player.append(player_choice)

        computer_choices = find_attackers(framework, player_choice)
        computer_real_choices = []
        # this for loop eliminates the choices already made by the player
        for x in computer_choices:
            if x not in args_player:
                computer_real_choices.append(x)
        if not computer_real_choices:
            print("The computer can make no more moves, you win!")
            win = "player"
            break

        print("Computer! Your turn!\n")
        time.sleep(1)
        print("Is this the end for you, player? You will find out soon!\n")
        time.sleep(1)



        computer_choice = random.choice(computer_real_choices)
        print("Computer: I have chosen "+computer_choice+".")
        args_computer.append(computer_choice)

        attackers_comp = find_attackers(framework, computer_choice)

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