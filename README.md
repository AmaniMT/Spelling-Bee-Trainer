# Spelling Bee Trainer

This repository contains a simple Python program for a spelling bee trainer application  using tkinter.

## Features:

1. **Word Pronunciation:** Users can listen to the pronunciation of the word by clicking on the sound icon.
2. **Spell Checker:** Users can input their spelling of the word, and the program provides instant feedback on correctness.
3. **Definition Lookup:** Users can click the "Define" button to get the definition of the word.
4. **Data Persistence:** User progress and word lists are saved in CSV files for future sessions.
5. **Statistics:** At the end of the session, the program displays the words with the most wrong guesses.



## Usage:

1. Ensure all dependencies are installed (`pip install -r requirements.txt`).
2. Replace the `data.csv` file with your own list of words to be learned.
3. When you run the program for the first time, a `to-learn.csv` will be created. Make sure that the `to-learn.csv` file is empty or delete it before running the program. If it contains data, it will be used instead of `data.csv`. 
4. Run the program using `python spelling_bee_trainer.py`.
5. Follow the instructions on the graphical user interface to spell words and get feedback.



## File Structure:

- `spelling_bee_trainer.py`: The main Python script containing the application logic.
- `data.csv`: CSV file containing a list of words to be learned.
- `to-learn.csv`: CSV file for storing words that the user still needs to learn.
- `sound.png`: Image file used for the sound icon in the GUI.
