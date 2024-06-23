import pandas as pd


"""script that converts a word into the nato phonetic equivalent"""

# import letter/code mappings as df
df = pd.read_csv("Day26/nato_phonetic_alphabet.csv")

# convert to dictionary without columns headers/index
alpha_dict = {row.letter:row.code for (index, row) in df.iterrows()}

# create list of phonetic code words from a word the user inputs
user_word = input("Enter a word: ").upper()
code_words = [alpha_dict[letter] for letter in user_word]

print(code_words)
