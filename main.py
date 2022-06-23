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
query = input("Enter The Text: ").lower().replace(" ", "")
quaery_list = list(query)
selected_words = [data_dictonary[letter] for letter in quaery_list]

# Printing the output
seprator = ", "
print(f"You can spell it as: {seprator.join(selected_words)}")