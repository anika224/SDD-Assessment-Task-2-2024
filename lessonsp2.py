import tkinter as tk
from tkinter import ttk, messagebox

class MultiplicationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiplication App")
        self.create_main_menu()

    def create_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        lessons_button = ttk.Button(self.main_frame, text="Lessons", command=self.create_lessons_menu)
        lessons_button.pack(pady=10)

        quizzes_button = ttk.Button(self.main_frame, text="Quizzes", command=self.create_quizzes_menu)
        quizzes_button.pack(pady=10)

        self.create_menu_bar()

    def create_menu_bar(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        
        text_size_menu = tk.Menu(edit_menu, tearoff=0)
        edit_menu.add_cascade(label="Text size", menu=text_size_menu)
        for size in [8, 10, 12, 14, 16]:
            text_size_menu.add_command(label=str(size), command=lambda size=size: self.change_text_size(size))

        font_menu = tk.Menu(edit_menu, tearoff=0)
        edit_menu.add_cascade(label="Fonts", menu=font_menu)
        for font in ["Times New Roman", "Arial", "Calibri", "Comic Sans MS", "Impact"]:
            font_menu.add_command(label=font, command=lambda font=font: self.change_font(font))

        colors_menu = tk.Menu(edit_menu, tearoff=0)
        edit_menu.add_cascade(label="Colours", menu=colors_menu)
        for color in ["High Contrast", "Dark Mode", "Default", "Blue", "Red", "Green"]:
            colors_menu.add_command(label=color, command=lambda color=color: self.change_color(color))

        edit_menu.add_command(label="Text to Speech", command=self.text_to_speech)

    def change_text_size(self, size):
        print(f"Text size changed to {size}")

    def change_font(self, font):
        print(f"Font changed to {font}")

    def change_color(self, color):
        print(f"Color scheme changed to {color}")

    def text_to_speech(self):
        print("Text to Speech function activated")

    def create_lessons_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.lessons_frame = ttk.Frame(self.root, padding="10")
        self.lessons_frame.pack(fill=tk.BOTH, expand=True)

        self.create_home_button(self.lessons_frame)

        lessons_label = ttk.Label(self.lessons_frame, text="Lesson Levels: What Year Are You In?")
        lessons_label.pack(pady=10)

        for level in ["1-2", "3-4", "5-6"]:
            lesson_button = ttk.Button(self.lessons_frame, text=level, command=lambda level=level: self.show_lessons(level))
            lesson_button.pack(pady=5)

    def show_lessons(self, level):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.lesson_frame = ttk.Frame(self.root, padding="10")
        self.lesson_frame.pack(fill=tk.BOTH, expand=True)

        self.create_home_button(self.lesson_frame)

        lesson_content = {
            "1-2": "Introduction to multiplication and basic rules.",
            "3-4": "Two digit multiplication and grouping.",
            "5-6": "Three digit multiplication and decimals."
        }

        lesson_label = ttk.Label(self.lesson_frame, text=f"Year {level} Lesson")
        lesson_label.pack(pady=10)

        content_label = ttk.Label(self.lesson_frame, text=lesson_content[level])
        content_label.pack(pady=10)

    def create_quizzes_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.quizzes_frame = ttk.Frame(self.root, padding="10")
        self.quizzes_frame.pack(fill=tk.BOTH, expand=True)

        self.create_home_button(self.quizzes_frame)

        quizzes_label = ttk.Label(self.quizzes_frame, text="Quiz Levels: What Year Are You In?")
        quizzes_label.pack(pady=10)

        for level in ["1-2", "3-4", "5-6"]:
            quiz_button = ttk.Button(self.quizzes_frame, text=level, command=lambda level=level: self.show_quiz(level))
            quiz_button.pack(pady=5)

    def show_quiz(self, level):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.quiz_frame = ttk.Frame(self.root, padding="10")
        self.quiz_frame.pack(fill=tk.BOTH, expand=True)

        self.create_home_button(self.quiz_frame)

        quiz_content = {
            "1-2": ["What is 2 x 3?", "What is 5 x 1?"],
            "3-4": ["What is 12 x 3?", "What is 25 x 4?"],
            "5-6": ["What is 123 x 3?", "What is 251 x 4?"]
        }

        quiz_label = ttk.Label(self.quiz_frame, text=f"Year {level} Quiz")
        quiz_label.pack(pady=10)

        questions = quiz_content[level]
        self.quiz_index = 0
        self.score = 0

        self.question_label = ttk.Label(self.quiz_frame, text=questions[self.quiz_index])
        self.question_label.pack(pady=10)

        if level == "1-2":
            for answer in ["A", "B", "C", "D"]:
                answer_button = ttk.Button(self.quiz_frame, text=f"Answer {answer}", command=self.answer_question)
                answer_button.pack(pady=5)
        else:
            self.answer_entry = ttk.Entry(self.quiz_frame)
            self.answer_entry.pack(pady=10)
            submit_button = ttk.Button(self.quiz_frame, text="Submit", command=self.submit_answer)
            submit_button.pack(pady=5)

        self.score_label = ttk.Label(self.quiz_frame, text=f"Score: {self.score}")
        self.score_label.pack(pady=10)

    def answer_question(self):
        self.quiz_index += 1
        self.score += 1
        self.update_quiz()

    def submit_answer(self):
        self.quiz_index += 1
        self.score += 1
        self.update_quiz()

    def update_quiz(self):
        quiz_content = {
            "1-2": ["What is 2 x 3?", "What is 5 x 1?"],
            "3-4": ["What is 12 x 3?", "What is 25 x 4?"],
            "5-6": ["What is 123 x 3?", "What is 251 x 4?"]
        }
        level = self.quiz_level
        questions = quiz_content[level]
        if self.quiz_index < len(questions):
            self.question_label.config(text=questions[self.quiz_index])
        else:
            self.question_label.config(text="Quiz Finished")
            self.score_label.config(text=f"Your Final Score: {self.score}")

    def create_home_button(self, frame):
        home_button = ttk.Button(frame, text="Home", command=self.create_main_menu)
        home_button.pack(anchor="ne")


root = tk.Tk()
app = MultiplicationApp(root)


root.mainloop()
