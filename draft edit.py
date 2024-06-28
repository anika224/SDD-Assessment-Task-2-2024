import tkinter as tk
from tkinter import ttk, messagebox
import random

class MultiplicationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiplication App")
        self.root.geometry("600x400")

        # Default configurations
        self.default_font = ("Arial", 12)

        # Initialize default color theme
        self.bg_color = "white"
        self.fg_color = "black"
        self.btn_bg_color = "lightgrey"

        # Theme colors dictionary
        self.theme_colors = {
            "High Contrast": {"bg": "black", "fg": "white", "btn_bg": "grey"},
            "Dark Mode": {"bg": "gray20", "fg": "white", "btn_bg": "gray30"},
            "Default": {"bg": "white", "fg": "black", "btn_bg": "lightgrey"},
            "Blue": {"bg": "light blue", "fg": "black", "btn_bg": "skyblue"},
            "Red": {"bg": "light coral", "fg": "black", "btn_bg": "indianred"},
            "Green": {"bg": "light green", "fg": "black", "btn_bg": "lightgreen"},
        }

        # Maintain a list of all widgets to apply settings
        self.all_widgets = []

        # Initialize the main menu
        self.create_main_menu()

    def apply_settings(self):
        # Apply the current font and color settings to all widgets
        for widget in self.all_widgets:
            try:
                widget.config(font=self.default_font)
            except tk.TclError:
                pass
        for frame in self.root.winfo_children():
            try:
                frame.config(bg=self.bg_color)
                for child in frame.winfo_children():
                    child.config(bg=self.bg_color, fg=self.fg_color)
                    if isinstance(child, ttk.Button):
                        child.config(style="Custom.TButton")
            except tk.TclError:
                pass

        self.root.config(bg=self.bg_color)
        
        style = ttk.Style()
        style.configure("Custom.TButton", font=self.default_font, background=self.btn_bg_color)

    def create_main_menu(self):
        # Clear current widgets
        self.clear_widgets()

        # Create main frame
        self.main_frame = tk.Frame(self.root, bg=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        self.all_widgets.append(self.main_frame)

        # Add buttons for Lessons and Quizzes
        lessons_button = ttk.Button(self.main_frame, text="Lessons", command=self.create_lessons_menu)
        lessons_button.pack(pady=10)
        self.all_widgets.append(lessons_button)

        quizzes_button = ttk.Button(self.main_frame, text="Quizzes", command=self.create_quizzes_menu)
        quizzes_button.pack(pady=10)
        self.all_widgets.append(quizzes_button)

        # Create the menu bar
        self.create_menu_bar()

        # Apply the settings
        self.apply_settings()

    def create_menu_bar(self):
        # Create a menu bar
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # Add 'Edit' menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # Add 'Text size' submenu
        text_size_menu = tk.Menu(edit_menu, tearoff=0)
        edit_menu.add_cascade(label="Text size", menu=text_size_menu)
        for size in [8, 10, 12, 14, 16]:
            text_size_menu.add_command(label=str(size), command=lambda size=size: self.change_text_size(size))

        # Add 'Fonts' submenu
        font_menu = tk.Menu(edit_menu, tearoff=0)
        edit_menu.add_cascade(label="Fonts", menu=font_menu)
        for font in ["Times New Roman", "Arial", "Calibri", "Comic Sans MS", "Impact"]:
            font_menu.add_command(label=font, command=lambda font=font: self.change_font(font))

        # Add 'Colours' submenu
        colours_menu = tk.Menu(edit_menu, tearoff=0)
        edit_menu.add_cascade(label="Colours", menu=colours_menu)
        for colour in self.theme_colors.keys():
            colours_menu.add_command(label=colour, command=lambda colour=colour: self.change_theme(colour))

    def change_text_size(self, size):
        # Change the text size
        self.default_font = (self.default_font[0], size)
        self.apply_settings()

    def change_font(self, font):
        # Change the font
        self.default_font = (font, self.default_font[1])
        self.apply_settings()

    def change_theme(self, theme_name):
        # Change the color theme
        theme = self.theme_colors.get(theme_name)
        if theme:
            self.bg_color = theme["bg"]
            self.fg_color = theme["fg"]
            self.btn_bg_color = theme["btn_bg"]
            self.apply_settings()

    def create_lessons_menu(self):
        # Clear current widgets
        self.clear_widgets()

        # Create lessons frame
        self.lessons_frame = tk.Frame(self.root, bg=self.bg_color)
        self.lessons_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        self.all_widgets.append(self.lessons_frame)

        # Add label and buttons for lesson levels
        lessons_label = ttk.Label(self.lessons_frame, text="Lesson Levels: What Year Are You In?")
        lessons_label.pack(pady=10)
        self.all_widgets.append(lessons_label)

        for level in ["1-2", "3-4", "5-6"]:
            lesson_button = ttk.Button(self.lessons_frame, text=level, command=lambda level=level: self.show_lessons(level))
            lesson_button.pack(pady=5)
            self.all_widgets.append(lesson_button)

        # Add home button
        self.create_home_button(self.lessons_frame)

        # Create the menu bar
        self.create_menu_bar()

        # Apply the settings
        self.apply_settings()

    def show_lessons(self, level):
        # Clear current widgets
        self.clear_widgets()

        # Create lesson frame
        self.lesson_frame = tk.Frame(self.root, bg=self.bg_color)
        self.lesson_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        self.all_widgets.append(self.lesson_frame)

        # Lesson content based on levels
        lesson_content = {
            "1-2": "Introduction to multiplication and basic rules.",
            "3-4": "Two digit multiplication and grouping.",
            "5-6": "Three digit multiplication and decimals."
        }

        # Add lesson labels
        lesson_label = ttk.Label(self.lesson_frame, text=f"Year {level} Lesson")
        lesson_label.pack(pady=10)
        self.all_widgets.append(lesson_label)

        content_label = ttk.Label(self.lesson_frame, text=lesson_content[level])
        content_label.pack(pady=10)
        self.all_widgets.append(content_label)

        # Add home button
        self.create_home_button(self.lesson_frame)

        # Create the menu bar
        self.create_menu_bar()

        # Apply the settings
        self.apply_settings()

    def create_quizzes_menu(self):
        # Clear current widgets
        self.clear_widgets()

        # Create quizzes frame
        self.quizzes_frame = tk.Frame(self.root, bg=self.bg_color)
        self.quizzes_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        self.all_widgets.append(self.quizzes_frame)

        # Add label and buttons for quiz levels
        quizzes_label = ttk.Label(self.quizzes_frame, text="Quiz Levels: What Year Are You In?")
        quizzes_label.pack(pady=10)
        self.all_widgets.append(quizzes_label)

        for level in ["1-2", "3-4", "5-6"]:
            quiz_button = ttk.Button(self.quizzes_frame, text=level, command=lambda level=level: self.show_quiz(level))
            quiz_button.pack(pady=5)
            self.all_widgets.append(quiz_button)

        # Add home button
        self.create_home_button(self.quizzes_frame)

        # Create the menu bar
        self.create_menu_bar()

        # Apply the settings
        self.apply_settings()

    def show_quiz(self, level):
        self.quiz_level = level

        # Clear current widgets
        self.clear_widgets()

        # Create quiz frame
        self.quiz_frame = tk.Frame(self.root, bg=self.bg_color)
        self.quiz_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        self.all_widgets.append(self.quiz_frame)

        self.questions = []
        self.answers = []
        self.score = 0
        self.current_question = 0

        # Generate questions based on the level
        if level == "1-2":
            self.generate_questions(1, 10)
        elif level == "3-4":
            self.generate_questions(10, 50)
        elif level == "5-6":
            self.generate_questions(30, 100)

        # Show the next question
        self.show_next_question()

        # Add home button
        self.create_home_button(self.quiz_frame)

        # Create the menu bar
        self.create_menu_bar()

        # Apply the settings
        self.apply_settings()

    def generate_questions(self, start, end):
        # Generate a set of random multiplication questions
        for _ in range(10):
            x = random.randint(start, end)
            y = random.randint(start, end)
            self.questions.append((x, y, x * y))

    def show_next_question(self):
        # Display the next question or show the final score
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            x, y = question[0], question[1]

            self.question_frame = tk.Frame(self.quiz_frame, bg=self.bg_color)
            self.question_frame.pack(pady=10)
            self.all_widgets.append(self.question_frame)

            self.question_label = ttk.Label(self.question_frame, text=f"What is {x} times {y}?")
            self.question_label.pack(pady=10)
            self.all_widgets.append(self.question_label)

            # Create a frame for the answer options
            self.options_frame = tk.Frame(self.quiz_frame, bg=self.bg_color)
            self.options_frame.pack(pady=10)
            self.all_widgets.append(self.options_frame)

            # Generate options for the answer
            options = [question[2]]
            while len(options) < 4:
                option = random.randint(question[2] - 10, question[2] + 10)
                if option not in options and option > 0:
                    options.append(option)
            random.shuffle(options)

            # Display answer options
            self.answer_var = tk.StringVar()
            for option in options:
                rb = ttk.Radiobutton(self.options_frame, text=option, variable=self.answer_var, value=option)
                rb.pack(side=tk.LEFT, padx=20, pady=5)
                self.all_widgets.append(rb)

            # Submit button
            self.submit_button = ttk.Button(self.quiz_frame, text="Submit", command=self.check_answer)
            self.submit_button.pack(pady=10)
            self.all_widgets.append(self.submit_button)

            # Score display
            self.score_label = ttk.Label(self.quiz_frame, text=f"Score: {self.score}")
            self.score_label.pack(pady=10)
            self.all_widgets.append(self.score_label)
        else:
            self.show_final_score()

    def check_answer(self):
        # Check if the answer is correct and update the score
        if self.answer_var.get() == str(self.questions[self.current_question][2]):
            self.score += 1
            messagebox.showinfo("Correct!", "Well done, that's the correct answer!")
        else:
            messagebox.showerror("Incorrect", "Oops, that's not correct.")

        self.current_question += 1
        self.clear_widgets(frame=self.quiz_frame)

        # Show the next question
        self.show_next_question()

    def show_final_score(self):
        # Show the final score after the quiz
        ttk.Label(self.quiz_frame, text=f"Quiz Finished. Your final score is: {self.score}").pack(pady=10)
        ttk.Label(self.quiz_frame, text="Well Done. Keep Practising to Get Even Better").pack(pady=10)

        # Add home button
        self.create_home_button(self.quiz_frame)

        # Create the menu bar
        self.create_menu_bar()

        # Apply the settings
        self.apply_settings()

    def create_home_button(self, frame):
        # Create a home button to return to the main menu
        home_button = ttk.Button(frame, text="Home", command=self.create_main_menu)
        home_button.pack(anchor="nw", pady=10, padx=10)
        self.all_widgets.append(home_button)

    def clear_widgets(self, frame=None):
        # Clear all widgets from the frame
        if frame is None:
            frame = self.root
        for widget in frame.winfo_children():
            widget.destroy()
        self.all_widgets = []

# Create the main Tkinter window
root = tk.Tk()
# Initialize the MultiplicationApp
app = MultiplicationApp(root)
# Run the main loop
root.mainloop()
