from tkinter import *
import random
import tkinter.messagebox
import math

main_window = Tk()
main_window.minsize(500,200) #sets the mininum size for the window
main_window.title('Guess the number')



number = random.randint(1,20)

def check_number():
    guess = number_input.get()
    guess = int(guess)
    if guess > number :
        tkinter.messagebox.showinfo('High','Your guess is too high')

    if guess < number :
        tkinter.messagebox.showinfo('Low','You guess is too low')

    if guess == number :
        tkinter.messagebox.showinfo('Correct','You are correct!')

def btn_confirm():
    name = name_input.get()
    tkinter.messagebox.showinfo('Welcome','Well ' +name +' I am thinking of a number, 1 to 20')

#name
welcome_label = tkinter.Label(main_window, text = 'Welcome to guess the number!')
welcome_label.pack()

name_label = tkinter.Label(main_window, text = 'Please enter your name:')
name_label.place(x = 25, y = 25)

name_input = tkinter.Entry(main_window, width = 25)
name_input.place(x = 200, y = 25)

name_confirm_button = tkinter.Button(main_window, text = 'Confirm', command = btn_confirm)
name_confirm_button.place(x = 400, y= 25)


# input
guess_prompt_label = tkinter.Label(main_window, text = 'Take a guess')
guess_prompt_label.place(x = 25, y = 75)

number_input = tkinter.Entry(main_window, width = 25)
number_input.place(x = 200, y = 75)

guess_confirm_button = tkinter.Button(main_window, text = 'Confirm guess', command = check_number)
guess_confirm_button.place(x = 400, y = 75)


main_window.mainloop()
