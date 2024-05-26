import tkinter as tk
from tkinter import ttk, messagebox
import random

class MultiplicationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiplication App")
        
        # Default configurations
        self.default_font = ("Arial", 12)
        self.bg_color = "white"
        self.fg_color = "black"
        
        self.create_main_menu()

    def apply_settings(self, widget):
        widget.config(font=self.default_font, bg=self.bg_color, fg=self.fg_color)
        for child in widget.winfo_children():
            self.apply_settings(child)

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
        self.apply_settings(self.root)

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

    def change_text_size(self, size):
        self.default_font = (self.default_font[0], size)
        self.apply_settings(self.root)

    def change_font(self, font):
        self.default_font = (font, self.default_font[1])
        self.apply_settings(self.root)

    def change_color(self, color):
        if color == "High Contrast":
            self.bg_color = "black"
            self.fg_color = "white"
        elif color == "Dark Mode":
            self.bg_color = "gray20"
            self.fg_color = "white"
        elif color == "Default":
            self.bg_color = "white"
            self.fg_color = "black"
        elif color == "Blue":
            self.bg_color = "light blue"
            self.fg_color = "black"
        elif color == "Red":
            self.bg_color = "light coral"
            self.fg_color = "black"
        elif color == "Green":
            self.bg_color = "light green"
            self.fg_color = "black"
        self.apply_settings(self.root)

    def create_lessons_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.lessons_frame = ttk.Frame(self.root, padding="10")
        self.lessons_frame.pack(fill=tk.BOTH, expand=True)

        lessons_label = ttk.Label(self.lessons_frame, text="Lesson Levels: What Year Are You In?")
        lessons_label.pack(pady=10)

        for level in ["1-2", "3-4", "5-6"]:
            lesson_button = ttk.Button(self.lessons_frame, text=level, command=lambda level=level: self.show_lessons(level))
            lesson_button.pack(pady=5)

        self.create_home_button(self.lessons_frame)
        self.create_menu_bar()
        self.apply_settings(self.root)

    def show_lessons(self, level):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.lesson_frame = ttk.Frame(self.root, padding="10")
        self.lesson_frame.pack(fill=tk.BOTH, expand=True)

        lesson_content = {
            "1-2": "Introduction to multiplication and basic rules.",
            "3-4": "Two digit multiplication and grouping.",
            "5-6": "Three digit multiplication and decimals."
        }

        lesson_label = ttk.Label(self.lesson_frame, text=f"Year {level} Lesson")
        lesson_label.pack(pady=10)

        content_label = ttk.Label(self.lesson_frame, text=lesson_content[level])
        content_label.pack(pady=10)

        self.create_home_button(self.lesson_frame)
        self.create_menu_bar()
        self.apply_settings(self.root)

    def create_quizzes_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.quizzes_frame = ttk.Frame(self.root, padding="10")
        self.quizzes_frame.pack(fill=tk.BOTH, expand=True)

        quizzes_label = ttk.Label(self.quizzes_frame, text="Quiz Levels: What Year Are You In?")
        quizzes_label.pack(pady=10)

        for level in ["1-2", "3-4", "5-6"]:
            quiz_button = ttk.Button(self.quizzes_frame, text=level, command=lambda level=level: self.show_quiz(level))
            quiz_button.pack(pady=5)

        self.create_home_button(self.quizzes_frame)
        self.create_menu_bar()
        self.apply_settings(self.root)

    def show_quiz(self, level):
        self.quiz_level = level
        for widget in self.root.winfo_children():
            widget.destroy()

        self.quiz_frame = ttk.Frame(self.root, padding="10")
        self.quiz_frame.pack(fill=tk.BOTH, expand=True)

        self.questions = []
        self.answers = []
        self.score = 0
        self.current_question = 0

        if level == "1-2":
            self.generate_questions(1, 10)
        elif level == "3-4":
            self.generate_questions(10, 50)
        elif level == "5-6":
            self.generate_questions(50, 100)

        self.show_next_question()

        self.create_home_button(self.quiz_frame)
        self.create_menu_bar()
        self.apply_settings(self.root)

    def generate_questions(self, start, end):
        for _ in range(10):
            x = random.randint(start, end)
            y = random.randint(start, end)
            self.questions.append((x, y, x * y))

    def show_next_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            x, y, _ = question

            self.question_label = ttk.Label(self.quiz_frame, text=f"What is {x} times {y}?")
            self.question_label.pack(pady=10)

            options = [question[2]]
            while len(options) < 4:
                option = random.randint(question[2] - 10, question[2] + 10)
                if option not in options and option > 0:
                    options.append(option)
            random.shuffle(options)

            self.answer_var = tk.StringVar()
            for option in options:
                ttk.Radiobutton(self.quiz_frame, text=option, variable=self.answer_var, value=option).pack(pady=5)

            self.submit_button = ttk.Button(self.quiz_frame, text="Submit", command=self.check_answer)
            self.submit_button.pack(pady=10)

        else:
            self.show_final_score()

    def check_answer(self):
        if self.answer_var.get() == str(self.questions[self.current_question][2]):
            self.score += 1
            messagebox.showinfo("Correct!", "Well done, that's the correct answer!")
        else:
            messagebox.showerror("Incorrect", "Oops, that's not correct.")

        self.current_question += 1
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()

        self.show_next_question()

    def show_final_score(self):
        ttk.Label(self.quiz_frame, text=f"Quiz Finished. Your final score is: {self.score}").pack(pady=10)
        ttk.Label(self.quiz_frame, text="Well Done. Keep Practising to Get Better").pack(pady=10)
        self.create_home_button(self.quiz_frame)
        self.create_menu_bar()
        self.apply_settings(self.root)

    def create_home_button(self, frame):
        home_button = ttk.Button(frame, text="Home", command=self.create_main_menu)
        home_button.pack(anchor="ne")

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiplicationApp(root)
    root.mainloop()
