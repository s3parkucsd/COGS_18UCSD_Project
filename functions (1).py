quiz = {
"Q1: What pokemon type is turtwig? a. water b. electric c. grass d. air" : "c",
"Q2: How many fingers am I holding up? a. one b. two c. three d. four:" : "b",
"Q3: What is the most recent song ATEEZ has come out with? a. Turbulence b. Thanxx c. Fever d. Deja vu:" : "a",
"Q4: What item does a baby drop in Minecraft? a. nothing b. porkchop c. baby meat d. ashes" : "b", 
"Q5: Who am I? a. you from the future b. santa c. a shoe d. ~your~ baby gorl ( ͡° ͜ʖ ͡°)" : "d",
}


def quiz_instructions(): 
    
    """ 
    Function that introduces the quiz. 
    """

    print("Hello! My name is Frederick ԅ (≖‿≖ԅ) ! Want to see how smart you are? ")
    print("There are 5 questions to answer." + 
          "All questions accurately measures intelligence." +
          "Afterwards, you'll be judged based off how many you get correct!")
    input("Press any key to begin... If you have the heart for it... ")
    return True


def prediction_question(): 
    
    """ 
    Function asks question and stores input into prediction.
    """

    prediction = input("How well do you think you'll do? ")
    return prediction
    

def new_quiz(): 
    
    """ 
    Function purpose is to run all the functions in order. 
    """

    quiz_instructions()
    
    prediction = prediction_question()
    
    inputs = []
    score = 0
    
    #prints each question, asks for an input for each quesiton, stores in text.  
    for key in quiz:
        print(key)
        text = input("\t")
        
        #makes sure answers are lowercase so it won't mark capitalized correct answers wrong.
        #stores all text into inputs list.
        text = text.lower()
        inputs.append(text)
        
        #counts amount of questions right from checking_answer function into score.
        score += checking_answer(quiz.get(key), text)
    
    final_score(score, inputs, prediction)


def checking_answer(answer, text):
    
    """ 
    Function to check if the input answers are correct.
    
    Parameters: 
        answer: string 
        text: input string list
    Returns: 
        int 
    """

    #the returns will add up to total score in the end.
    if answer == text:
        print("Surprisingly correct.")
        return 1
    else:
        print("HAHA Wrong.")
        return 0

    
def final_score(score, inputs, prediction):
    
    """ 
    Function organizes all the information stored and presents them as a summary at the end of the quiz. 
    
    Parameters: 
        score: int
        inputs: string list
        prediction: string
        
    Returns: 
        string
    """

    #title of quiz summary.
    print("~~~~~~~~~~~~~~~~")
    print("Judgement day (ง’̀-‘́)ง:")
    print("~~~~~~~~~~~~~~~~")
    print("Answers: ", end = " ")
    
    #prints answers of the quiz here.    
    for choice in quiz:
        print(quiz.get(choice), end = " ")
    print()
    
    #prints inputs from the user here.    
    print("Inputs:", end = " ")
    for ans in inputs:
        print(ans, end = " ")
    print()
    
    #prints prediction input from user here.   
    print("Your Prediction: " + prediction)
    
    #calculates total score and gives message depending on score and total score count.    
    if score == 5: 
        print("Conclusion: You cheated (ಠ_ಠ).")
        print("Total Score: " + str(score))
    elif score >= 4: 
        print("Conclusion: You just got lucky ~(˘▾˘~).")
        print("Total Score: " + str(score))
    elif score >= 3: 
        print("Conclusion: You're a little dumb ╮ (. ❛ ᴗ ❛.) ╭.")
        print("Total Score: " + str(score))
    elif score >= 2: 
        print("Conclusion: This is kind of sad (づ￣ ³￣)づ.")
        print("Total Score: " + str(score))
    else: 
        print("Conclusion: You're dumb (☞ﾟ∀ﾟ)☞!")
        print("Total Score: " + str(score))
        

def take_quiz_again():

    """ 
    Function to have the option to take the quiz again. 
    """

    decision = input("Want to take quiz again to make yourself feel better? Reply yes or no: ")
    decision = decision.lower()

    if decision == "yes":
        return True
    else:
        return False

    
def quiz_time():
    new_quiz()
    
    """ 
    Function was added so it can run smoother. 
    Without this the function kept running in the wrong cell.
    """

    #end of the quiz.    
    while take_quiz_again():
        new_quiz()
    print("Bye. I won't miss you (ノ-_-)ノ~┻┻.")
       