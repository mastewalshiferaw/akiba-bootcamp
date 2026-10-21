quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. Rome", "D. Madrid"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "Which programming language is named after a British comedy troupe?",
        "options": ["A. Python", "B. Java", "C. Ruby", "D. C++"],
        "answer": "A"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    }
]



def display_question(q_data):
    print("\n" + q_data["question"])
    for option in q_data["options"]:
        print(option)


def validate_answer():
    valid_options = ["A", "B", "C", "D"]
    while True:
        user_input = input("Enter your choice (A, B, C, or D): ").strip().upper()
        if user_input in valid_options:
            return user_input
        print("Invalid choice! Please enter only A, B, C, or D.")



def check_answer(user_answer, correct_answer):
    return user_answer.upper() == correct_answer.upper()


def update_score(current_score, is_correct):
    if is_correct:
        return current_score + 1
    return current_score



def get_category(percentage):
    if percentage >= 80:
        return "Excellent!"
    elif percentage >= 60:
        return "Good Job!"
    elif percentage >= 40:
        return "Fair - Needs Practice"
    else:
        return "Needs Improvement"


def display_results(score, total_questions):
    incorrect = total_questions - score
    percentage = (score / total_questions) * 100
    category = get_category(percentage)

    print("\n" + "=" * 30)
    print("         QUIZ RESULTS")
    print("=" * 30)
    print("Total Questions   :", total_questions)
    print("Correct Answers   :", score)
    print("Incorrect Answers :", incorrect)
    print("Final Score       :", score, "/", total_questions)
    print("Percentage        :", round(percentage, 2), "%")
    print("Performance       :", category)
    print("=" * 30)



def run_quiz():
    score = 0
    total_questions = len(quiz_questions)

    for q in quiz_questions:
        display_question(q)
        user_choice = validate_answer()

        if check_answer(user_choice, q["answer"]):
            print("Correct!")
            score = update_score(score, True)
        else:
            print("Incorrect! The correct answer was " + q["answer"] + ".")
            score = update_score(score, False)

    display_results(score, total_questions)


#Play-again loop without restarting Python
def main():
    while True:
        run_quiz()
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again != "yes" and play_again != "y":
            print("\nThank you for playing! Goodbye.")
            break


# Start the program
main()