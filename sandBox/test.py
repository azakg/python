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
# import pyperclip
# pyperclip.copy("Example Text")
# pyperclip.past()

#_________________________________________________________________________________________________________
#
# with open("file.txt", "w") as file:
#     file.write("some text")

# from tkinter import *
#
#
# window = Tk()
# window.title("Example")
# window.config(padx=50, pady=50, bg="green")
#
# canvas = Canvas(width=800)
#
#
# window.mainloop()
# #_________________________________________________________________________________________________________
# str1 = input()
# #print(len(str1))
# counter = 0
# new_str = ""
# go_on = True
# while go_on:
#     for i in str1:
#         if i =="a" and go_on:
#             for x in range(counter, 100):
#                 #print(f"{x}:{len(str1)}")
#                 if x >= len(str1):
#                     go_on = False
#                 else:
#                     new_str += str1[x]
#         counter += 1
#     else:
#         pass
# print(new_str)


# _________________________________________________________________________________________________________

# str1 = input()
#
# new_index = str1.find("a")
# print(new_index)
# print(str1[new_index:])
# _________________________________________________________________________________________________________

# text_str = 'https://nostarch.com'
# new_text_str = text_str.removeprefix("https://")
# print(new_text_str)

# _________________________________________________________________________________________________________
#
# fig_list = input().split()
# init_list = [1, 1, 2, 2, 2, 8]
# final_list = []
#
# for x in range(6):
#     if int(fig_list[x]) > init_list[x]:
#         final_list.append(-abs(int(fig_list[x]) - init_list[x]))
#     elif int(fig_list[x]) == init_list[x]:
#         final_list.append(0)
#     else:
#        final_list.append(init_list[x]-int(fig_list[x]))
# print(' '.join(str(e) for e in final_list))

# _________________________________________________________________________________________________________

# two_nums = input().split()
# if int(two_nums[0]) > int(two_nums[1]):
#     print(1)
# else:
#     print(0)

# _________________________________________________________________________________________________________

# email = input()
# print(email.replace(" ", ""))
# _________________________________________________________________________________________________________
# input_str = input()
# counter = 0
# for x in input_str:
#     if ord(x) in range(65, 91) or ord(x) in range(97, 123):
#         counter += 1
#     else:
#         pass
# print(counter)
# _________________________________________________________________________________________________________
# bin_num = bin(int(input()))
# reversed = [ x for x in bin_num[:1:-1]]
# unit = ''.join(reversed)
# print(int(unit,2))
# _________________________________________________________________________________________________________
# line1 = input().split()
# print((int(line1[1])*2)-int(line1[0]))

# _________________________________________________________________________________________________________
# iter = int(input())
# for _ in range(iter):
#     input_ints = [int(x) for x in input().split()]
#     if input_ints[1]-input_ints[2] > input_ints[0]:
#         print("advertise")
#     elif input_ints[1] - input_ints[2] == input_ints[0]:
#         print("does not matter")
#     else:
#         print("do not advertise")
# _________________________________________________________________________________________________________
# list1 = input()
# if "OCT 31" == list1 or "DEC 25" == list1:
#     print("yup")
# else:
#     print("nope")
# _________________________________________________________________________________________________________
# iter1 = int(input())
# default = 0
# incre = 0
# for x in range(iter1):
#     list1 = input().split()
#     for n in range(int(list1[1])):
#         default +=1
#         incre += n+1
#     print(f"{x+1} {default+incre}")
#     default = 0
#     incre = 0
# _________________________________________________________________________________________________________

# import math
# iter1 = int(input())
# for _ in range(iter1):
#     n = int(input())
#     print(math.factorial(n)%10)
# _________________________________________________________________________________________________________

# greating = input()
# counter = 0
# for x in greating:
#     if x == "e":
#         counter +=1
# list1 = ['e' for _ in range(counter*2)]
# print(f"h{''.join(list1)}y")
# _________________________________________________________________________________________________________
# phone_n = input()
# if phone_n[:3] == "555":
#     print(1)
# else:
#     print(0)

