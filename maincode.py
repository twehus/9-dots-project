#greeting and welcome
greeting = [
    ("Welcome to the Cat Purrsonality Quiz!"),
    ("In this quiz, you'll receive points for the answers you choose."), 
    ("At the end, they'll be calculated and you'll discover your cat personality.\n"), 
    ("Have fun!"), 
    ("\n=^._.^= ∫\n\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
]
welcome = greeting[0]
print("*************************************\n" + welcome + "\n*************************************\n")
name = input("What's your name?")
print("\nHi " + name + "!\n")
welcome2 = greeting[1]
print(welcome2)
welcome3 = greeting[2]
print(welcome3)
welcome4 = greeting[3]
print(welcome4)
welcome5 = greeting[4]
print(welcome5)



input()



#first question
print("Your first question is:")
input()
#questions for users
questions = [
    ("How do you react when meeting someone new?\n"),
    ("What music genre would you most likely listen to?\n"),
    ("Choose one that you think would be cool to do.\n"),
    ("Pick a color.\n"),
    ("What's your favorite animal?\n")
    ("Do you consider yourself organized?\n")
    ("Are you more creative or logical?\n")
]
question1 = questions[0]
print(question1)

#answers for question 1
answers_for_q1 = [
("A) I want to be their friend immediately."),
("B) I make an effort to engage with them."),
("C) I'm pretty neutral about it."),
("D) I briefly introduce myself before finding someone I know to talk to."),
("E) I run awayyyyyyy.")
]
answer1 = answers_for_q1[0]
print(answer1)
answer2 = answers_for_q1[1]
print(answer2)
answer3 = answers_for_q1[2]
print(answer3)
answer4 = answers_for_q1[3]
print(answer4)
answer5 = answers_for_q1[4]
print(answer5)


def quiz_question1():
    answer = input("\nEnter your answer (A-E): \n").upper()  # Converts input to uppercase
    if answer in ['A', 'B', 'C', 'D', 'E']:
        points = {'A': 2, 'B': 1, 'C': 4, 'D': 3, 'E': 5}
        return points[answer]  
    else:
        print("Error. Please enter a letter from A to E.")
        return quiz_question1()

points1 = quiz_question1()
print("Points earned:", points1)

print("\nᐟᐠ-ꞈ-ᐟᐠ\n\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")



input()



#question for 2
print("Okay, " + name + " let's go to question 2:")
next = input()
question2 = questions[1]
print(question2)

#answers for question 2
answers_for_q2 = [
("A) Country"),
("B) Pop"),
("C) Rock/Alternative"),
("D) Classical"),
("E) R&B"),
("F) Rap/Hip-Hop")
]

answer1 = answers_for_q2[0]
print(answer1)
answer2 = answers_for_q2[1]
print(answer2)
answer3 = answers_for_q2[2]
print(answer3)
answer4 = answers_for_q2[3]
print(answer4)
answer5 = answers_for_q2[4]
print(answer5)
answer6 = answers_for_q2[5]
print(answer6)

def quiz_question2():
    answer = input("\nEnter your answer (A-F): \n").upper()  # Convert input to uppercase
    if answer in ['A', 'B', 'C', 'D', 'E', 'F']:
        points = {'A': 0, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 1}
        return points[answer]  
    else:
        print("Error. Please enter a letter from A to F.")
        return quiz_question2()

points2 = quiz_question2()
print("Points earned:", points2)

print("\n^.ᆽ.^= ∫\n\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")



input()



#question for 3
print("Now for question 3!")
next = input()
question3 = questions[2]
print(question3)

#answers for question 3
answers_for_q3 = [
("A) Explore an abandoned forest."),
("B) Be a part of a professional sports team."),
("C) Discover a new species."),
("D) Create an original art piece."),
("E) Swim with sharks.")
]

answer1 = answers_for_q3[0]
print(answer1)
answer2 = answers_for_q3[1]
print(answer2)
answer3 = answers_for_q3[2]
print(answer3)
answer4 = answers_for_q3[3]
print(answer4)
answer5 = answers_for_q3[4]
print(answer5)


def quiz_question3():
    answer = input("\nEnter your answer (A-E): \n").upper()
    if answer in ['A', 'B', 'C', 'D', 'E']:
        points = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1}
        return points[answer]  
    else:
        print("Error. Please enter a letter from A to E.")
        return quiz_question3()

