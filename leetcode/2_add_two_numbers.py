



# def addTwoNumbers(l1, l2):
#     str1 = ""
#     str2 = ""
#     for i in range(len(l1)-1, -1, -1):
#         str1 = str1+str(l1[i])
#     for i in range(len(l2)-1, -1, -1):
#         str2 = str2+str(l2[i])
#     print(int(str1)+int(str2))

def addTwoNumbers(l1, l2):
    list1 = l1[-1::-1]
    list2 = l2
    print(list1)
    # list1.reverse()
    # list2.reverse()
    num_str1 = [str(i) for i in list1]
    num_str2 = [str(i) for i in list2]
    num_str1_join = "".join(num_str1)
    num_str2_join = "".join(num_str2)
    result = int(num_str1_join)+int(num_str2_join)
    final_result = []
    for i in range(len(str(result))):
        final_result.append(str(result)[i])
    final_result1 = [int(i) for i in final_result]
    # print(final_result1)




l1 = [2, 4, 3]
l2 = [5, 6, 4]

addTwoNumbers(l1, l2)

