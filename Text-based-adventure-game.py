

def forestScene():
    print("You find yourself in a dense, mysterious forest.")
    print("Where would you like to go?")
    userInput = ""
    while userInput != "exit":
        print("Options: left/right/forward/exit")
        userInput = input().lower()
        if userInput == "left":
            print("You encounter a peaceful meadow and find fresh water.")
            print("You feel rejuvenated and rested.")
        elif userInput == "right":
            print("You stumble upon a hidden cave.")
            print("Do you want to explore it? (yes/no)")
            explore_cave = input().lower()
            if explore_cave == "yes":
                caveScene()
            elif explore_cave == "no":
                print("You decide not to enter the cave.")
            else:
                print("Please enter a valid option.")
        elif userInput == "forward":
            fight_result = encounterWildAnimal()
            if fight_result is True:
                print("While exploring, you discover a hidden path.")
                print("Do you want to explore it? (yes/no)")
                explore_path = input().lower()
                if explore_path == "yes":
                    print("You venture into the hidden path.")
                    print("After a while, you reach the end of the path and find a small clearing.")
                    print("Congratulations! You've reached the end of this adventure.")
                    print("Thank you for playing!")
                    break  # End the game
                elif explore_path == "no":
                    print("You decide not to explore the path.")
                    print("You continue exploring the forest.")
                    print("The forest seems endless and you keep wandering, hoping to find a way out.")
                    print("Unfortunately, you never find your way out and remain lost in the mysterious forest.")
                    print("Game over.")
                    exit(0)
                else:
                    print("Please enter a valid option.")
            elif fight_result is False:
                break  # End the game if player chooses to exit
            else:
                # Handle invalid choice or continue exploring after unsuccessful fight
                pass
        elif userInput == "exit":
            print("You decide to leave the forest.")
            break
        else:
            print("Please enter a valid option.")

def encounterWildAnimal():
    print("You encounter a wild animal.")
    print("What do you want to do?")
    print("1. Hide and wait for it to leave.")
    print("2. Fight the animal.")
    choice = input().lower()
    if choice == "1":
        print("You hide, but the animal notices you and attacks.")
        print("Game Over!")
        exit(0)
    elif choice == "2":
        print("You engage in a fight with the animal.")
        print("You manage to defeat the animal! Continue exploring")
        return True  # Indicates the successful fight
    elif choice == "exit":
        print("You decide to leave the forest.")
        return False  # Indicates the player chose to exit
    else:
        print("Invalid choice.")
    return None  # Indicates no decision was made yet

def caveScene():
    print("You enter the cave and find yourself surrounded by darkness.")
    print("What do you want to do?")
    print("Options: light a torch/look for an exit/return to the forest")
    userInput = input().lower()

    if userInput == "light a torch":
        print("With the torch lit, you see ancient inscriptions on the walls.")
        print("You discover a hidden passage and find your way out of the cave.")
        print("Congratulations! You've reached the end of this adventure.Thank you for playing!")
        exit(0)
    elif userInput == "look for an exit":
        print("You search for an exit but get lost in the labyrinthine caves.")
        print("Unfortunately, you can't find your way out. Game Over!")
        exit(0)
    elif userInput == "return to the forest":
        print("You decide to go back to the forest.")
    else:
        print("Invalid choice.")


def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in an unknown land.")
    print("Navigate through the forest to discover your path.")
    print("Let's begin the adventure.")
    
    forestScene()

if __name__ == "__main__":
    start_game()