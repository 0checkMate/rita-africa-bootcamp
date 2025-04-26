# 
# Defining the questions library
quiz_questions = {
    'What is the output of print(2 ** 3)?': {
        'options': ['A. 6', 'B. 8', 'C. 9', 'D. 5'],
        'answer': 'B'
    },
    'Which keyword is used to define a function in Python?': {
        'options': ['A. function', 'B. define', 'C. def', 'D. func'],
        'answer': 'C'
    },
    'Which of these is a Python list?': {
        'options': ['A. (1, 2, 3)', 'B. [1, 2, 3]', 'C. {1, 2, 3}', 'D. <1, 2, 3>'],
        'answer': 'B'
    },
    "What is the result of: len('Python')?": {
        'options': ['A. 5', 'B. 6', 'C. 7', 'D. 8'],
        'answer': 'B'
    },
    "What does the 'input()' function do?": {
        'options': ['A. Prints a value', 'B. Adds two numbers', 'C. Gets user input', 'D. Creates a loop'],
        'answer': 'C'
    },
    'Which data type is immutable in Python?': {
        'options': ['A. List', 'B. Dictionary', 'C. Set', 'D. Tuple'],
        'answer': 'D'
    },
    'What is the correct way to start a for loop in Python?': {
        'options': ['A. for i to range(5)', 'B. foreach i in range(5)', 'C. for i in range(5):', 'D. loop i in 5'],
        'answer': 'C'
    },
    'How do you insert a comment in Python?': {
        'options': ['A. // comment', 'B. # comment', 'C. <!-- comment -->', 'D. /* comment */'],
        'answer': 'B'
    },
    'Which operator is used for equality comparison?': {
        'options': ['A. =', 'B. !=', 'C. ==', 'D. =>'],
        'answer': 'C'
    },
    'What is the correct file extension for Python files?': {
        'options': ['A. .pt', 'B. .py', 'C. .pyt', 'D. .python'],
        'answer': 'B'
    }
}

# function to add questions
def add_question():
    print('\n Add a new question to the quiz')
    
    question = input('Enter the question: ')
    option_a = input('Option A: ')
    option_b = input('Option B: ')
    option_c = input('Option C: ')
    option_d = input('Option D: ')
    correct = input('Enter correct answer (A/B/C/D): ').strip().upper()

    quiz_questions[question] = {
        'options': [f'A. {option_a}', f'B. {option_b}', f'C. {option_c}', f'D. {option_d}'],
        'answer': correct
    }

    print('Question added successfully!')

# function to take quiz and grade it
def take_quiz():
    print('\n Starting the Quiz...')
    score = 0
    total = len(quiz_questions)

    for question, data in quiz_questions.items():
        print('\n' + question)
        for option in data['options']:
            print(option)
        
        answer = input('Your answer (A/B/C/D): ').strip().upper()

        if answer == data['answer']:
            print('Correct!')
            score += 1
        else:
            print(f'Incorrect! The correct answer was {data["answer"]}')
    
    print(f'\n Quiz complete! Your score: {score}/{total}')
    return score

# function to save it into a txt file
def save_score(name, score):
    with open('quiz_scores.txt', 'a') as file:
        file.write(f'{name}: {score}/{len(quiz_questions)}\n')
    
    print('Your score has been saved to quiz_scores.txt')

# main function to run the script
def main():
    print('Welcome to the Python Quiz Maker!\n')

    role = input('Are you a student or admin? ').strip().lower()

    if role == 'admin':
        add_q = input('Do you want to add a question to the quiz? (yes/no): ').strip().lower()

        while add_q == 'yes':
            add_question()
            add_q = input('Add another question? (yes/no): ').strip().lower()

    name = input('\nEnter your name: ')
    score = take_quiz()
    save_score(name, score)






