student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dic = {row.letter:row.code for index,row in data.iterrows()}
# print(phonetic_dic)



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# input_word = input("Please input word: ").upper()
# index = -1
# output_list = [name for name in alphabet_list if input_word[index + 1] == alphabet_list[index + 1]]
# print(output_list)

word = input("Enter a word: ").upper()
output_list = [phonetic_dic[letter] for letter in word]
print(output_list)
