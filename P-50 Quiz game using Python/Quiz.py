import tkinter as tk
from tkinter import messagebox
import random

# Questions and answers data
questions = [
    {"question": "What is the capital of India?", "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"], "answer": "Delhi"},
    {"question": "Who wrote the Indian national anthem?", "options": ["Rabindranath Tagore", "Bankim Chandra", "Sarojini Naidu", "Mahatma Gandhi"], "answer": "Rabindranath Tagore"},
    {"question": "What is the national animal of India?", "options": ["Tiger", "Elephant", "Lion", "Leopard"], "answer": "Tiger"},
    {"question": "Which is the largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Jupiter"},
    {"question": "What is the chemical symbol for water?", "options": ["O2", "H2O", "CO2", "NaCl"], "answer": "H2O"},
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("General Knowledge Quiz")
        self.root.geometry("500x400")
        
        self.score = 0
        self.current_q = 0
        random.shuffle(questions)  # Shuffle questions for randomness
        
        self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=20)
        
        self.options = []
        self.selected_answer = tk.StringVar()

        for i in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.selected_answer, value="", font=("Arial", 12))
            btn.pack(anchor="w", padx=50)
            self.options.append(btn)
        
        self.submit_btn = tk.Button(root, text="Submit", command=self.check_answer, font=("Arial", 12), bg="blue", fg="white")
        self.submit_btn.pack(pady=20)
        
        self.restart_btn = tk.Button(root, text="Restart Quiz", command=self.restart_quiz, font=("Arial", 12), bg="green", fg="white")
        self.restart_btn.pack(pady=10)
        self.restart_btn.config(state=tk.DISABLED)
        
        self.display_question()

    def display_question(self):
        if self.current_q < len(questions):
            q_data = questions[self.current_q]
            self.question_label.config(text=q_data["question"])
            
            self.selected_answer.set("")  # Reset selected answer
            for i, option in enumerate(q_data["options"]):
                self.options[i].config(text=option, value=option)
        else:
            self.show_result()

        
    def check_answer(self):
        if not self.selected_answer.get():
            messagebox.showwarning("Warning", "Please select an answer!")
            return
        
        if self.selected_answer.get() == questions[self.current_q]["answer"]:
            self.score += 1
        
        self.current_q += 1
        self.display_question()
    
    def show_result(self):
        messagebox.showinfo("Quiz Over", f"Your Score: {self.score}/{len(questions)}")
        self.submit_btn.config(state=tk.DISABLED)
        self.restart_btn.config(state=tk.NORMAL)