points3 = quiz_question3()
print("Points earned:", points3)

print("\n(˃ᆺ˂)\n\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")



input()



#question for 4
print(name + ", you've made it to question 4!")
input()
question4 = questions[3]
print(question4)

#answers for question 4
answers_for_q4 = [
("A) Red"),
("B) Orange"),
("C) Yellow"),
("D) Green"),
("E) Blue"),
("F) Purple")
]

answer1 = answers_for_q4[0]
print(answer1)
answer2 = answers_for_q4[1]
print(answer2)
answer3 = answers_for_q4[2]
print(answer3)
answer4 = answers_for_q4[3]
print(answer4)
answer5 = answers_for_q4[4]
print(answer5)
answer6 = answers_for_q4[5]
print(answer6)

def quiz_question4():
    answer = input("\nEnter your answer (A-F): \n").upper()
    if answer in ['A', 'B', 'C', 'D', 'E', 'F']:
        points = {'A': 4, 'B': 2, 'C': 1, 'D': 0, 'E': 3, 'F': 5}
        return points[answer]  
    else:
        print("Error. Please enter a letter from A to F.")
        return quiz_question4()

points4 = quiz_question4()
print("Points earned:", points4)

print("\nᐟᐠ｡ꞈ｡ᐟᐠ\n\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")



input()



#question 5
print("Here's question 5:")
input()
question5 = questions[4]
print(question5)

#answers for question 5
answers_for_q5 = [
("A) Cat"),
("B) Dog (jk I meant to say cat)"),
("C) Bird (but really a cat)"),
("D) Hamster (aka cat!!)"),
("E) Snake (snakes are basically cats bc they hiss too)")
]

answer1 = answers_for_q5[0]
print(answer1)
answer2 = answers_for_q5[1]
print(answer2)
answer3 = answers_for_q5[2]
print(answer3)
answer4 = answers_for_q5[3]
print(answer4)
answer5 = answers_for_q5[4]
print(answer5)

def quiz_question5():
    answer = input("\nEnter your answer (A-E): \n").upper()
    if answer in ['A', 'B', 'C', 'D', 'E']:
        points = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
        return points[answer]  
    else:
        print("Error. Please enter a letter from A to E.")
        return quiz_question5()

points5 = quiz_question5()
print("Points earned:", points5)

print("\n(=^･ω･^=)\n\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")



input()



#question 6
print("Question #6:")
input()
question6 = questions[5]
print(question6)

#answers for question 6
answers_for_q6 = [
("A) I'm the most organized person I know."),
("B) Yes!"),
("C) At work but not at home."),
("D) Only when it really matters."),
("E) No lol.")
]

answer1 = answers_for_q6[0]
print(answer1)
answer2 = answers_for_q6[1]
print(answer2)
answer3 = answers_for_q6[2]
print(answer3)
answer4 = answers_for_q6[3]
print(answer4)
answer5 = answers_for_q6[4]
print(answer5)

def quiz_question6():
    answer = input("\nEnter your answer (A-E): \n").upper()
    if answer in ['A', 'B', 'C', 'D', 'E']:
        points = {'A': 5, 'B': 3, 'C': 2, 'D': 1, 'E': 4}
        return points[answer]  
    else:
        print("Error. Please enter a letter from A to E.")
        return quiz_question6()

points6 = quiz_question6()
print("Points earned:", points6)

print("\n(=◉ᆽ◉=)\n\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")



input()



#question 7
print(name + ", here's the final question!")
input()
question7 = questions[6]
print(question7)

#answers for question 7
answers_for_q7 = [
("A) Creative"),
("B) Mostly creative"),
("C) An equal mix of both"),
("D) Mostly logical"),
("E) Logical")
]

