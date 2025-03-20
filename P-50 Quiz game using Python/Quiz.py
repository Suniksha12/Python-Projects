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