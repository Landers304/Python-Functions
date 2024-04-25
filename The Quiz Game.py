#Task 1:


questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the chemical symbol for water?",
        "answer": "H2O"
    }
]

print(questions)




#Task 2: 


def quiz_user(questions):
    score = 0
    for question in questions:
        user_answer = input(question["question"] + " ")
        if user_answer.lower() == question["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question["answer"])
    return score




#Task 3:


def score_quiz(score, total_questions):
    percentage = (score / total_questions) * 100
    if percentage >= 70:
        print("Awesome! You scored", score, "out of", total_questions, "(", percentage, "%). You passed!")
    else:
        print("You scored", score, "out of", total_questions, "(", percentage, "%). Come back with more knowledge.")

total_questions = len(questions)
user_score = quiz_user(questions)
score_quiz(user_score, total_questions)
