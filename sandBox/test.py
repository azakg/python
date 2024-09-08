# int_str_list = "2 1 -1 1 -1 2" #input("Type list of numbers: ")
# new_str = int_str_list.split()
# list = []
# for b in new_str:
#     list.append(int(b))
# print(max(list))

#
# list = []
# for n in new_str:
#     list.append(int(n))
#
# sum_of_list = 0
# for x in list:
#     if x > sum_of_list:
#         sum_of_list = x
# print(sum_of_list)
#

# import sys
# input_data = sys.stdin.read()
# print(input_data)

# result = input()
# diagnos = "Ekki veikur!"
# for n in range(0, len(result) - 1):
#     if result[n] == "C" and result[n + 1] == "O" and result[n + 2] == "V":
#         diagnos = "Veikur!"
#
# print(diagnos)

# text = input()
# times = input()
# print(text * int(times))

# n = int(input())
# dic_list = {}
# for b in range(n):
#     x = input().split()
#     if x[0] not in dic_list:
#         dic_list[x[0]] = 0
#     dic_list[x[0]] += int(x[1])
#
# biggest = 0
# key2 = ""
# for key,value in dic_list.items():
#     if dic_list[key] > biggest:
#         biggest = dic_list[key]
#         key2 = key
#
# print(key2)

# list1 = [1,3,5,7]
# list2 = [8,10,12]
# month = int(input())
# if month in list1 or month in list2:
#     print(31)

# guests_amount = int(input())
# list_dic = {}
# for n in range(guests_amount):
#     x = input().split()
#     list_dic[x[0]] = int(x[1])
# default_value = 0
# key1 = ""
# for key, value in list_dic.items():
#     if value > default_value:
#         default_value = value
#         key1 = key
#     # print(key)
#     # print(value)
#
# print(key1)
#___________________________________________________________________________
# data = input().split()
#
# data2 = []
# for n in data:
#     data2.append(int(n))
# print(data2[0]*data2[2]+0.5*data2[1]*(data2[2]*data2[2]))
#____________________________________________________________________________

# reversed_str = input()
# normal_str = reversed_str[::-1]
# print(normal_str)

#________________________________________________________________________________

# import sys
#
# for line in sys.stdin:
# 	if 'q' == line.rstrip():
# 		break
# 	print(f'Input : {line}')
#
# print("Exit")
#______________________________________________________________________________________________________
# import random
#
# def randomizer(sides):
# 	return random.randint(0, sides)
# i = input()
# dices = i.split()
# new_dices = []
# for n in dices:
# 	new_dices.append(int(n))
#
# sum_dics = 0
#
# for n in range(new_dices[1]):
# 	sum_dics += randomizer(new_dices[0])
# print(sum_dics)

#________________________________________________________________________________________________________________
#
# list1 = []
# for _ in range(3):
#     list1.append(int(input()))
# minimum = min(list1)
# if minimum == list1[0]:
#     print("Monnei")
# elif minimum == list1[1]:
#     print("Fjee")
# else:
#     print(" Dolladollabilljoll")
#__________________________________________________________________________________________________________________
# first = int(input())
# second = int(input())
# multi_list = [[(x+1)+(y+1) for x in range(first)] for y in range(second)]
# max_value = first+second
# dic_list = {}
# count = 1
# for x in range(second):
# 	for y in range(first):
# 		if multi_list[x][y] not in dic_list:
# 			dic_list[f"{multi_list[x][y]}"] = 0
#
# for x in range(second):
# 	for y in range(first):
# 		for key, value in dic_list.items():
# 			if multi_list[x][y] == int(key):
# 				dic_list[key] += 1
#
# # list1 = [v for k, v in dic_list.items() if v == max(dic_list, key=dic_list.get)]
# print(dic_list)
# print(max(dic_list, key=dic_list.get))
# for n in
#______________________________________________________________________________________________________________

# text = input()
# new_str = ""
# for n in text:
#     if n.isupper():
#         new_str = new_str + n
#     else:
#         pass
# print(new_str)
#________________________________________________________________________________________________________________
# line = input().replace(" ", '')
# x = 1
# for n in line:
#     x = x * int(n)
# print(x)
#_______________________________________________________________________________________________________________________

# dic = {"one": 0}
# ch = "one"
# dic[ch] += 1
# print(dic[ch])
#________________________________________________________________________________________________________________________#
# amount = int(input())
# lines = -1
# total = 0
# for _ in range(amount):
#     lines +=1
#     total +=int(input())
#
# print(total - lines)

#_________________________________________________________________________________________________________
# word = input()
# printed_word = ""
# for _ in range(3):
#     printed_word += f" {word}"
# print(printed_word)
#____________________________________________________________________________________
# input_seq = input().split()
# print(int(input_seq[0])+int(input_seq[1]))

#_________________________________________________________________________________________________________
# import random
# import string
#
# #symbol = ''.join(random.choices(string.ascii_letters, k=7))
# symbol = random.choices(string.ascii_letters, k=7)
# #  res = ''.join(random.choices(string.ascii_letters, k=7))
# print(str(symbol))
#_________________________________________________________________________________________________________
import pyperclip
pyperclip.copy("Example Text")
pyperclip.past()