import tkinter as tk
import random

# Unicode dice characters
dice_faces = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']

def roll_dice():
    face = random.choice(dice_faces)
    dice_label.config(text=face, font=("Helvetica", 100), fg="#333")
    result_label.config(text=f"You rolled: {dice_faces.index(face) + 1}")

# GUI setup
root = tk.Tk()
root.title("🎲 Dice Roller")
root.geometry("500x500")
root.configure(bg="#f0f4f8")

title = tk.Label(root, text="Roll the Dice!", font=("Helvetica", 18, "bold"), bg="#f0f4f8")
title.pack(pady=10)

dice_label = tk.Label(root, text="🎲", font=("Helvetica", 100), bg="#f0f4f8")
dice_label.pack(pady=10)

roll_button = tk.Button(root, text="Roll Dice", font=("Helvetica", 14), bg="#007acc", fg="white", padx=10, pady=5, command=roll_dice)
roll_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f4f8", fg="#444")
result_label.pack(pady=10)

root.mainloop()
