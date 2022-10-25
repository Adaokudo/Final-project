
from optparse import check_builtin

class Director:

    def start_game():
        guesses = []
        correct_guesses = 0
        question_num = 1

        for key in questions:
            print("--------------------")
            print(key)
            for i in options[ question_num-1 ]:
             print(i)
             print()
            guess = input("letter (A,B,or C): ")
            guess = guess.upper()
            guesses.append(guess)

            correct_guesses += check_answer(questions.get(key), guess)

            question_num += 1

        display_score(correct_guesses, guesses)

def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print('WRONG')
        return 0

#-------------------------#
def display_score(correct_guesses,guesses):
 print('-----------------')
 print('RESULTS')
 print("Answers:", end="")
 for i in questions:
    print(questions.get(i), end ="")
    print()

    print("guesses: ", end="")
    for i in guesses:
        print(i,end="")
        print()

    score = int((correct_guesses/len(questions))*100)
    print("your score is:"+str(score)+"%")
    
#----------------------#
def play_again():
    pass

questions = {
    "what is the meaning of WHO?: ": "A",
    " Is the earth round?: ":  "B",
    " who is the founder of facebook": "C"
}

options = [["A. word health org","B. world health org", "C. world health officials"],
           ["A. Yes", "B. No", "C. Sometimes"],
           ["A. Bill gate","B.mark zuckerburg", "C. Abraham hilton"]]

#new_game()#



