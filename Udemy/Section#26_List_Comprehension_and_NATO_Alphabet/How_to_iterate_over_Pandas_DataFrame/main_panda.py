student_dic = {"student": ["Angela", "james", "Lily"],
               "score": [56, 76,98]}
#________________________________________________________________________
# Standard iteration over Dic

for (key, value) in student_dic.items():
    print(key)
    print(value)
print("########################################################################")


########################################################################

import pandas
# ________________________________________________________________________
# Create Panda's DataFrame from Dictionary
print("This is Dic converted into Pandas DataFrame")
student_data_frame = pandas.DataFrame(student_dic)
print(student_data_frame)
print("########################################################################")
# Looping through a data Frame
print("This is loop through DataFrame")
for (key, value) in student_data_frame.items():
    print(key)
    print(value)

#__________________________________________________________________________________________
# Loop through rows of Data Frame
print("###########################################################################")
print("This is Loop through rows of Data Frame")
for (index, row) in student_data_frame.iterrows():
    if row.student == "Lily":
        print(row.score)

