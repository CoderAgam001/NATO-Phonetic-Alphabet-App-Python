# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @coderagam001 / @codewithagam
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

import pandas as pd

# Redaing the CSV data
data = pd.read_csv('data.csv')
data_dictonary = {row.Letter:row.Code for (index, row) in data.iterrows()}

# Getting the input from the user
name = input("Enter Your Name: ").upper()
name_string = name.replace(" ", "")
name_list = list(name_string)
selected_words = [data_dictonary[letter] for letter in name_list]

# Printing the output
seprator = ", "
print(f"{name} can be spelled as: {seprator.join(selected_words)}")