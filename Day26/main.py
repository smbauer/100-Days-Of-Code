import pandas as pd


"""script that converts a word into the nato phonetic equivalent"""

# import letter/code mappings as df
df = pd.read_csv("Day26/nato_phonetic_alphabet.csv")

# convert to dictionary without columns headers/index
alpha_dict = {row.letter:row.code for (index, row) in df.iterrows()}

is_valid = False

# create list of phonetic code words from a word the user inputs
while not is_valid:
    user_word = input("Enter a word: ").upper()
    try:
        code_words = [alpha_dict[letter] for letter in user_word]
    except KeyError:
        print("Only letters in the alphabet are allowed")
    else:
        is_valid = True
        
print(code_words)
