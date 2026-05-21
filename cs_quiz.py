import time

# --- All quiz questions ---
# Each question is a dictionary with: question, options, answer, explanation
questions = [
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Core Processing Unit"],
        "answer": "B",
        "explanation": "CPU = Central Processing Unit, the brain of the computer."
    },
    {
        "question": "Which data structure works on LIFO principle?",
        "options": ["A. Queue", "B. Array", "C. Stack", "D. Linked List"],
        "answer": "C",
        "explanation": "Stack = Last In First Out (like a stack of plates)."
    },
    {
        "question": "What is the time complexity of Binary Search?",
        "options": ["A. O(n)", "B. O(n²)", "C. O(log n)", "D. O(1)"],
        "answer": "C",
        "explanation": "Binary search halves the list each time, so it's O(log n)."
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. function", "D. def"],
        "answer": "D",
        "explanation": "In Python, 'def' is used to define a function."
    },
    {
        "question": "What does HTML stand for?",
        "options": ["A. Hyper Text Markup Language", "B. High Text Machine Language", "C. Hyper Transfer Markup Logic", "D. None of these"],
        "answer": "A",
        "explanation": "HTML = HyperText Markup Language, used to build web pages."
    },
    {
        "question": "Which of these is NOT a Python data type?",
        "options": ["A. List", "B. Tuple", "C. Vector", "D. Dictionary"],
        "answer": "C",
        "explanation": "Vector is not a built-in Python data type. It exists in C++ STL."
    },
    {
        "question": "What does RAM stand for?",
        "options": ["A. Read Access Memory", "B. Random Access Memory", "C. Run After Memory", "D. Read And Memory"],
        "answer": "B",
        "explanation": "RAM = Random Access Memory, temporary storage while programs run."
    },
    {
        "question": "Which sorting algorithm has the best average-case time complexity?",
        "options": ["A. Bubble Sort", "B. Selection Sort", "C. Merge Sort", "D. Insertion Sort"],
        "answer": "C",
        "explanation": "Merge Sort has O(n log n) average-case, better than O(n²) sorts."
    },
    {
        "question": "In Python, which symbol is used for single-line comments?",
        "options": ["A. //", "B. --", "C. #", "D. /* */"],
        "answer": "C",
        "explanation": "Python uses # for single-line comments."
    },
    {
        "question": "Which layer of the OSI model handles IP addressing?",
        "options": ["A. Physical Layer", "B. Data Link Layer", "C. Network Layer", "D. Transport Layer"],
        "answer": "C",
        "explanation": "The Network Layer (Layer 3) handles IP addressing and routing."
    }
]

# --- Game Logic ---

def run_quiz():
    print("=" * 45)
    print("       Welcome to the CS Quiz Game!")
    print("       Test your Computer Science knowledge")
    print("=" * 45)
    
    name = input("\nEnter your name: ")
    print(f"\nHello {name}! Let's begin. You have 10 questions.\n")
    time.sleep(1)

    score = 0
    wrong_questions = []

    for i, q in enumerate(questions):
        print(f"Q{i+1}. {q['question']}")
        for option in q["options"]:
            print(f"   {option}")
        
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")
            print(f"   💡 {q['explanation']}\n")
            wrong_questions.append(q["question"])
        
        time.sleep(0.5)

    # --- Final Score ---
    print("=" * 45)
    print(f"       Quiz Over, {name}!")
    print(f"       Your Score: {score} / {len(questions)}")
    
    percentage = (score / len(questions)) * 100
    
    if percentage == 100:
        print("       🏆 Perfect Score! You're a CS genius!")
    elif percentage >= 70:
        print("       🎉 Great job! Keep it up!")
    elif percentage >= 50:
        print("       👍 Not bad! A little more practice needed.")
    else:
        print("       📚 Keep studying! You'll get there.")

    if wrong_questions:
        print("\n   Review these topics:")
        for q in wrong_questions:
            print(f"   - {q}")

    print("=" * 45)

# --- Start the game ---
run_quiz()
