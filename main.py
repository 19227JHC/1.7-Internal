'''
  Name: Hannah Wilson
  James Hargest College
  Programming Internal for 1.7 ~ 4 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''

# -------------------------------------------------------------- Option to Start ------------------------------------
print("  ____        _       _                                  _    ")
print(" / ___| _ __ | | __ _| |_ ___   ___  _ __     __ _ _   _(_)____  ")
print(" \___ \| '_ \| |/ _` | __/ _ \ / _ \| '_ \   / _` | | | | |_  /  ")
print("  ___) | |_) | | (_| | || (_) | (_) | | | | | (_| | |_| | |/ /   ")
print(" |____/| .__/|_|\__,_|\__\___/ \___/|_| |_|  \__, |\__,_|_/___|  ")
print("       |_|                                      |_|              ")


print("\033[0;92m                              ██████              ")
print("                            ██▒▒▒▒▒▒██            ")
print("                          ██▒▒▒▒▒▒▒▒▒▒██          ")
print("                        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██        ")
print("                      ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██      ")
print("                    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    ")
print("                  ██▒▒▒▒▒▒▒▒████▒▒████▒▒▒▒▒▒▒▒██  ")
print("                  ██▒▒▒▒▒▒██  ████  ████▒▒▒▒▒▒██  ")
print("                ██▒▒▒▒▒▒██  ████  ████  ██▒▒▒▒▒▒██")
print("                ██▒▒▒▒▒▒██              ██▒▒▒▒▒▒██")
print("                  ████▒▒▒▒██    ██    ██▒▒▒▒████  ")
print("                      ██▒▒▒▒████▒▒████▒▒▒▒██      ")
print("                      ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██      ")
print("                    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    ")
print("                    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    ")
print("                    ██▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒▒██    ")
print("                      ██████  ██████  ██████      \033[0m")

print("\nWelcome to the Splatoon Quiz!\nThis quiz will test your knowledge of the game Splatoon.")

# Instructions for beginning
print("\nIf you are ready to start the quiz, input Y then press enter to confirm your answer")
print("\nIf you are not ready to start the quiz, input N then press enter to confirm your answer")

# Define function to ask user if they are ready to start the quiz
def start_quiz():

    # Asks the user if they are ready to start the quiz 
    ready = input("\nAre you ready to start the quiz? (Y/N) ").lower()  # Use str.lower() method to make it so the program accepts both Y and y
  
    # If the user is ready to take the quiz and inputs Y, it will display the instructions and start the quiz 
    if ready == "y":
        print("\nAwesome!\nTo take the quiz, input the letters 'A', 'B', or 'C' to select your answer to each question. Once chosen answer has been selected/inputted, press enter to confirm it.\nGood luck!\n")
        return True

    # If the user is not ready to take the quiz and inputs N, it will exit the program
    elif ready == "n":
        print("\nNo problem, come back when you're ready!")
        return False

    # If the user input is not a valid input, it will print this message until they input a valid one
    else:
        print("\033[0;31mInvalid input, please enter 'Y' or 'N'.\033[0m")
        return start_quiz()  # Call the function again if the user inputs an invalid input


# Call the start_quiz function
if start_quiz():
    pass


# ----------------------------------------------------- Quiz Questions\Setup ----------------------------------------


# Define the questions of the quiz as a list of dictionaries, where each dictionary represents a question and its choices for answers
    quiz = [
    {   "question": "Which of these idol groups hosted Inkopolis News in Splatoon 1?",      
        "choices": ["A.Off The Hook", "B.Squid Sisters", "C.Deep Cut"],
        "answer": "B"
    },
    {
        "question": "Where does the Octo Expansion take place?",
        "choices": ["A.Deepsea Metro", "B.Octo Canyon", "C.Alterna"],
        "answer": "A"
    },
    {
        "question": "What is sanitized ink made of?",
        "choices": ["A.Sanitizer products", "B.Human remnants", "C.Blended up octarians"],
        "answer": "C"
    },
    {
        "question": "What type of Salmonid is Little Buddy?",
        "choices": ["A.Cohock", "B.Chum.", "C.Smallfry"],
        "answer": "C"
    },
    {
        "question": "Which of the following is not a playable mode in Splatoon 3?",
        "choices": ["A.Inkstrike", "B.Splat Zones", "C.Rainmaker"],
        "answer": "A"
    },
    {
        "question": "Who is 'The Ursine Anomaly #03'?",
        "choices": ["A.lil Judd", "B.Mr. Grizz", "C.Mr. Coco"],
        "answer": "B"
    },
    {
        "question":"What is the name of the AI in Alterna?",
        "choices": ["A.C.Q. Cumber", "B.Commander Tartar", "C.O.R.C.A."],
        "answer": "C"
    },
    {
        "question": "Who is the leader of the Octarian army?",
        "choices": ["A.DJ Octavio", "B.Captain Cuttlefish", "C.Inner Agent 3"],
        "answer": "A"
    },
    {
        "question": "The Fuzzy Ooze is made up of liquid crystals, Mr. Grizz's fur, and ___",
        "choices": ["A.Salmonids", "B.Golden Eggs", "C.Human remnant"],
        "answer": "B"
    },
    {
        "question": "How many Denizens of the Deep are there in the Deepsea Metro?",
        "choices": ["A.5", "B.13", "C.9"],
        "answer": "C"
    },
    {
        "question": "What was the name of the final splatfest in Splatoon 2?",
        "choices": ["A.Splatocalypse", "B.Splatfest Memories", "C.Superfest"],
        "answer": "A"
    },
    {
        "question": "What was the name of the final splatfest in Splatoon 2?",
        "choices": ["A.Octo Swim", "B.Salmon Run", "C.Squid Run"],
        "answer": "B"
    } 
    ]

 # Import the random module to shuffle the quiz questions
    import random
  
  # Command to shuffle the questions
    random.shuffle(quiz)
  
  # Initialize the score to 0
    score = 0
  
# ------------------------------------------------------- Quiz Output Code ------------------------------------------
  
          # Display the questions and choices, and get user input
      
    for i, q in enumerate(quiz):  # Loop through the shuffled quiz list with the enumerate function to number the questions
          print(f"Question {i+1}: {q['question']}")  # Display the question number and question text using an f-string
            
          for choice in q['choices']: 
              print(choice)  # Display the answer choices for the current question
          
          # Use a while loop to make sure the user inputs a valid answer
          while True:
              user_answer = input("\nEnter your answer (A, B, or C): ").upper()  # Used .upper() method to make it so that the answer will be accepted if it is a A,B,C or a,b,c
              if user_answer in ["A", "B", "C"]:
                  break
                    
              # If the user input is not a valid input, it will print this message until they enter a valid one
              else:
                  print("\n\033[0;31mInvalid input, please enter A, B, or C.\033[0m")
          
          if user_answer == q["answer"]:
              print("\033[0;32m\nCorrect!\n\033[0m")
              score += 1
                
          else:
              print(f"\033[0;31m\nIncorrect. The correct answer is {q['answer']}.\n\033[0m")  # Made it so that it will tell you the correct answer with an f-string
          
                
      # Define the custom messages based on the final score
    if score == 0:
          message = "\nOpps! You didn't get any questions right. Better luck next time."  # This message displays if the user got no questions correct
            
    elif score <= 5:
          message = f"\nYou got {score} out of {len(quiz)} questions correct. You can do better!"  # This message displays if the user got 5 or less correct
            
    elif score <= 9:
          message = f"\nYou got {score} out of {len(quiz)} questions correct. Good job!"  # this message displays if the user got 9 or less correct
            
    else:
          message = f"\nCongratulations! You got {score} out of {len(quiz)} questions correct. You are a Spaltoon master!"  # This message displays if the user got 9 or above questions correct
          
      # Displays the messages above depending on the user's score at the end of the quiz
    print(message)


  
    print("\nThanks taking the quiz!")
    print("\n\033[0;93m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⠛⠛⣻⠿⠛⠩⠍⢒⣒⣛⣂⣀⠐⠺⠭⢛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠅⣀⣥⣴⣶⠆⢀⣠⣶⣶⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⠁⠈⠝⠛⡿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣛⠭⠍⢀⣥⣶⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⢲⣦⣤⣀⣩⣉⣈⣉⣩⣭⣍⣁⡊⠩⢻⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⠴⠀⢈⣥⣤⣴⣿⣿⣿⣿⣿⡿⠃⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠇⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⢛⠀⣠⣴⣾⣿⣿⣿⡿⠿⡟⠛⠛⠛⠁⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⢁⣬⣭⣤⣤⣤⣄⠈⠙⠻⣿⣿⣿⣿⡏⢀⠇⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⣾⣿⣿⣿⠟⠋⣑⣿⣿⣶⣶⣶⣷⣶⣶⣤⡀⡉⠛⢿⣿⣿⣿⣿⣿⣿⠟⢋⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡈⠻⣿⠟⢀⠞⣼⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⢱⠀⣼⣿⡿⠛⣡⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⡹⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⡀⢾⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⡟⡇⠰⠟⠋⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣙⠈⠋⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣦⡀⠀⠮⡙⢿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⡿⡋⠕⢁⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣶⣄⡀⠐⠙⠿⣿⣿⣿")
    print("⣿⣿⡿⠫⠂⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⢈⢿⣿")
    print("⣿⡟⡁⢡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⡩⠝⠻⣿⣇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⢸⢸⣿")
    print("⡟⡜⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠘⣴⣿⣦⣄⠉⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⡏⣿")
    print("⢰⡇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢂⣿⣿⣿⣿⣷⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢀⢧⣿")
    print("⣸⣷⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⠀⢈⣍⣉⣵⣤⣤⣤⣤⣤⣬⡙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⢀⣴⣿⣿")
    print("⢸⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢫⡾⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣬⡙⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠁⢀⢀⣰⣿⣿⣿⣿")
    print("⡘⡟⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣱⣿⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⠀⠈⢉⣉⡉⣉⣁⣀⠀⢄⣠⣶⣿⣿⣿⣿⣿⣿")
    print("⣧⠡⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣼⣿⡿⠃⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣷⢠⢻⣿⣿⣿⣿⣾⣆⢸⢻⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣧⡁⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠘⢛⠛⠇⠰⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⣉⣥⣶⣶⠶⠈⢿⣿⣿⣿⠀⠎⣿⣿⣿⣿⣿⣿⢸⢸⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣧⢁⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠐⠻⠿⢿⠃⠰⠆⢈⣿⣿⣿⣿⣿⣿⣿⣿⣄⣉⣉⣉⣩⣴⣶⣷⣿⣿⣿⣿⣇⠀⠿⣿⣿⣿⢻⡏⡸⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⡟⡄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢧⣿⣿⡿⠇⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠈⠻⣿⡀⢰⣿⣿⠋⠘⠁⠥⠛⠿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣟⠄⢰⣿⣿⣿⣿⣟⢿⣿⣿⣿⣿⣾⡟⣻⣬⢲⡶⠺⠀⠈⠛⠻⢿⣿⣿⣿⣿⣿⣝⢻⣿⠟⠁⠀⢀⠄⠀⠂⠉⠁⠀⠀⣀⣈⣇⠈⣿⠋⣼⣿⡁⠶⣦⣌⡀⠹⠻⣿⣿⣿")
    print("⣿⣿⡿⠻⠀⣾⣿⣿⣿⣿⣿⣮⣿⣿⣿⣿⢫⣖⢝⢁⢴⠂⠀⠀⠀⠀⠀⠀⠙⠛⠛⠉⠉⢉⣉⠉⠀⠀⠈⣀⣤⣤⣤⣤⡰⠷⢲⣌⢻⣿⠈⢃⣼⣟⡻⢿⣶⣤⣙⠋⣀⠣⠛⢿⣿")
    print("⣿⣿⣿⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⢇⣦⡦⠄⢀⣤⣤⣤⣤⣤⡠⣀⣶⣿⣥⣤⣿⣿⣿⣶⣾⣿⣟⣿⣭⡥⣖⣻⣭⣵⣿⣞⣿⣷⢺⣿⣿⣿⣿⣦⣝⢻⣿⣿⣷⣄⠀⡹")
    print("⣿⣿⡏⠔⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣼⠗⢁⣤⣬⣗⣒⡂⠼⢿⡧⣿⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣯⣯⣿⣿⣿⣼⣿⠻⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⠇⡘")
    print("⡿⡫⢂⣴⣷⡈⢿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠊⢀⣴⣷⢶⣶⣯⣭⣝⣻⣿⣿⣿⣿⡁⠒⠺⣟⣓⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⣠⣾")
    print("⡇⠇⢾⣿⣿⣷⣄⠙⠿⠿⠿⠛⢋⣉⣤⡰⣆⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⡿⠀⣰⣿⣿⣿⣿⣿⠿⠟⠉⢀⣠⣶⣿⣿⣿")
    print("⣿⣦⣀⠌⡙⠻⢿⣿⣦⣶⣶⣶⣿⣿⣿⣷⡌⠎⢿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠟⣛⣉⣩⠭⠤⠶⠶⣶⡶⠂⠀⢀⣿⣿⣿⣿⣿⣿⣿⠃⢀⠿⠿⠟⡋⠉⣐⣠⣵⣾⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣾⣥⣐⡨⠉⢙⡛⠻⠿⠿⢿⣿⣷⡄⠈⢻⣿⣿⣿⣿⣿⣇⠀⠀⠈⠉⢋⣀⣀⣀⣤⣶⡄⠀⠀⣠⣾⣿⣿⣿⣿⣿⠟⠀⠤⣄⣂⣤⣵⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣮⣭⣥⣤⣐⣀⠤⠤⠄⠀⠹⢿⣿⣿⣿⣿⣷⣦⣄⣀⠙⠋⠛⠿⠛⢋⣁⣴⣿⣿⣿⣿⣿⡿⢋⠁⠔⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⡀⢀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⡨⠀⠠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣕⣀⠠⢈⡙⡛⠿⠿⡿⠿⠟⠛⠛⠛⢋⣉⡁⢀⣀⠀⠀⠀⠈⠒⠒⠉⠩⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣛⠻⠏⠉⠐⠊⢁⣁⣤⣤⠰⠀⣶⣾⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣷⣶⣦⣤⠄⡀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡱⠀⢤⣤⣤⣶⣶⣿⣿⣿⣿⣿⣿⠀⠆⢹⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⡟⢀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡁⠘⢿⣿⣿⣿⣿⢿⣿⣿⣿⣿⡆⠘⠀⣿⣿⣿⣿⣿⣧⢸⠿⣿⣿⣿⣿⣿⡿⠁⢇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡡⡀⠙⠟⠋⣡⣤⣍⡙⠻⢿⣷⠀⡀⣿⣿⡿⠟⣋⣭⣶⣦⣄⠉⠻⢿⡟⠁⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷⠰⠀⢠⣾⣿⣿⣿⣿⣷⣦⣅⡀⠳⢉⣡⣴⣾⣿⣿⡿⣿⣿⣿⠦⠄⡀⠢⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠫⠁⣡⣶⣶⣦⣬⣉⡫⠉⠙⠛⠿⠿⠟⠀⠈⠻⠿⠛⢋⣩⡤⠈⢉⣠⣶⣿⣿⣲⢄⠀⠀⠝⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠫⠈⣠⣾⣿⣷⣶⠍⣿⣿⣷⣦⡀⠻⣶⣶⡄⣤⠐⣶⣾⣿⣿⠏⢀⣼⣿⣿⠸⠛⣿⣿⣷⡝⣦⡀⠑⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⠐⢠⡾⣿⣿⣿⣿⣿⣷⣦⣄⠙⢿⣿⡀⠹⣿⡇⢸⠀⣿⣿⣿⡏⠀⣾⡿⠋⣠⣶⣿⣿⣿⣿⣿⣼⣿⡆⠈⠨⠻⣿⠿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⡫⢈⡐⠁⢀⣴⣿⣿⣿⣿⣿⣏⡩⣟⢻⣿⣷⡈⢻⠟⢀⣿⡇⢸⠀⣿⣿⣿⡇⠀⣏⢠⣾⣿⠋⢁⣼⣿⣿⣿⣿⣿⣿⡂⢀⠐⠒⠀⠜⢻⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⢫⠏⣰⣿⡇⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡄⠹⣿⣇⠀⠠⣿⣿⡇⢸⡄⣿⣿⣿⣿⠄⠈⠸⡟⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⡿⢃⡤⠂⣠⣄⢡⠻⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⠏⠊⣼⣿⣿⣄⠑⡈⢻⣿⣿⣿⡿⡛⢿⣿⣿⣿⠂⠘⣡⣶⣶⣤⣌⣑⠈⠳⠘⢛⣡⣤⣶⣶⣆⡐⢸⣿⣿⠟⢋⠁⠉⢿⠟⣉⠔⣁⣤⣾⣿⣿⡆⠃⢹⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⡸⢠⡉⢿⣿⣿⣷⣌⠀⠙⠛⠉⢠⣶⣶⣿⣿⠟⢁⣾⣿⠿⢿⣿⣿⣿⣦⠀⢾⣿⣿⣿⣿⠿⣿⣷⣄⠙⠿⠿⠿⠋⠀⡠⠊⣡⣾⣿⣿⣿⣿⠟⣠⢱⣸⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⡿⡁⢁⣿⣷⣈⠻⣿⣿⣿⣷⣄⠈⠲⣤⡉⠉⠉⠁⣀⣉⣭⣶⣶⣶⣦⣭⣭⠁⣠⠈⣭⣭⣴⣶⣶⣶⣬⣍⠑⠒⠒⠀⠠⢊⣴⣾⣿⣿⣿⣿⠟⣡⣾⣿⣆⠣⢻⣿⣿\033[0m")
      
    print("\nDepending on screen size, you may need to scroll up for your score :)")
        
    
# -------------------------------------------------------------- End ------------------------------------------------
  