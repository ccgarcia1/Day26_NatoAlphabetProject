import pandas as pd


data = pd.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
#Loop through rows of a data frame
# Keyword Method with iterrows()
phonetic_alphabet_dic = {row['letter']: row['code'] for (index, row) in data.iterrows()}
print(phonetic_alphabet_dic) # result must be {"A": "Alfa", "B": "Bravo"...}
# we could get the same result using:
# phonetic_alphabet_dic = data.to_dict()




#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Insira um nome: ").upper()
result = [phonetic_alphabet_dic[letter] for letter in user_input]

print(result)
