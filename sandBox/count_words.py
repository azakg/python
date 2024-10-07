with open("words_text.txt","r") as text_file:
    txt1 = text_file.read().split()
print(len(txt1))
# for x in txt1:
#     print(x)