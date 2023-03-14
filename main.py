'''
  Name: Hannah Wilson
  James Hargest College
  Programming Internal for 1.7 ~ 4 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
print("|---Splatoon Quiz---|")
print("Welcome to the Splatoon Quiz!\nThis quiz will test your knowledge of the game Splatoon.\nTo play, use the letters 'a', 'b', or 'c' to select your answer to each question.\nGood luck!\n")


# define the questions and their answers
quiz = [    
    {   "question": "Which of these idol groups hosted Inkopolis News in Splatoon 1?",      
        "choices": ["A.Off The Hook", "B. Squid Sisters", "C. Deep Cut"],
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
    }
]

# Initialize the score
score = 0

# Display the questions and choices, and get user input
for i, q in enumerate(quiz): # Added an enumerate function to number the questions
    print(f"Question {i+1}: {q['question']}") # Used an f-string to make the output easier to read
    for choice in q['choices']:
        print(choice)
    user_answer = input("Enter your answer (A, B, or C): ").upper() # Used str.upper() method to make it so that the answer will be accepted if it is a A,B,C or a,b,c
    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {q['answer']}.") # Made it so that it will tell you the correct answer with an f-string

# Display the results
print(f"You got {score} out of {len(quiz)} questions correct.") # Updated this

