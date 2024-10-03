import random
import tkinter as tk
from tkinter import messagebox


def computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])


def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        return "You win!"
    else:
        return "You lose!"

def play_round(user_choice):
    comp_choice = computer_choice()
    result = determine_winner(user_choice, comp_choice)
    
    result_label.config(text=f"You chose {user_choice}, Computer chose {comp_choice}. {result}")
    
   
    if "win" in result:
        scores['user'] += 1
    elif "lose" in result:
        scores['computer'] += 1
    
    score_label.config(text=f"Score - You: {scores['user']}, Computer: {scores['computer']}")
    

def reset_game():
    scores['user'] = 0
    scores['computer'] = 0
    result_label.config(text="Let's start a new game!")
    score_label.config(text=f"Score - You: {scores['user']}, Computer: {scores['computer']}")
    

def confirm_exit():
    if messagebox.askokcancel("Quit", "Do you want to quit the game?"):
        root.destroy()


root = tk.Tk()
root.title("Rock, Paper, Scissors Game")


scores = {'user': 0, 'computer': 0}


instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
instruction_label.pack(pady=10)


btn_rock = tk.Button(root, text="Rock", width=15, command=lambda: play_round("Rock"))
btn_rock.pack(pady=5)

btn_paper = tk.Button(root, text="Paper", width=15, command=lambda: play_round("Paper"))
btn_paper.pack(pady=5)

btn_scissors = tk.Button(root, text="Scissors", width=15, command=lambda: play_round("Scissors"))
btn_scissors.pack(pady=5)


result_label = tk.Label(root, text="Let's start the game!", font=("Arial", 14))
result_label.pack(pady=10)

score_label = tk.Label(root, text=f"Score - You: {scores['user']}, Computer: {scores['computer']}", font=("Arial", 14))
score_label.pack(pady=10)


btn_reset = tk.Button(root, text="Reset Game", width=15, command=reset_game)
btn_reset.pack(pady=5)

btn_exit = tk.Button(root, text="Exit", width=15, command=confirm_exit)
btn_exit.pack(pady=5)


root.mainloop()