# _________________________________________________________________________________________________________
# two_ints = input().split()
# p_n = int(two_ints[0]) + int(two_ints[1])
# print(p_n)
# _________________________________________________________________________________________________________
# first_input = input().split()
# go_on = True
# while go_on:
#     first_input = input().split()
#     second_input = input().split()
#     if first_input[0] == "0":
#         go_on = False
#     if int(first_input[0]) ==
#
#
# """
# 1 + 2
# length + width + 3 + depth
# length = 3
# length + width + 3 + depth
# width = 7
# length + width + 3 + depth
# depth = 2
# length + width + 3 + depth
# depth = 1
# length + width + 3 + depth
# computercost + televisioncost
# 0
# """
# _________________________________________________________________________________________________________
# input_s = list(map(int, input().split()))
# input_s.sort()
# print(*input_s)


# _________________________________________________________________________________________________________
# iter_n = int(input())
# list_of_int = list(map(int, input().split()))
# print(sum(list_of_int))
# _________________________________________________________________________________________________________
# list_of_int = list(map(int, input().split()))
# result = (list_of_int[0] * list_of_int[1])*0.5
# print(result)
# _________________________________________________________________________________________________________
# a, b, c = map(int, input().split())
# if a + b == c:
#     print("correct!")
# else:
#     print("wrong!")

# _________________________________________________________________________________________________________
# nothing = int(input())
# list_of_int = list(map(int, input().split()))
# print(f"{int(sum(list_of_int)/nothing)}")

# _________________________________________________________________________________________________________
# without_y = "aeiouAEIOU"
# with_y = "aeiouyAEIOUY"
# counter_y = 0
# counter = 0
# input_str = input()
# for l in input_str:
#     if l in without_y:
#         counter +=1
#     else:
#         counter_y +=1
# print(f"{counter} {counter_y}")

# _________________________________________________________________________________________________________
# iter1 = int(input())
# list1 = []
# for _ in range(iter1):
#     list1.append(input())
#
# for x in range(len(list1)):
#     if x%2 == 0:
#         print(list1[x])
# _________________________________________________________________________________________________________
# iter1 = int(input())
# items_list = ["keys", "phone", "wallet"]
# new_items_list = []
# print_list = []
# for _ in range(iter1):
#     new_items_list.append(input())
#
# for x in items_list:
#     if x in new_items_list:
#         pass
#     else:
#         print_list.append(x)
# if len(print_list) == 0:
#     print('ready')
# else:
#     for x in print_list:
#         print(x)
# _________________________________________________________________________________________________________
# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
        # for x in range(len(nums)):
        #     if val == nums[x]:
        #         nums.pop(x)
        #         nums.append("_")
        # print(f"{len(nums)}, nums = {nums}")
        # return len(nums)
        # k = 0
#         for i in range(len(nums)):
#             if (nums[i] != val):
#                 nums[k] = nums[i]
#                 k += 1
#         return k
# obj = Solution()
# obj.removeElement([3,2,2,3], 3)
# _________________________________________________________________________________________________________
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         initial_str = strs[0]
#         for x in strs:
#             while not x.startswith(initial_str):
#                 initial_str = initial_str[:-1]
#         if initial_str == "":
#             print("There is no common prefix among the input")
#         else:
#             print(initial_str)
# strs = ["flower","flow","flight"]
# strs1 = ["dog","racecar","car"]
# obj = Solution()
# obj.longestCommonPrefix(strs)
#
# print(Solution.longestCommonPrefix(strs))
# _________________________________________________________________________________________________________
# diff = int(input())
# WM = input()
# WM_dic ={}
# for x in WM:
#     WM_dic[x]=0
# result_num = 0
#
# for i in WM:
#     if abs(WM_dic["W"] - WM_dic["M"]) > diff:
#         if i == "W":
#             WM_dic[i] -=1
#             result_num +=1
#         elif i == "M":
#             WM_dic[i] -=1
#             result_num +=1
# print(result_num)
# for i in WM:
#     if abs(WM_dic["W"] - WM_dic["M"]) <= diff:
#         if i == "W":
#             WM_dic[i] +=1
#             result_num +=1
#         elif i == "M":
#             WM_dic[i] +=1
#             result_num +=1
# print(result_num)
# go_on = True
# result_num = len(WM)
# while go_on:
#     if abs(WM_dic["W"] - WM_dic["M"]) > diff:
#         result_num -=1
#     else:
#         print(result_num)
#         go_on = False

