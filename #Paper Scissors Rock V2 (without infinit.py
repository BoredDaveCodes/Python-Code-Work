#Paper Scissors Rock V2 (without infinity)
#Author: Dave Muton
import random
words = ["PAPER", "SCISSORS", "ROCK"]
def welcome_message():
    print("============================")
    print("    PAPER SCISSORS ROCK")
    print("============================")
    print("")
    print("welcome to Paper Scissors Rock!")
welcome_message()

players = int(input("Enter number of players (1 - 4): "))
print("You have chosen", players, "players.")
    

while True:
    if players == 1:
        print("What is your name?")
        player_name = input("Name: ")
        print("")
        print("You will be playing against Gazza (Garry the Seagull).") 
        num_of_rounds = int(input("Enter number of rounds to play (1 - 4): "))
        print("You have chosen to play", num_of_rounds, "round(s).")
        if num_of_rounds == 1:
            def game_round_1_player():
                print("Who would you like to play first?")
                print("1. ",player_name)
                print("2. Gazza (Garry the Seagull)")
                who_first = int(input("Who goes first? (1 or 2): "))
                if who_first == 1:
                    print(player_name, "will go first.")
                    print("Choose your weapon:")
                    print("- PAPER")
                    print("- SCISSORS")
                    print("- ROCK")
                    choose_weapon = input("Weapon: ")
                    print("Player chose", choose_weapon)
                    gazza_weapon = random.choice(words)
                    gazza_chosen_weapon1 = "PAPER"
                    gazza_chosen_weapon2 = "SCISSORS"
                    gazza_chosen_weapon3 = "ROCK"
                    
                    import time
                    print("Gazza is choosing his weapon...")
                    time.sleep(10)
                    print("Gazza has chosen his weapon!")
                    print("")
                    

                    if gazza_weapon == gazza_chosen_weapon1:
                        print("Gazza chose PAPER")
                        if choose_weapon == "PAPER":
                            print("It's a tie!")

                            with open("Scoreboard.txt", "w") as f:
                                f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                f.write("Winner: Tie\n")
                                f.close()
                            
                        elif choose_weapon == "SCISSORS":
                            print(player_name, "wins!")

                            with open("Scoreboard.txt", "w") as f:
                                f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                f.write("Winner: " + player_name + "\n")
                                f.close()
                            
                        elif choose_weapon == "ROCK":
                            print("Gazza wins!")

                            with open("Scoreboard.txt", "w") as f:
                                f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                f.write("Winner: Gazza\n")
                                f.close()
                            

                    if gazza_weapon == gazza_chosen_weapon2:
                        print("Gazza chose SCISSORS")
                        if choose_weapon == "SCISSORS":
                            print("It's a tie!")

                            with open("Scoreboard.txt", "w") as f:
                                f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                f.write("Winner: Tie\n")
                                f.close()
                            

                        if choose_weapon == "ROCK":
                            print(player_name, "wins!")

                            with open("Scoreboard.txt", "w") as f:
                                f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                f.write("Winner: " + player_name + "\n")
                                f.close()
                            

                        elif choose_weapon == "PAPER":
                                print("Gazza wins!")

                                with open("Scoreboard.txt", "w") as f:
                                    f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                    f.write("Winner: Gazza\n")
                                    f.close()
                                
                            
                    if gazza_weapon == gazza_chosen_weapon3:
                        print("Gazza chose ROCK")
                        if choose_weapon == "ROCK":
                            print("It's a tie!")
                            with open("Scoreboard.txt", "w") as f:
                                f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                f.write("Winner: Tie\n")
                                f.close()
                            

                        elif choose_weapon == "PAPER":
                            print(player_name, "wins!")

                            with open("Scoreboard.txt", "w") as f:
                                f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                f.write("Winner: " + player_name + "\n")
                                f.close()
                        elif choose_weapon == "SCISSORS":
                            print("Gazza wins!")

                            with open("Scoreboard.txt", "w") as f:
                                f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                f.write("Winner: Gazza\n")
                                f.close()
                            
                if who_first == 2:
                    print("Gazza will go first.")
                    gazza_weapon = random.choice(words)
                    gazza_chosen_weapon1 = "PAPER"
                    gazza_chosen_weapon2 = "SCISSORS"
                    gazza_chosen_weapon3 = "ROCK"
                    def gazza_thinking():
                        import time
                        print("Gazza is choosing his weapon...")
                        time.sleep(10)
                        print("Gazza has chosen his weapon!")
                        print("")
                    gazza_thinking()

                    if gazza_weapon == gazza_chosen_weapon1:
                        print("Gazza chose PAPER")
                        print("Choose your weapon:")
                        print("- PAPER")
                        print("- SCISSORS")
                        print("- ROCK")
                        choose_weapon = input("Weapon: ")
                        print("Player chose", choose_weapon)

                        if choose_weapon == "PAPER":
                            print("It's a tie!")

                            with open("Scoreboard.txt", "w") as f:
                                f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                f.write("Winner: Tie\n")
                                f.close()
                            
                        elif choose_weapon == "SCISSORS":
                            print(player_name, "wins!")

                            with open("Scoreboard.txt", "w") as f:
                                f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                f.write("Winner: " + player_name + "\n")
                                f.close()
                            
                        elif choose_weapon == "ROCK":
                            print("Gazza wins!")

                            with open("Scoreboard.txt", "w") as f:
                                f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                f.write("Winner: Gazza\n")
                                f.close()
                             

                    if gazza_weapon == gazza_chosen_weapon2:
                        print("Gazza chose SCISSORS")
                        print("Choose your weapon:")
                        print("- PAPER")
                        print("- SCISSORS")
                        print("- ROCK")
                        choose_weapon = input("Weapon: ")
                        print("Player chose", choose_weapon)

                        if choose_weapon == "SCISSORS":
                            print("It's a tie!")

                            with open("Scoreboard.txt", "w") as f:
                                f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                f.write("Winner: Tie\n")
                                f.close()
                            

                        if choose_weapon == "ROCK":
                            print(player_name, "wins!")

                            with open("Scoreboard.txt", "w") as f:
                                f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                f.write("Winner: " + player_name + "\n")
                                f.close()
                            

                        elif choose_weapon == "PAPER":
                                print("Gazza wins!")

                                with open("Scoreboard.txt", "w") as f:
                                    f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                    f.write("Winner: Gazza\n")
                                    f.close()
                                
                            
                    if gazza_weapon == gazza_chosen_weapon3:
                        print("Gazza chose ROCK")
                        print("Choose your weapon:")
                        print("- PAPER")
                        print("- SCISSORS")
                        print("- ROCK")
                        choose_weapon = input("Weapon: ")
                        print("Player chose", choose_weapon)

                        if choose_weapon == "ROCK":
                            print("It's a tie!")

                            with open("Scoreboard.txt", "w") as f:
                                f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                f.write("Winner: Tie\n")
                                f.close()
                            

                        elif choose_weapon == "PAPER":
                            print(player_name, "wins!")

                            with open("Scoreboard.txt", "w") as f:
                                f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                f.write("Winner: " + player_name + "\n")
                                f.close()
                        elif choose_weapon == "SCISSORS":
                            print("Gazza wins!")

                            with open("Scoreboard.txt", "w") as f:
                                f.write(player_name + " vs Gazza (Garry the Seagull)\n")
                                f.write("Winner: Gazza\n")
                                f.close()
                            
                        game_round_1_player()

                        
        if num_of_rounds == 2:

            print("")
            print("Round 1:")
            game_round_1_player()
            print("Round 2:")
            game_round_1_player()

        if num_of_rounds == 3:
            print("")
            print("Round 1:")
            game_round_1_player()
            print("Round 2:")
            game_round_1_player()
            print("Round 3:")
            game_round_1_player()

        if num_of_rounds == 4:
        
            print("")
            print("Round 1:")
            game_round_1_player()
            print("Round 2:")
            game_round_1_player()
            print("Round 3:")
            game_round_1_player()
            print("Round 4:")
            game_round_1_player()  

    if players == 2:
        player1_name = input("Enter name of Player 1: ")
        player2_name = input("Enter name of Player 2: ")
        num_of_rounds = int(input("Enter number of rounds to play (1 - 4): "))
        print("You have chosen to play", num_of_rounds, "rounds.")
        if num_of_rounds == 1:
            def game_round_2_players():
                print("Who would like to play first?")
                print("1.",player1_name)
                print("2. ",player2_name)
                who_first = int(input("Who goes first? (1 or 2): "))
                if who_first == 1:
                    print(player1_name, "will go first.")
                    print(player1_name, "choose your weapon:")
                    print("- PAPER")
                    print("- SCISSORS")
                    print("- ROCK")
                    player1_weapon = input("Weapon: ")
                    print(player1_name, "chose", player1_weapon)
                    print(player2_name, "choose your weapon:")
                    print("- PAPER")
                    print("- SCISSORS")
                    print("- ROCK")
                    player2_weapon = input("Weapon: ")
                    print(player2_name, "chose", player2_weapon)
                    if player1_weapon == player2_weapon:
                        print("It's a tie!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + " vs " + player2_name + "\n")
                            f.write("Winner: Tie\n")
                            f.close()
                    elif (player1_weapon == "PAPER" and player2_weapon == "ROCK") or (player1_weapon == "SCISSORS" and player2_weapon == "PAPER") or (player1_weapon == "ROCK" and player2_weapon == "SCISSORS"):
                        print(player1_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + " vs " + player2_name + "\n")
                            f.write("Winner: " + player1_name + "\n")
                            f.close()
                    else:
                        print(player2_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + " vs " + player2_name + "\n")
                            f.write("Winner: " + player2_name + "\n")
                            f.close()
                        game_round_2_players()
                if who_first == 2:
                    print(player2_name, "will go first.")
                    print(player2_name, "choose your weapon:")
                    print("- PAPER")
                    print("- SCISSORS")
                    print("- ROCK")
                    player2_weapon = input("Weapon: ")
                    print(player2_name, "chose", player2_weapon)
                    print(player1_name, "choose your weapon:")
                    print("- PAPER")
                    print("- SCISSORS")
                    print("- ROCK")
                    player1_weapon = input("Weapon: ")
                    print(player1_name, "chose", player1_weapon)
                    if player1_weapon == player2_weapon:
                        print("It's a tie!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + " vs " + player2_name + "\n")
                            f.write("Winner: Tie\n")
                            f.close()
                             

                    elif (player1_weapon == "PAPER" and player2_weapon == "ROCK") or (player1_weapon == "SCISSORS" and player2_weapon == "PAPER") or (player1_weapon == "ROCK" and player2_weapon == "SCISSORS"):
                        print(player1_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + " vs " + player2_name + "\n")
                            f.write("Winner: " + player1_name + "\n")
                            f.close()
                            
                    else:
                        print(player2_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + " vs " + player2_name + "\n")
                            f.write("Winner: " + player2_name + "\n")
                            f.close()
                            
                        game_round_2_players()

        if num_of_rounds == 2:
            print("")
            print("Round 1:")
            game_round_2_players()
            print("Round 2:")
            game_round_2_players()

        if num_of_rounds == 3:
            print("")
            print("Round 1:")
            game_round_2_players()
            print("Round 2:")
            game_round_2_players()
            print("Round 3:")
            game_round_2_players()

        if num_of_rounds == 4:
            print("")
            print("Round 1:")
            game_round_2_players()
            print("Round 2:")
            game_round_2_players()
            print("Round 3:")
            game_round_2_players()
            print("Round 4:")
            game_round_2_players()

    if players == 3:
        player1_name = input("Enter name of Player 1: ")
        player2_name = input("Enter name of Player 2: ")
        player3_name = input("Enter name of Player 3: ")
        num_of_rounds = int(input("Enter number of rounds to play (1 - 4): "))
        print("You have chosen to play", num_of_rounds, "rounds.")
        if num_of_rounds == 1:
            print("Round 1:")
            def game_round_3_players():
                print("Who is playing first?")
                print("1.",player1_name)
                print("2. ",player2_name)
                print("3. ",player3_name)
                who_first = int(input("Who goes first? (1, 2 or 3): "))
                if who_first == 1:
                    print(player1_name, "will go first.")
                    print("Weapons:")
                    print("- PAPER")
                    print("- SCISSORS")
                    print("- ROCK")
                    player1_weapon = input(player1_weapon, "Weapon: ")
                    player2_weapon = input(player2_weapon, "Weapon: ")
                    player3_weapon = input(player3_weapon, "Weapon: ")

                    if player1_weapon == player2_weapon == player3_weapon:
                        print("It's a tie!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + " and " + player3_name + "\n")
                            f.write("Winner: Tie\n")
                            f.close()
                            

                    elif (player1_weapon == "PAPER" and player2_weapon == "ROCK" and player3_weapon == "ROCK") or (player1_weapon == "SCISSORS" and player2_weapon == "PAPER" and player3_weapon == "PAPER") or (player1_weapon == "ROCK" and player2_weapon == "SCISSORS" and player3_weapon == "SCISSORS"):
                        print(player1_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + " and " + player3_name + "\n")
                            f.write("Winner: " + player1_name + "\n")
                            f.close()
                            

                    elif (player2_weapon == "PAPER" and player1_weapon == "ROCK" and player3_weapon == "ROCK") or (player2_weapon == "SCISSORS" and player1_weapon == "PAPER" and player3_weapon == "PAPER") or (player2_weapon == "ROCK" and player1_weapon == "SCISSORS" and player3_weapon == "SCISSORS"):
                        print(player2_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + " and " + player3_name + "\n")
                            f.write("Winner: " + player2_name + "\n")
                            f.close()
                            

                    else:
                        print(player3_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + " and " + player3_name + "\n")
                            f.write("Winner: " + player3_name + "\n")
                            f.close()
                        

                if who_first == 2:
                    print(player2_name, "will go first.")
                    print("Weapons:")
                    print("- PAPER")
                    print("- SCISSORS")
                    print("- ROCK")
                    player1_weapon = input(player2_weapon, "Weapon: ")
                    player2_weapon = input(player1_weapon, "Weapon: ")
                    player3_weapon = input(player3_weapon, "Weapon: ")

                    if player1_weapon == player2_weapon == player3_weapon:
                        print("It's a tie!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + " and " + player3_name + "\n")
                            f.write("Winner: Tie\n")
                            f.close()
                            

                    elif (player1_weapon == "PAPER" and player2_weapon == "ROCK" and player3_weapon == "ROCK") or (player1_weapon == "SCISSORS" and player2_weapon == "PAPER" and player3_weapon == "PAPER") or (player1_weapon == "ROCK" and player2_weapon == "SCISSORS" and player3_weapon == "SCISSORS"):
                        print(player1_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:  
                            f.write(player1_name + ", " + player2_name + " and " + player3_name + "\n")
                            f.write("Winner: " + player1_name + "\n")
                            f.close()
                            

                    elif (player2_weapon == "PAPER" and player1_weapon == "ROCK" and player3_weapon == "ROCK") or (player2_weapon == "SCISSORS" and player1_weapon == "PAPER" and player3_weapon == "PAPER") or (player2_weapon == "ROCK" and player1_weapon == "SCISSORS" and player3_weapon == "SCISSORS"):
                        print(player2_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + " and " + player3_name + "\n")
                            f.write("Winner: " + player2_name + "\n")
                            f.close()
                            

                    else:
                        print(player3_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + " and " + player3_name + "\n")
                            f.write("Winner: " + player3_name + "\n")
                            f.close()
                            

                if who_first == 3:
                    print(player3_name, "will go first.")
                    print("Weapons:")
                    print("- PAPER")
                    print("- SCISSORS")
                    print("- ROCK")
                    player1_weapon = input(player3_weapon, "Weapon: ")
                    player2_weapon = input(player2_weapon, "Weapon: ")
                    player3_weapon = input(player1_weapon, "Weapon: ")

                    if player1_weapon == player2_weapon == player3_weapon:
                        print("It's a tie!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + " and " + player3_name + "\n")
                            f.write("Winner: Tie\n")
                            f.close()
                            

                    elif (player1_weapon == "PAPER" and player2_weapon == "ROCK" and player3_weapon == "ROCK") or (player1_weapon == "SCISSORS" and player2_weapon == "PAPER" and player3_weapon == "PAPER") or (player1_weapon == "ROCK" and player2_weapon == "SCISSORS" and player3_weapon == "SCISSORS"):
                        print(player1_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + " and " + player3_name + "\n")
                            f.write("Winner: " + player1_name + "\n")
                            f.close()
                            

                    elif (player2_weapon == "PAPER" and player1_weapon == "ROCK" and player3_weapon == "ROCK") or (player2_weapon == "SCISSORS" and player1_weapon == "PAPER" and player3_weapon == "PAPER") or (player2_weapon == "ROCK" and player1_weapon == "SCISSORS" and player3_weapon == "SCISSORS"):
                        print(player2_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + " and " + player3_name + "\n")
                            f.write("Winner: " + player2_name + "\n")
                            f.close()
                            

                    else:
                        print(player3_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + " and " + player3_name + "\n")
                            f.write("Winner: " + player3_name + "\n")
                            f.close()
                        
            game_round_3_players()
        if num_of_rounds == 2:
            print("")
            print("Round 1:")
            game_round_3_players()
            print("Round 2:")
            game_round_3_players()
       
        if num_of_rounds == 3:
            print("")
            print("Round 1:")
            game_round_3_players()
            print("Round 2:")
            game_round_3_players()
            print("Round 3:")
            game_round_3_players()
       
        if num_of_rounds == 4:
            print("")
            print("Round 1:")
            game_round_3_players()
            print("Round 2:")
            game_round_3_players()
            print("Round 3:")
            game_round_3_players()
            print("Round 4:")
            game_round_3_players()
            
    if players == 4:
        player1_name = input("Enter name of Player 1: ")
        player2_name = input("Enter name of Player 2: ")
        player3_name = input("Enter name of Player 3: ")
        player4_name = input("Enter name of Player 4: ")
        num_of_rounds = int(input("Enter number of rounds to play (1 - 4): "))
        print("You have chosen to play", num_of_rounds, "rounds.")
        if num_of_rounds == 1:
            print("Round 1:")
            def game_round_4_players():
                print("Who is playing first?")
                print("1.",player1_name)
                print("2. ",player2_name)
                print("3. ",player3_name)
                print("4. ",player4_name)
                who_first = int(input("Who goes first? (1, 2, 3 or 4): "))
                if who_first == 1:
                    print(player1_name, "will go first.")
                    print("Weapons:")
                    print("- PAPER")
                    print("- SCISSORS")
                    print("- ROCK")
                    player1_weapon = input(player1_weapon, "Weapon: ")
                    player2_weapon = input(player2_weapon, "Weapon: ")
                    player3_weapon = input(player3_weapon, "Weapon: ")
                    player4_weapon = input(player4_weapon, "Weapon: ")
                    if player1_weapon == player2_weapon == player3_weapon == player4_weapon:
                        print("It's a tie!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: Tie\n")
                            f.close()
                            

                    elif (player1_weapon == "PAPER" and player2_weapon == "ROCK" and player3_weapon == "ROCK" and player4_weapon == "ROCK") or (player1_weapon == "SCISSORS" and player2_weapon == "PAPER" and player3_weapon == "PAPER" and player4_weapon == "PAPER") or (player1_weapon == "ROCK" and player2_weapon == "SCISSORS" and player3_weapon == "SCISSORS" and player4_weapon == "SCISSORS"):
                        print(player1_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: " + player1_name + "\n")
                            f.close()
                            

                    elif (player2_weapon == "PAPER" and player1_weapon == "ROCK" and player3_weapon == "ROCK" and player4_weapon == "ROCK") or (player2_weapon == "SCISSORS" and player1_weapon == "PAPER" and player3_weapon == "PAPER" and player4_weapon == "PAPER") or (player2_weapon == "ROCK" and player1_weapon == "SCISSORS" and player3_weapon == "SCISSORS" and player4_weapon == "SCISSORS"):
                        print(player2_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: " + player2_name + "\n")
                            f.close()
                            

                    elif (player3_weapon == "PAPER" and player1_weapon == "ROCK" and player2_weapon == "ROCK" and player4_weapon == "ROCK") or (player3_weapon == "SCISSORS" and player1_weapon == "PAPER" and player2_weapon == "PAPER" and player4_weapon == "PAPER") or (player3_weapon == "ROCK" and player1_weapon == "SCISSORS" and player2_weapon == "SCISSORS" and player4_weapon == "SCISSORS"):
                        print(player3_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: " + player3_name + "\n")
                            f.close()
                            
                    else:
                        print(player4_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: " + player4_name + "\n")
                            f.close()
                            

                if who_first == 2:
                    print(player2_name, "will go first.")
                    print("Weapons:")
                    print("- PAPER")
                    print("- SCISSORS")
                    print("- ROCK")
                    player1_weapon = input(player2_weapon, "Weapon: ")
                    player2_weapon = input(player1_weapon, "Weapon: ")
                    player3_weapon = input(player3_weapon, "Weapon: ")
                    player4_weapon = input(player4_weapon, "Weapon: ")
                    if player1_weapon == player2_weapon == player3_weapon == player4_weapon:
                        print("It's a tie!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: Tie\n")
                            f.close()
                            

                    elif (player1_weapon == "PAPER" and player2_weapon == "ROCK" and player3_weapon == "ROCK" and player4_weapon == "ROCK") or (player1_weapon == "SCISSORS" and player2_weapon == "PAPER" and player3_weapon == "PAPER" and player4_weapon == "PAPER") or (player1_weapon == "ROCK" and player2_weapon == "SCISSORS" and player3_weapon == "SCISSORS" and player4_weapon == "SCISSORS"):
                        print(player1_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:  
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: " + player1_name + "\n")
                            f.close()
                         

                    elif (player2_weapon == "PAPER" and player1_weapon == "ROCK" and player3_weapon == "ROCK" and player4_weapon == "ROCK") or (player2_weapon == "SCISSORS" and player1_weapon == "PAPER" and player3_weapon == "PAPER" and player4_weapon == "PAPER") or (player2_weapon == "ROCK" and player1_weapon == "SCISSORS" and player3_weapon == "SCISSORS" and player4_weapon == "SCISSORS"):
                        print(player2_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: " + player2_name + "\n")
                            f.close()
                            

                    elif (player3_weapon == "PAPER" and player1_weapon == "ROCK" and player2_weapon == "ROCK" and player4_weapon == "ROCK") or (player3_weapon == "SCISSORS" and player1_weapon == "PAPER" and player2_weapon == "PAPER" and player4_weapon == "PAPER") or (player3_weapon == "ROCK" and player1_weapon == "SCISSORS" and player2_weapon == "SCISSORS" and player4_weapon == "SCISSORS"):
                        print(player3_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: " + player3_name + "\n")
                            f.close()
                            

                    else:
                        print(player4_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: " + player4_name + "\n")
                            f.close()
                            

                if who_first == 3:
                    print(player3_name, "will go first.")
                    print("Weapons:")
                    print("- PAPER")
                    print("- SCISSORS")
                    print("- ROCK")
                    player1_weapon = input(player3_weapon, "Weapon: ")
                    player2_weapon = input(player1_weapon, "Weapon: ")
                    player3_weapon = input(player2_weapon, "Weapon: ")
                    player4_weapon = input(player4_weapon, "Weapon: ")
                    if player1_weapon == player2_weapon == player3_weapon == player4_weapon:
                        print("It's a tie!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: Tie\n")
                            f.close()
                          

                    elif (player1_weapon == "PAPER" and player2_weapon == "ROCK" and player3_weapon == "ROCK" and player4_weapon == "ROCK") or (player1_weapon == "SCISSORS" and player2_weapon == "PAPER" and player3_weapon == "PAPER" and player4_weapon == "PAPER") or (player1_weapon == "ROCK" and player2_weapon == "SCISSORS" and player3_weapon == "SCISSORS" and player4_weapon == "SCISSORS"):
                        print(player1_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: " + player1_name + "\n")
                            f.close()
                            
                    elif (player2_weapon == "PAPER" and player1_weapon == "ROCK" and player3_weapon == "ROCK" and player4_weapon == "ROCK") or (player2_weapon == "SCISSORS" and player1_weapon == "PAPER" and player3_weapon == "PAPER" and player4_weapon == "PAPER") or (player2_weapon == "ROCK" and player1_weapon == "SCISSORS" and player3_weapon == "SCISSORS" and player4_weapon == "SCISSORS"):
                        print(player2_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: " + player2_name + "\n")
                            f.close()
                            

                    elif (player3_weapon == "PAPER" and player1_weapon == "ROCK" and player2_weapon == "ROCK" and player4_weapon == "ROCK") or (player3_weapon == "SCISSORS" and player1_weapon == "PAPER" and player2_weapon == "PAPER" and player4_weapon == "PAPER") or (player3_weapon == "ROCK" and player1_weapon == "SCISSORS" and player2_weapon == "SCISSORS" and player4_weapon == "SCISSORS"):
                        print(player3_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: " + player3_name + "\n")
                            f.close()
                            
                    else:
                        print(player4_name, "wins!")
                if who_first == 4:
                    print(player4_name, "will go first.")
                    print("Weapons:")
                    print("- PAPER")
                    print("- SCISSORS")
                    print("- ROCK")
                    player1_weapon = input(player1_weapon, "Weapon: ")
                    player2_weapon = input(player2_weapon, "Weapon: ")
                    player3_weapon = input(player3_weapon, "Weapon: ")
                    player4_weapon = input(player4_weapon, "Weapon: ")
                    if player1_weapon == player2_weapon == player3_weapon == player4_weapon:
                        print("It's a tie!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: Tie\n")
                            f.close()
                             
                    elif (player1_weapon == "PAPER" and player2_weapon == "ROCK" and player3_weapon == "ROCK" and player4_weapon == "ROCK") or (player1_weapon == "SCISSORS" and player2_weapon == "PAPER" and player3_weapon == "PAPER" and player4_weapon == "PAPER") or (player1_weapon == "ROCK" and player2_weapon == "SCISSORS" and player3_weapon == "SCISSORS" and player4_weapon == "SCISSORS"):
                        print(player1_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: " + player1_name + "\n")
                            f.close()
                        
                    elif (player2_weapon == "PAPER" and player1_weapon == "ROCK" and player3_weapon == "ROCK" and player4_weapon == "ROCK") or (player2_weapon == "SCISSORS" and player1_weapon == "PAPER" and player3_weapon == "PAPER" and player4_weapon == "PAPER") or (player2_weapon == "ROCK" and player1_weapon == "SCISSORS" and player3_weapon == "SCISSORS" and player4_weapon == "SCISSORS"):
                        print(player2_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: " + player2_name + "\n")
                            f.close()
                        
                    elif (player3_weapon == "PAPER" and player1_weapon == "ROCK" and player2_weapon == "ROCK" and player4_weapon == "ROCK") or (player3_weapon == "SCISSORS" and player1_weapon == "PAPER" and player2_weapon == "PAPER" and player4_weapon == "PAPER") or (player3_weapon == "ROCK" and player1_weapon == "SCISSORS" and player2_weapon == "SCISSORS" and player4_weapon == "SCISSORS"):
                        print(player3_name, "wins!")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: " + player3_name + "\n")
                            f.close()
                        
                    else:
                        print(player4_name, "wins")

                        with open("Scoreboard.txt", "w") as f:
                            f.write(player1_name + ", " + player2_name + ", " + player3_name + " and " + player4_name + "\n")
                            f.write("Winner: " + player4_name + "\n")
                            f.close()

                        
            game_round_4_players()
        if num_of_rounds == 2:
            print("")
            print("Round 1:")
            game_round_4_players()
            print("Round 2:")
            game_round_4_players()
                
        if num_of_rounds == 3:
                print("")
                print("Round 1:")
                game_round_4_players()
                print("Round 2:")
                game_round_4_players()
                print("Round 3:")
                game_round_4_players()
        if num_of_rounds == 4:
                print("")
                print("Round 1:")
                game_round_4_players()
                print("Round 2:")
                game_round_4_players()
                print("Round 3:")
                game_round_4_players()
                print("Round 4:")
                game_round_4_players()
    if players < 1 or players > 4:
        print("Invalid number of players. Please enter a number between 1 and 4.")
        players = int(input("Enter number of players (1 - 4): "))
        continue