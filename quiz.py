questions = ("What race is goku?", "Who is his grandfather?", "How many saiyans existed in the beginning of dbz?", "Who is my favourite producer?",("What is my favourite genre in music?"),)

options = (
('A. Human ',"B.Saiyan",'C. Namekian','D.buu'),
('A.Gohan',"B. Roshi",'C.Chiaotzu','D.Krillin'),
('A.5',"B.3",'C.8','D.1'),
('A.MF doom',"B.Nujabes",'C.Drake','D.The weeekend'),
('A.Yacht ROck',"B.Hip Hop",'C.Rap','D.Jazz'))



answers = ('B','A','A','B','A')
guesses=[]
score = 0
question_num = 0 

for question in questions:
    print("__________________________")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{answers[question_num]} is the correct answer")
        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
    question_num += 1
print("__________________________")
print("RESULTS")
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print("\nGuesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
score = int(score / len(questions) * 100)
print(f"\nYour score is: {score}%")