# sub_result = abs(WM_dic["W"] - WM_dic["M"])
#
# if sub_result == 0:
#     print(WM_dic["W"])
# else:
#     print(len(WM) - sub_result)

# _________________________________________________________________________________________________________
# num1 = int(input())
# line1 = [x for x in input()]
# num_of_M = 0
# num_of_W = 0
# for x in line1:
#     if x == "M":
#         num_of_M +=1
#     else:
#         num_of_W +=1
# go_on =True
# new_line = []
# i = 0
# while go_on:
#     new_line.append(line1[i])
#     if
# _________________________________________________________________________________________________________
# list1 = [2,3,4]
# list2 = [5,6,4]
# list1R = int(''.join([str(i) for i in list1[::-1]]))
# list2R = int(''.join([str(i) for i in list2[::-1]]))









# _________________________________________________________________________________________________________
# number = eval(input("Type number: "))
# print(type(number))
# print(number)
# # _________________________________________________________________________________________________________
# def Calculate(n):
#     x = 0
#     y = 0
#     for a in range(4, 10):
#         x = a
#         for b in range(1, 10):
#             y = b
#             middle_result = ((b**2)+(a**2))**0.5
#             z = float("{:.2f}".format(middle_result))
#             if z == float(n):
#                 print(x)
#                 return x, y
#
# radius = int(input())
# x, y = Calculate(radius)
# if x is not None and y is not None:
#     print(f"x = {x}, y = {y}")
# else:
#     print("Not found")

# print(((x**2)+(y**2))**0.5)
# _________________________________________________________________________________________________________
# print(len(input()))
# _________________________________________________________________________________________________________
# improvements = int(input())
# improvements_year = int(input())
# print(int((improvements/improvements_year)+2022))
# _________________________________________________________________________________________________________
# lines_num = int(input())
# names_list = []
# for _ in range(lines_num):
#     names_list.append(input())
# for n in names_list:
#     print(f"Takk {n}")
# _________________________________________________________________________________________________________
# line = input().replace(" ", "")
# print(int((int(line[0])*int(line[1])/2)))

# _________________________________________________________________________________________________________
# line = input().replace(" ", "")
# print(int(line[0])+int(line[1]))
# _________________________________________________________________________________________________________
# input_str = input()
# go_on = True
# counter = 0
# while go_on:
#     if input_str[counter] != "a":
#         counter +=1
#     else:
#         go_on = False
# print(input_str[counter::])


# _________________________________________________________________________________________________________
# int_str = input().replace(" ", "")
# if int(int_str[0]) > int(int_str[1]):
#     print(1)
# else:
#     print(0)
# _________________________________________________________________________________________________________
# print(int(((int(input())+5)*3)-10))

# _________________________________________________________________________________________________________
# print(input().replace(" ", ""))
# _________________________________________________________________________________________________________
# input_str = input()
# k = 0
# b = 0
# for c in input_str:
#     if c == "k":
#         k +=1
#     elif c == "b":
#         b +=1
# if k > b:
#     print("kiki")
# elif k < b:
#     print("boba")
# elif k != 0 and k == b:
#     print("boki")
# else:
#     print("none")
# _________________________________________________________________________________________________________
# month = int(input())
# full = [1,3,5,7,8,10,12]
# not_full = [4,6,9,11]
# if month in full:
#     print(31)
# elif month in not_full:
#     print(30)
# else:
#     print(28)
# _________________________________________________________________________________________________________
# num_str = input().split()
# v = int(num_str[0])
# a = int(num_str[1])
# t = int(num_str[2])
# print((v*t)+((0.5*a)*(t*t)))

# _________________________________________________________________________________________________________
# number = int(input())
# list1 = []
# for _ in range(number):
#     list1.append(input())
# for w in list1[::2]:
#     print(w)
# _________________________________________________________________________________________________________
figures_list = input().split()
right_list = [1,1,2,2,2,8]
correct
for f in right_list:
    if
# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

# _________________________________________________________________________________________________________
