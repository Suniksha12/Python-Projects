import tkinter as tk
from tkinter import messagebox
import random

# List of quiz questions and answers
quiz_data = [
    {"question": "What is the capital of India?", "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"], "answer": "Delhi"},
    {"question": "Who wrote the Indian National Anthem?", "options": ["Rabindranath Tagore", "Bankim Chandra Chatterjee", "Sarojini Naidu", "Mahatma Gandhi"], "answer": "Rabindranath Tagore"},
    {"question": "Which is the largest planet in our Solar System?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Jupiter"},
    {"question": "Who was the first Prime Minister of India?", "options": ["Sardar Patel", "Jawaharlal Nehru", "Lal Bahadur Shastri", "Rajendra Prasad"], "answer": "Jawaharlal Nehru"},
    {"question": "Which is the longest river in India?", "options": ["Ganges", "Brahmaputra", "Yamuna", "Godavari"], "answer": "Ganges"},
    {"question": "Who discovered gravity?", "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla"], "answer": "Isaac Newton"},
    {"question": "Which Indian scientist is known as the Missile Man of India?", "options": ["C.V. Raman", "A.P.J. Abdul Kalam", "Vikram Sarabhai", "Homi Bhabha"], "answer": "A.P.J. Abdul Kalam"},
    {"question": "What is the currency of Japan?", "options": ["Yen", "Won", "Ringgit", "Peso"], "answer": "Yen"},
    {"question": "Which Indian festival is known as the Festival of Lights?", "options": ["Holi", "Navratri", "Diwali", "Eid"], "answer": "Diwali"},
    {"question": "Which is the smallest state in India?", "options": ["Goa", "Sikkim", "Tripura", "Manipur"], "answer": "Goa"}
]

# Shuffle questions
random.shuffle(quiz_data)

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("500x400")

        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar()
        self.options_buttons = []

        for i in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.options_var, value="", font=("Arial", 12), indicatoron=0, width=20, height=2, bg="lightgray")
            btn.pack(pady=5)
            self.options_buttons.append(btn)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=("Arial", 12), bg="green", fg="white")
        self.submit_button.pack(pady=20)

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
        self.score_label.pack()

        self.restart_button = tk.Button(root, text="Restart Game", command=self.restart_game, font=("Arial", 12), bg="blue", fg="white")
        self.restart_button.pack(pady=10)
        self.restart_button.config(state=tk.DISABLED)

        self.load_question()

    def load_question(self):
        if self.current_question < len(quiz_data):
            q_data = quiz_data[self.current_question]
            self.question_label.config(text=q_data["question"])
            self.options_var.set("")
            
            for i, option in enumerate(q_data["options"]):
                self.options_buttons[i].config(text=option, value=option)

        else:
            self.end_quiz()

    def check_answer(self):
        selected_answer = self.options_var.get()
        if not selected_answer:
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        correct_answer = quiz_data[self.current_question]["answer"]
        if selected_answer == correct_answer:
            self.score += 1
        
        self.current_question += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.load_question()

    def end_quiz(self):
        messagebox.showinfo("Quiz Completed!", f"Your final score is {self.score}/{len(quiz_data)}")
        self.submit_button.config(state=tk.DISABLED)
        self.restart_button.config(state=tk.NORMAL)

    def restart_game(self):
        self.score = 0
        self.current_question = 0
        self.submit_button.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.DISABLED)
        self.score_label.config(text="Score: 0")
        random.shuffle(quiz_data)
        self.load_question()

# Run the game
root = tk.Tk()
quiz = QuizGame(root)
root.mainloop()

