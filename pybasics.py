# num1,num2,num3 = input("enter the num1, num2, num3 ").split(",")
# print(f"average is {(int(num1)+int(num2)+int(num3))/3}")
# language  = "python" 

# print("language" [: :-2])
# name = input("enter your name : ")
# print(f"{name}"[-1: :-1])
# print(len("saurabh"))
# print("SUMMIT".lower())
# print("sumifhhdfshfjkt".count("j"))
# name , char = input("enter your name and char ").split(",")
# print(f"the length of your name is {len(name.strip())}")
# print(f"the count of char is {name.strip().lower().count(char.strip().lower())}")
# name = "she is beautiful and she is also a good dancer."
# Is_pos1 = name.find("is")
# Is_pos2 = name.find("is", Is_pos1 + 1) 
# print(Is_pos2)
# name = input("enter the name ")
# print(name.center(len(name) + 8, "*"))
# import random

# winning_number =random.randint(0,100)
# guess = 1
# game_over = False
# guess_number = int(input("guess the number:- "))
 
# while not game_over:   
# 	if guess_number == winning_number:
# 		print(f"You WIN!!!!!  \n you guess the number in {guess} times")
# 		game_over = True
# 	if guess_number < winning_number:
# 		print("too low")
# 		guess_number = int(input("guess again :- "))
# 		guess += 1
# 	if guess_number > winning_number:
# 		print("too high ")
# 		guess_number = int(input("guess again :- "))
# 		guess +=1 

# name= input("enter your name:- ")
# age = int(input("enter the age :- "))
# if (name[0] == "a" or name[0]=="A") and age >= 10:
#         print("you can watch movie.")
# else:
#         print("you cannot watch movie.")
# age = int(input("enter your age :- "))

# if age ==0 or age <0:
#     print("you cannot watch movie")
# elif 0<age<=3:
#     print("ticket is free.")
# elif 3<age<=15:
#     print("ticket price is:- 100")
# elif 15<age<=60:
#     print("ticket price is :- 250")
# else:
#     print("ticket price is:- 200")

# name = input("enter your name:- ")

# if name:
#     print(f"your name is {name}")
# else:
#     print("you didn\'t enter anything.")
# i = 1
# while i<=10:
#     print(f"hello world {i}")
#     i= i+1

# num = input("enter the number which ever you want to sum :- ")
# total = 0
# i = 0
# while i < len(num):
#     total += int(num[i])
#     i += 1
# print(total)

# name = input("enter your name:- ")
# temp_var = ""
# for i in range(len(name)):
#     if name[i] not in temp_var:
#         temp_var += name[i]
#         print(f"{name[i]} : {name.count(name[i])}") 
    

# num = input("enter the number:- ")
# total = 0
# for i in range(0,len(num)):
#     total += int(num[i])
# print(total)

# for i in range(0,11,2):
# 	print(i)

# function practice:-
# def char(name):  show output of last char of string.
# 	name = input("enter your name:- ")
# 	return name[-1]
# print(char("sumit"))
# def even(num):
# 	if num % 2 == 0:
# 		return "even no"
# 	else:
# 		print("odd no")

# num = int(input("enter the number"))
# print(even(num))
# def even(num):
# 	return num %2 ==0
# num = int(input("enter the number:- "))
# print(even(num))
# def great(a,b):
# 	if a>b:
# 		return a
# 	return b


# def greater(a,b,c):
# 	if a>c and a>b:
# 		return a
# 	elif  b>a and b>c:
# 		return b
# 	return c

# def new_greater(a, b, c):
# 	bigger = great(a,b)
# 	return great(bigger, c)

# print(new_greater(400,50,6))

#palindrome string
# def palindrome(name):
# 	name = input("enter the string:- ")
# 	str = name[::-1]

# 	if str == name:
# 		return "string is palindrome"
# 	return "string is not palindrome"

# print(palindrome(" "))
# fibonacci sequence 

# def fib(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     elif n ==2 :
#         print(a, b)
#     else:
#         print(a, b, end= " ")
#         for i in range(n-2):
#             c = a+b
#             a= b
#             b = c
#             print(b, end = " ")
# n  = int(input("enter the number:- "))
# fib(n)

# number = [1,2,3,4,5,6,7,8,9,10]

# def neg(l):
#     negative = []
#     for i in l:
#         negative.append(-i)
#     return negative

# print(neg(number))

# num = ['abc', 'ijk', 'xyz']

# def square(l):
#     sq = []
#     for i in range(len(l)):
#         sq.append(l[i][::-1])
#     return sq
# print(square(num))

# #with reverse function
# def rev(l):
#     l.reverse()
#     return l

# num = [1,2,3,4]
# print(rev(num))

# #with string slicing
# def rev(l):
#     return l[::-1]

# num = [1,2,3,4]
# print(rev(num))

# #with 
# def rev(l):
#     ele = []
#     for i in l:
#         ele.append(i[::-1])
#     return ele
# words = ['abc', 'cds','dsj']
# print(rev(words))

# def odd(l):
#     even = []
#     oddd = []
#     for i in l:
#         if i % 2 ==0:
#             even.append(i)
#         else:
#             oddd.append(i)
#     output = [oddd, even]
#     return output 
# num = list(range(1,11))
# print(odd(num))

# def common(a,b):
#     com = []
#     for i in a:
#         if i in b:
#             com.append(i)
#     return com 
# a = [2,3,7,8,4]
# b = [1,2,3,5,6]
# print(common(a,b))

# def m(l):
#     count = 0
#     for i in l:
#         if type(i) == list:
#             count += 1
#     return count
# a= [1,2,3 ,[1,2], [3,4]]
# print(m(a))

# Fruits =('mango', 'banana', 'grapes',  [4,5,6,7])
# # Fruits[3].pop()
# Fruits[3].append(567)
# print(Fruits)

# def tup(int1, int2):
#     add = int1 + int2
#     multiply = int1 * int2
#     return add, multiply
# print(tup(2,4))

num = tuple(range(1,11))
print(num)