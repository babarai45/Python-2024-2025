# # Question 1:-
# # # Write a function that takes two integers and returns their sum as a complex number.
# a=20
# b=10
# print("Ans-1: sum as complex numbers ",complex(a,b))
# #------------------- value by user input 
# # 
# user_1=int(input("Enter first number: "))
# user_2=int(input("Enter second number: "))
# def sum_of_complex(v1,v2):
#     return  complex(v1,v2)
# result=sum_of_complex(user_1,user_2)
# print("By taking user value with simple-function :",result)
hight
# # using function  lambda
# result= lambda x,y :complex(x,y)
# print("using lambda function :",result(user_1,user_2))

#---------------------------------------------------------


# Question 2:-

# # Implement a program that prompts the user to enter a
#  sequence of numbers (integers and floats) and calculates 
# the sum of all even numbers and the product of all odd numbers.


# # -----simple Me
# user_input=input("Eenter asequence of numbers (integers and floats)").split(',')
# print(user_input)
# sum_of_even_number=0
# pro_of_odd_number=1
# for i in user_input:
#     num=float(i)
#     if num % 2==0:
#         sum_of_even_number+=num
#     else:
#         pro_of_odd_number*=num
# print(f'sum of all even numbers is :{sum_of_even_number}')
# print(f'product of all odd numbers is :{pro_of_odd_number}')

# #-----------------------Method Function:-
# def sum_even_and_product_odd_number():
#     sum_of_even_number=0
#     pro_of_odd_number=1
#     user_input=input("Eenter asequence of numbers (integers and floats)").split(',')
#     for i in user_input:
#         num=float(i)
#         if num%2==0:
#             sum_of_even_number += num
#         else:
#             pro_of_odd_number *=num
#     return f'sum of even number is {sum_of_even_number}\nproduct of odd number is {pro_of_odd_number}'
# result=sum_even_and_product_odd_number()
# print(result)

#------------------- Using list comprehension and ternaly operters  
# def sum_even_and_product_odd_number():
#     user_input=input("Eenter asequence of numbers (integers and floats)").split(',')
#     sum_of_even_number=sum([float(i) for i in user_input if float(i)%2==0])
#     pro_of_odd_number=1
#     for i in user_input:
#         pro_of_odd_number *=float(i) if float(i)%2!=0 else 1
#     return f'sum of even number is {sum_of_even_number}\nproduct of odd number is {pro_of_odd_number}'
# result=sum_even_and_product_odd_number()
# print(result)

#------------------- Using list comprehension and ternaly operters and lambda function
# sum_even_and_product_odd_number=lambda user_input: (sum([float(i) for i in user_input if float(i)%2==0]),1 if float(i)%2!=0 else float(i) for i in user_input)
# result=sum_even_and_product_odd_number(input("Eenter asequence of numbers (integers and floats)").split(','))
# print(f'sum of even number is {result[0]}\nproduct of odd number is {result[1]}')

#---------------------------------------------------------


# Question 3:-

# Create a program that prompts the user to enter a string and converts it to a float if possible, or prints an error message if the string cannot be converted.

# simple 
# user_input=input("Enter a string: ")
# try:
#     print(float(user_input))
# except ValueError as e:
#     print("Error:",e)
# finally:
#     print("Thanks for using the program")

#---------------------------

# Question 4:-
# Write a function that takes two integers and returns their product,
# but returns the keyword None if either input is negative.
#sol-1
# int1=int(input("Enter first  integer  "))
# int2=int(input("Enter  second integer  "))
# def product_of_two_interer(x,y):
#     if x>=0 and y>=0:
#         return x*y
#     else:
#         return None
# result=product_of_two_interer(int1,int2)
# print(result)

# #sol-2 using lambda 
# result=lambda x,y : (x*y if x>=0 and y>=0 else None)
# print(result(int1,int2)) 

#-------------------------------------

# Question 5:-

# Implement a program that takes a list of complex numbers and
# returns a new list with only the imaginary parts of those complex numbers.

# user_input = input("Enter list of complex numbers ").split(',')
# print(user_input)
# print(user_input[-1:][-1][-2:])
# new_list=[]
# for com in user_input:
#     img=com.split('+')
#     new_list.append(img[-1])
# print(user_input)
# print(new_list)

#----------------Using Function
# new_list=[]
# def split_complex(x):
#     for i in x:
#         img=i.split('+')
#         new_list.append(img[-1])
# result=split_complex(user_input)
# print(new_list)
#____________________________________
# new_list=[]
# def com(x):
#     for i in x:
#         new_list.append(( i.split('+')[-1]))
# result=com(user_input)
# print(new_list)

#-----------------Using List comprehensive 
# result=[i.split('+')[-1] for i in user_input ]
# print(result)
#------------------using map
# result=map(lambda x:x.split('+')[-1] ,user_input)
# print(list(result))

#_________________________________________________________

# Question 4:-
# Create a function that takes a boolean expression as a string
# (e.g., "True and False or not (True)") and evaluates it, returning the result as a boolean.


# user_input=input("Enter a boolean expression as a string: ") 
# print(eval(user_input))

#-------------------Using Function
# def boolean_expression(x):
#     return eval(x)
# result=boolean_expression(user_input)
# print(result)

#___________________using lamda 
# result=lambda x: eval(x) 
# print(result(user_input))


#____________________________________________Question 6:- _________________________#

# Write a program that prompts the user to enter a sequence of integers and floats, and prints the sum 
# of all numbers that are greater than 10 and the product of all numbers that are less than or equal to 10.

#----------- using for loop
# user_input=input("Enter the Sequence of Integer or Flaot :-").split(' ')
# sum_greter_10=0
# product_less_10=1
# for i in user_input:
#     num=float(i)
#     if num>10:
#         sum_greter_10+=num
#     elif num<=10:
#         product_less_10*=num
# print(sum_greter_10)
# print(product_less_10)

#-----------------Using Function
# def sum_and_product(x):
#     sum_greter_10=0
#     product_less_10=1
#     for i in x:
#         num=float(i)
#         if num>10:
#             sum_greter_10+=num
#         elif num<=10:
#             product_less_10*=num
#     return f'sum_greter_10 is {sum_greter_10}\n and sum of prdict less than 10 is  {product_less_10}'
# result=sum_and_product(user_input)
# print(result)

# --------------------------- using lamda function 

user_input = input("Enter the Sequence of Integer or Float: ").split(' ')
result = lambda x: [sum(float(i) for i in x if float(i) > 10),eval('*'.join(str(float(i)) for i in x if float(i) <= 10))]
print(result(user_input))
