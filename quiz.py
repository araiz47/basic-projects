#Random quiz project Ver 1

questions = ["What is my age ?",
             "What is my name ?",
             "Where do i live ?",
             "What is my country ?"]

options = ["A. 17 B. 18 C. 19 D. 21",
           "A. Ara B. Buk C. Arriz D. Ara-iz",
           "A. Lhr B. RWP C. BWP D. ISB",
           "A. US B. PAK C. UK D. Italy"]

answers = ["D","A","C", "B"]
score = 0

for i in range(len(questions)):
    print(questions[i])
    print(options[i])

    guess = input("Enter your answers: ")

    if guess == answers[i]:
        print("Correct !!")
        score +=1
    else:
        print("Wrong !!")

print(f"Final Score: {score}")