answer1 = answers_for_q7[0]
print(answer1)
answer2 = answers_for_q7[1]
print(answer2)
answer3 = answers_for_q7[2]
print(answer3)
answer4 = answers_for_q7[3]
print(answer4)
answer5 = answers_for_q7[4]
print(answer5)

def quiz_question7():
    answer = input("\nEnter your answer (A-E): \n").upper()
    if answer in ['A', 'B', 'C', 'D', 'E']:
        points = {'A': 4, 'B': 1, 'C': 2, 'D': 3, 'E': 5}
        return points[answer]  
    else:
        print("Error. Please enter a letter from A to E.")
        return quiz_question7()

points7 = quiz_question7()
print("Points earned:", points7)

print("\n(=ಠᆽಠ=)\n\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")



input()



print("* Nice job, " + name + "! *\nYou've completed all of the questions.\nNow it's time to calculate your points.")
input()
total_points = points1 + points2 + points3 + points4 + points5
print("\nYour results are:\n")
input()

orange_cat_result = ("You have an orange cat purrsonality.\n"
    "Orange cats are often associated with being outgoing and friendly.\n"
    "They can also be energetic, affectionate and adventurous.\n"
    "Some orange cats tend to be chaotic monsters with a single braincell.\n"
    "Fun fact: Gabby's orange cat is the latter :)\n"
    "Fun fact #2: Orange cats are mostly male due to a gene that's related to their fur color.")

black_cat_result = ("You have a black cat purrsonality.\n"
  "Black cats are known to be intelligent, elegant and mysterious.\n"
  "They are also independent, loyal and resourceful.\n"
  "Fun fact #1: Black cats are more resistant to diseases that other colored cats.\n"
  "Fun fact #2: Christianity is to blame for their associations with bad luck and 'evil'.\nAround the 13th century Christian churches saw witches as a direct competition with them,\nand over time there became a correlation between witches and black cats specifically\n(there's a lot of detailed information out there, and I used a History.com ariticle to find this particular fact).")


tabby_cat_result = ("You have a tabby cat purrsonality.\n"
  "Tabby cats are known to be outgoing, sociable and playful.\n"
  "They can also be adaptable and affectionate.\n"
  "Fun fact #1: The 'M' shape on most tabbys' head is said to be the marking of the Egyptian goddess Bastet.\n"
  "Fun fact #2: Most cats have the tabby coat pattern (around 60%).")


calico_cat_result = ("You have a calico cat purrsonality.\n"
  "Calicos are known to be strong-willed and sassy.\n"
  "They can also be quirky, vocal and unique.\n"
  "Fun fact #1: Calico cats are almost always female due to their coat coloration.\n"
  "Fun fact #2: Calicos are symbols of good luck in many cultures.")

tuxedo_cat_result = ("You have a tuxedo cat purrsonality.\n"
  "Tuxedo cats are known to be dapper and distinguished, with a bit of mischief.\n"
  "They can also be charismatic, playful and social.\n"
  "Some people say tuxedos are the huskies of cats.\n" 
  "Fun fact: Tuxedo cats earned their name because of their distinctive black and white markings.")

if total_points <= 5:
    print(orange_cat_result)
elif total_points <= 10:
    print(tabby_cat_result)
elif total_points <= 15:
    print(calico_cat_result)
elif total_points <= 19:
    print(tuxedo_cat_result)
elif total_points <= 25:
    print(black_cat_result)
else:
    print("Error. Total number cannot be greater than 25.")
    
input()

print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\nThanks for taking my quiz! Have a wonderful rest of your day! :)\nᶠᵉᵉᵈ ᵐᵉ /ᐠ-ⱉ-ᐟ\ﾉ\n")
print(
"\n   /\-/\    /\-/\    /\-/\    /\-/\    /\-/\    /\-/\    /\-/\    /\-/\ \n",
" (=^Y^=)  (=^Y^=)  (=^Y^=)  (=^Y^=)  (=^Y^=)  (=^Y^=)  (=^Y^=)  (=^Y^=) \n",
"  (>o<)    (>o<)    (>o<)    (>o<)    (>o<)    (>o<)    (>o<)    (>o<)")

