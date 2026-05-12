#basic flashcard learning Ver 1
flashcard = {}

while True:
    print("1. Add Flashcard")
    print("2. Study")
    print("3. Quit")
    choice = input("Enter a choice: ")

    if choice == "1":
        question = input("Enter a question: ")
        answer = input("Enter a answer: ")
        flashcard[question] = answer

    elif choice == "2":
        for question,answer in flashcard.items():
            print("\n Question: ",question)
            input("Press Enter to answer.....")
            print("Answer: ",answer)

    elif choice == "3":
        break            