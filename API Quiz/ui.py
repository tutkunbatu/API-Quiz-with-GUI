from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#233001"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("API Quiz Game")
        self.window.config(padx=25, pady=25, bg=THEME_COLOR)

        self.score_label = Label(text="Score = 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=270 ,text="Question", fill=THEME_COLOR, font=("Times New Roman", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, command=self.true_answer)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_have_questions():
            #Reset background
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text_new = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text_new)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            #Disabling the buttons at the end
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        self.feedback(self.quiz.check_answer("True"))
    def false_answer(self):
        self.feedback(self.quiz.check_answer("False"))
    def feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)