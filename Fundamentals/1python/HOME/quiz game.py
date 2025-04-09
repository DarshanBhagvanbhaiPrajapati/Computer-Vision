
def new_game():
    guesses = []
    correct_guesses = 0
    question_num =1

    for key in Questions:
        print("----------------------------")
        print(key)
        for i in Options[question_num-1]:
            print(i)
        
        guess = input("enter any option: ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(Questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses,guesses)

def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT ANSWER")
        return 1
    else:
        print("WRONG ANSWER")
        return 0
def display_score(correct_guesses,guesses):
    print("----------------------------")
    print("RESULTS")
    print("----------------------------")

    print("Answers: ",end = "")
    for i in Questions:
        print(Questions.get(i),end=" ")
    print()
    print("Guesses: ",end = "")
    for i in guesses:
        print(i,end=" ")
    print()

    score = int((correct_guesses/len(Questions) * 100))
    print("YOUR SCORE IS : "+str(score)+ "%")
def play_again():
    
    response = input("Do you want to play again?: (Yes or No):")
    response = response.upper()

    if response == "Yes":
        return True
    else:
        return False

Questions = {
    "from which college you are?: " :"A",
    "from which branch?:" : "B",
    "how much sgpa you scored in your first sem?: " : "C",
    "fail in how many subject?: " : "D",
}
Options = [["A. PDEU","B. NIRMA","C. DAIICT","D. IIT"],
           ["A.CSE","B.ICT","C.CHEMICAL","D.MECHAN"],
           ["A. >=7","B. >=8","C. >=9","D. =10"],
           ["A. 2","B. 3","C.1","D. 0"]]

new_game()

while play_again():
    new_game()

print("BYY")