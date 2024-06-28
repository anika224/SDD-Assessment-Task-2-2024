import tkinter as tk
from tkinter import ttk, messagebox
import random

class MultiplicationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiplication App")
        self.root.geometry("800x600")

        # Default configurations
        self.default_font = ("Arial", 12)

        # Initialize default color theme
        self.bg_color = "white"
        self.fg_color = "black"
        self.btn_bg_color = "lightgrey"

        # Theme colors dictionary
        self.theme_colors = {
            "High Contrast": {"bg": "dark blue", "fg": "purple", "btn_bg": "dark blue"},
            "Dark Mode": {"bg": "gray20", "fg": "white", "btn_bg": "gray20"},
            "Default": {"bg": "white", "fg": "black", "btn_bg": "white"},
            "Blue": {"bg": "light blue", "fg": "black", "btn_bg": "light blue"},
            "Red": {"bg": "light coral", "fg": "black", "btn_bg": "light coral"},
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
            "1-2": "Multiplication is defined as repeated addition. It is that simple! You add groups of the same number together. For example, when we multiply 2 by 3, 3 is added to itself twice, resulting in 3 + 3 = 6.\n\nRules: Producting an integer with 0 always yields 0. For example, 3 x 0 = 0.\nThe product of a number with one is always the other number. For example, 3 x 1 equals 3.\n\nHint: When multiplying by 10, add a 0 to the end of the other number. For example, 3 x 10 equals 30.",
            "3-4": "Two-digit multiplication is just the multiplication of a single digit twice. It begins the same way, with multiplying the numbers in the one place, followed by a second round of multiplication using the numbers in the ten position.\n\nLet's say we have two numbers: 12 and 34. We can divide these numbers into tens and ones. So 12 becomes 10 and 2, whereas 34 becomes 30 and 4.\n\nNext, we multiply each part of the first number by each part of the second number. So we multiply 10 by 30 to get 300; 10 by 4 to get 40; 2 by 30 to get 60; and 2 by 4 to get 8.\n\nThe findings are then combined together. So, 300 + 40 + 60 + 8 = 408. So that's our response!\n\nThis procedure is called grouping because we separate the tens and ones before multiplying and adding them. It's an excellent approach to learn how multiplication works with huge numbers. Remember: practice makes perfect! Happy learning!",
            "5-6": "When we multiply three-digit integers, we arrange them in columns based on the digits' place values. The place values are one, ten, and hundreds.\n\nNow let's speak about decimals. Decimals are fractions of a whole number. They employ a decimal point to distinguish the complete number from the fractional component. For example, in the number 1.23, '1' represents the full number, whereas '23' represents the fractional component.\n\nWhen multiplying decimals, we start as if they were whole numbers. Then we count the total number of digits following the decimal point in the original numbers. The response should have the same amount of digits following the decimal point.\n\nTo multiply 0.03 (2 decimal places) by 1.1 (1 decimal place), we first multiply them as whole integers (3 x 11 = 33). Then, we put the decimal point in the answer so it has three decimal places, giving us 0.033.\n\nRemember, practice is key when learning new mathematical concepts. Happy learning!"
        }

        # Add lesson labels
        lesson_label = ttk.Label(self.lesson_frame, text=f"Lesson for Level {level}")
        lesson_label.pack(pady=10)
        self.all_widgets.append(lesson_label)

        lesson_text = tk.Text(self.lesson_frame, wrap=tk.WORD, height=20, width=80)
        lesson_text.insert(tk.END, lesson_content[level])
        lesson_text.config(state=tk.DISABLED, bg=self.bg_color, fg=self.fg_color, font=self.default_font)
        lesson_text.pack(pady=10)
        self.all_widgets.append(lesson_text)

        # Add back button
        back_button = ttk.Button(self.lesson_frame, text="Back to Lessons Menu", command=self.create_lessons_menu)
        back_button.pack(pady=10)
        self.all_widgets.append(back_button)

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
        quizzes_label = ttk.Label(self.quizzes_frame, text="Quiz Levels: Select Your Level")
        quizzes_label.pack(pady=10)
        self.all_widgets.append(quizzes_label)

        for level in ["1-2", "3-4", "5-6"]:
            quiz_button = ttk.Button(self.quizzes_frame, text=level, command=lambda level=level: self.start_quiz(level))
            quiz_button.pack(pady=5)
            self.all_widgets.append(quiz_button)

        # Add home button
        self.create_home_button(self.quizzes_frame)

        # Create the menu bar
        self.create_menu_bar()

        # Apply the settings
        self.apply_settings()

    def start_quiz(self, level):
        # Set the current level for the quiz
        self.current_level = level

        # Clear current widgets
        self.clear_widgets()

        # Create quiz frame
        self.quiz_frame = tk.Frame(self.root, bg=self.bg_color)
        self.quiz_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        self.all_widgets.append(self.quiz_frame)

        # Add quiz question label
        self.question_label = ttk.Label(self.quiz_frame, text="Solve the following multiplication:")
        self.question_label.pack(pady=10)
        self.all_widgets.append(self.question_label)

        # Add quiz question
        self.generate_question(level)

        # Add answer entry
        self.answer_entry = ttk.Entry(self.quiz_frame)
        self.answer_entry.pack(pady=10)
        self.all_widgets.append(self.answer_entry)

        # Add submit button
        submit_button = ttk.Button(self.quiz_frame, text="Submit", command=self.check_answer)
        submit_button.pack(pady=10)
        self.all_widgets.append(submit_button)

        # Add back button
        back_button = ttk.Button(self.quiz_frame, text="Back to Quizzes Menu", command=self.create_quizzes_menu)
        back_button.pack(pady=10)
        self.all_widgets.append(back_button)

        # Add home button
        self.create_home_button(self.quiz_frame)

        # Create the menu bar
        self.create_menu_bar()

        # Apply the settings
        self.apply_settings()

    def generate_question(self, level):
        # Generate multiplication question based on level
        if level == "1-2":
            self.num1 = random.randint(1, 10)
            self.num2 = random.randint(1, 10)
        elif level == "3-4":
            self.num1 = random.randint(10, 20)
            self.num2 = random.randint(10, 20)
        else:
            self.num1 = random.randint(100, 200)
            self.num2 = random.randint(10, 100)

        self.correct_answer = self.num1 * self.num2
        self.question_label.config(text=f"What is {self.num1} x {self.num2}?")

    def check_answer(self):
        # Check the user's answer
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.correct_answer:
                messagebox.showinfo("Correct", "Well done! That's the correct answer.")
            else:
                messagebox.showerror("Incorrect", f"Sorry, the correct answer is {self.correct_answer}.")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")

        # Clear the answer entry
        self.answer_entry.delete(0, tk.END)
        self.generate_question(self.current_level)

    def create_home_button(self, frame):
        # Add home button to the frame
        home_button = ttk.Button(frame, text="Home", command=self.create_main_menu)
        home_button.pack(pady=10)
        self.all_widgets.append(home_button)

    def clear_widgets(self):
        # Clear all current widgets from the root
        for widget in self.root.winfo_children():
            widget.destroy()
        self.all_widgets.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiplicationApp(root)
    root.mainloop()
