



# def addTwoNumbers(l1, l2):
#     str1 = ""
#     str2 = ""
#     for i in range(len(l1)-1, -1, -1):
#         str1 = str1+str(l1[i])
#     for i in range(len(l2)-1, -1, -1):
#         str2 = str2+str(l2[i])
#     print(int(str1)+int(str2))

def addTwoNumbers(l1, l2):
    list1 = []
    list2 = []
    for i in l1:
        list1.append(i)
    for i in l2:
        list2.append(i)
    rev1 = reversed(list1)
    rev2 = reversed(list2)


l1 = [2, 4, 3]
l2 = [5, 6, 4]

addTwoNumbers(l1, l2)

