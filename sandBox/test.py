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
import random

def randomizer(sides):
	return random.randint(0, sides)
i = input()
dices = i.split()
new_dices = []
for n in dices:
	new_dices.append(int(n))

sum_dics = 0

for n in range(new_dices[1]):
	sum_dics += randomizer(new_dices[0])
print(sum_dics)