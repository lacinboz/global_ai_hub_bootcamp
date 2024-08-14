import random
def tas_kagit_makas_LACIN_BOZ():
    show_menu()

def show_menu():
  global user_name
  global game_number
  game_number = 0
  user_name = "Human Player (You)"
  print("**** Welcome To The Rock Paper Scissors Game! ****")
  print("*     Created by: Laçin Boz     *")
    #Oyun loopunu burdan başlat
  while True:
    print("\n***MENU***")
    print("1: Enter Player Name:")
    print("2: Show Rules:")
    print("3: Play a Game:")
    print("4: Exit The Game")

    user_option = input("Please select one option : ")
    if user_option == "1" :
      user_name = input("Please enter your name: ")
      print("Hello " + user_name)
      user_option_play_button= input("Are you ready to play? (yes/no) ")
      if user_option_play_button == "yes":
        #Call the function for playing game, play game bitince buraya geri döner
        play_game()
      elif user_option_play_button == "no" :
        print("We can wait all day, but I will wait you on the main menu!")
      else:
        print("Please enter a valid option")
        #Ana menüye dön

    elif user_option == "2":
      print("-----Rules-----")
      print("This is a hand game for two or more players.")
      print("After starting the game, write one of the 3 options(rock, paper, scissors) on the screen and see if you win.")
      print("Rock smashes scissors.")
      print("Paper covers rock.")
      print("Scissors cut paper.")
      print("The winner of the first two rounds wins the game!")
      print("Do not forget, if both players want to continue the game after the first game, the second game begins.")
      print("HAVE FUN! I am on your side!")

    elif user_option == "3":
      #Call the function for playing game
      play_game()
    elif user_option == "4":
      #exit from the loop ekle
      print("It was good to see you, bye!")
      break
    else:
      print("Please enter a valid option")

def play_game():
  actions = ["rock","paper","scissors"]
  global game_number
  round_number = 0
  player_score = 0
  computer_score = 0
  while True:
    print("---Game Number: " + str(game_number) + " ----")
    round_number = 0
    player_score = 0
    computer_score = 0
    while True:
      if player_score < 2 and computer_score < 2:
        print("---Round Number: " + str(round_number) + " ----")
      if player_score == 2 or computer_score == 2:
        break
      print("1. Rock")
      print("2. Paper")
      print("3. Scissors")
      user_input= input("Please enter a number for the action: (1,2,3) ")
      if user_input == "1":
        user_action = "rock"
      elif user_input == "2":
          user_action = "paper"
      elif user_input == "3":
          user_action = "scissors"
      else:
          print("Invalid input. Please enter 1, 2, or 3.")
          continue


      print("Now the computer is choosing an action. ")
      computer_action = actions[random.randint(0,2)]
      print("You have selected " +  user_action + " and the computer selected " + computer_action + ".")
      #Conditions:
      if user_action == computer_action:
        print("Tie! Both players chose the same action.")
      # 1,3 ü yener, 2,1 i yener, 3 de 2 yi yener
      elif (user_action == "rock" and computer_action == "scissors" ) or (user_action == "paper" and computer_action == "rock") or (user_action == "scissors" and computer_action == "paper"):
        print("Congratulations, " + user_name + "  won this round!")
        player_score += 1

      else:
        print("Computer won this round. You should make a better guess!")
        computer_score+= 1

      round_number+=1

    # The game now ended
    print("***Game Score:***")
    print(user_name + " Score : ", player_score, "Computer Score : ", computer_score)
    if player_score == 2:
      print("Congratulations, you won the game!")
      user_next_game_button = input("Do you want to play again, champion? (yes/no)")

    elif computer_score == 2:#
      print("Unfortunately, the computer won this time. Better luck next time!")
      user_next_game_button = input("Do you want to try again " + user_name + "? I bet you can win this time! (yes/no)")

    #If the variable is not yes or no it will enter the while loop and it will continue until we got the valid option
    while user_next_game_button not in ["yes","no"]:
      print("Please enter a valid option (yes or no).")
      user_next_game_button = input("Do you want to play again? (yes/no): ")
    # Select a random integer index for the action list, computer_next_game_button can be yes or no.
    number = random.randint(0,1)
    actions_comp = ["yes","no"]

    computer_next_game_button = actions_comp[number]

    if user_next_game_button == "yes" and computer_next_game_button == "yes":

      #computer_next_game_button =
      print("---Starting a new game---")
      game_number+= 1
    elif user_next_game_button == "yes" and computer_next_game_button == "no":
      print("Sorry, but the computer does not want to play.")
      break


      #Oyun tekrar başlasın ama dıştaki while loop kaliyor

    elif user_next_game_button == "no":
      print("See you then!")
      break
    #Looptan çıkmalı

tas_kagit_makas_LACIN_BOZ()