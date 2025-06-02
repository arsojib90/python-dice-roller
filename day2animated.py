import tkinter as tk
import random

dice_faces = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']

rolling = False
roll_count = 0
final_face = ""

def animate_roll():
    global roll_count, final_face
    if roll_count < 10:
        face = random.choice(dice_faces)
        dice_label.config(text=face, font=("Helvetica", 100))
        roll_count += 1
        root.after(100, animate_roll)  # Continue animation
    else:
        dice_label.config(text=final_face, font=("Helvetica", 100))
        result_label.config(text=f"You rolled: {dice_faces.index(final_face)+1}")
        roll_button.config(state="normal")  # Enable button again

def roll_dice():
    global roll_count, final_face
    roll_button.config(state="disabled")  # Disable button during roll
    roll_count = 0
    final_face = random.choice(dice_faces)
    animate_roll()

# GUI setup
root = tk.Tk()
root.title("🎲 Dice Roller with Animation")
root.geometry("300x300")
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
