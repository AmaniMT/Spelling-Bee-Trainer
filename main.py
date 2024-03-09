import pandas as pd
from tkinter import *
from gtts import gTTS
import pygame
import random
from io import BytesIO
from PyDictionary import PyDictionary


# Function to play the pronunciation of the word
def play_sound():
    mp3_fp = BytesIO()
    obj = gTTS(text=word, lang='en', slow=False)
    obj.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    pygame.mixer.pre_init(24000)
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_fp)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


# Function to handle user input and provide feedback
def on_enter(event):
    global word, wrong_guesses

    elements = [canvas, window, button, label, wrong_word_label]
    user_answer = entry.get()
    entry.delete(0, END)
    if user_answer.lower().strip() == word.lower().strip():
        wrong_word_label.config(text="")
        for element in elements:
            element.config(bg='green')
        lst.remove(word)
    else:
        for element in elements:
            element.config(bg='red')
        wrong_word_label.config(text=f"Wrong: {word}")
        wrong_guesses[word] = wrong_guesses.get(word, 0) + 1

    for element in elements[:5]:
        element.after(1000, lambda e=element: e.config(bg='SystemButtonFace'))

    if not lst:
        window.destroy()
    else:
        word = random.choice(lst)
    window.after(1100, lambda: play_sound())


# Function to get the definition of the current word
def define():
    print(dictionary.meaning(word))


# Attempt to read from "to-learn.csv", if it's empty, read from "data.csv" and write to "to-learn.csv"
try:
    df_to_learn = pd.read_csv("to-learn.csv", header=None)
except (pd.errors.EmptyDataError, FileNotFoundError):
    df_to_learn = pd.read_csv("data.csv", header=None)
    df_to_learn.stack().dropna().to_csv("to-learn.csv", header=None, index=None)

lst = df_to_learn.stack().dropna().tolist()
wrong_guesses = {}
word = random.choice(lst)
dictionary = PyDictionary()

# Initialize tkinter window
window = Tk()
window.config(pady=10, padx=10)
window.title("Spelling Bee Trainer")

# Create GUI elements: canvas, sound button, label, entry, wrong word label
canvas = Canvas(width=200, height=100, highlightthickness=0)
canvas.grid(row=0, column=0)
sound_img = PhotoImage(file="sound.png")
button = Button(image=sound_img, command=play_sound, highlightthickness=0, border=0)
button.grid(row=0, column=0)
label = Label(text="Spell the word:")
entry = Entry()
entry.bind("<Return>", on_enter)
label.grid(row=1, column=0)
entry.grid(row=2, column=0)
wrong_word_label = Label(text="", fg="red")
wrong_word_label.grid(row=3, column=0)

# Schedule the pronunciation of the initial word after 100 milliseconds
window.after(100, lambda: play_sound())

# Create a button to get the definition of the word
button = Button(text="Define", command=define)
button.grid(row=4, column=0)

# Run the tkinter event loop
window.mainloop()

# Save the remaining words to learn to "to-learn.csv"
pd.DataFrame(lst).to_csv("to-learn.csv", index=False, header=False)

# Sort the wrong guesses and display them
sorted_wrong_guesses = sorted(wrong_guesses.items(), key=lambda x: x[1], reverse=True)
df_wrong_guesses = pd.DataFrame(sorted_wrong_guesses, columns=['Word', 'Wrong Guesses'])
print("Wrong Guesses (Most to Least):")
print(df_wrong_guesses.to_string(index=False))
