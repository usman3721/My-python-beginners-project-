 # #print("hello"+" "+ "Usman")
#the input fuction will be executed b4 hello and giving answer to the input funtion replaces the input function in execution
#print(len(input('what is you name? ')))
# name =input('what is you name? ')
# print(len(name))
# print("Hello"+ " "+ name)
#num=len(input('what is your name?'))
#print(num)

# num=input("type a two digits numbber ")
# firstNum=num[0]
# secondNum=num[1]
# thirdNum=num[2]
# result=firstNum+secondNum+thirdNum
# print(result)

#crating a bmi calculator
# weight=input('please enter your weight  kg')
# height=input('please enter your height in m')
# bmi=int(weight)/float(height)**2.0
# if bmi <18.5:
#     print('You are underweight')
# elif bmi < 25:
#     print('You are of normal weight')
# elif bmi <30:
#     print('Youare overweighted')
# elif bmi <35:
#     print( 'You are obesed')
# elif bmi==35:
#     print('You are clinnically obesed')
# else:
#     print('you weight is not known')

# # print(int(bmi_calculation))

# print('Welcome to rollercoaster!')
# height=int(input('What is your height in cm? '))
# bill=0
#age = int(input('What is your age? '))

# if height>=120:
#     print("You can ride on the roller coaste")
#     age = int(input('What is your age? '))
#     if age < 12:
#         bill=5
#         print('please apy $5')
#     elif age <=18:
#         bill= 7
#         print("please pay $7")
#     elif age >=45 or age <=55:
#         bill=0
#         print( "Everything is going fine.Have afree ride on us")
#     else:
#         bill=12
#         print('You are an adult, please pay $12.')
#     cupOfTea=input('Do you want a cup of tea.lower(Yes or No)?. ')
#     if cupOfTea=="Yes"or"yes":
#         total_bill=bill + 3
#         print(f"Your total bill is ${total_bill}")
#         print("Thanks for visiting our store")
# else:
   
#     print("Sorry you can't ride on the rollercoaster, You need to grow taller")
#     print("Thanks for visiting our store")

# number=int(input("Write a number of your choice! "))
# if number%2==0:
#     print('You have gotten an even number')

# else:
#     print("You have an odd number")

# print('Welcome to a leap year detection project')
# year=int(input('please enter the year to be tested! '))
# if year%4==0:
#     print("it's a leap year")
#     if year%100 == 0:
#         print("it's a leap year")
#     else: 
#         print('its not a leap year')
#         if year% 400==0:
#             print("it's a leap year")
#         else:
#             print('Not a leap year')
# else:
#     print('Not a leap year')

# print('Welcome to a leap year detection project')
# year=int(input('please enter the year to be tested! '))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("leap year")
#         else:
#             print('Not aleap year')
#     else:
#         print('laep year')
# else:
#     print('Not a leap year')

# print("Welcome to Python Pizza Deliveries!")
# size=input("what size of pizza do you want? S or L or M?")
# pepperroni=input("Would you like to add pepperoni? Y or No")
# # extra_cheese=input('Would you like to add an extra cheese? Y or N')
# bill=0
# if size=="S":
#     # bill=15
#     if pepperroni== "Y":
#         tBill=bill+2
#         print(f"You will paa{tBill}")
# else:
#     print("jkdsbj")
# elif size=="M":
#     bill=20
#     print("You will pay $20")
# elif size=="L":
#     bill=25
#     print("ypu will pay $25")
#     if pepperroni== "Y":
#         tBill=bill+2
#         print(f"You will paa{tBill}")
#         if pepperroni=="Y":
#            tBill=bill+3
#         print(f"You will pay {tBill}")
# if extra_cheese=="Y":
#     tBill=bill+1
#     print(f"You will pay {tBill}")
# else:
#     print("We do not have this type of python pizza")
#     print("Thank for visiting our store")


# print("Welcome to Python Pizza Deliveries!")
# size=input("what size of pizza do you want? S,L,M?")
# pepperroni=input("Would you like to add pepperoni? Y or No")
# extra_cheese=input('Would you like to add an extra cheese? Y or N') 
# bill= 0
# if size=="S":
#     bill+=15
# elif size=="M":
#     bill+=20
# elif:
#     bill+=25
# if pepperroni=="Y":
#     if size=="S":
#         bill+=2
#     else:
#         bill+=3
# if extra_cheese== "Y":
#     bill+=1
# print(f"Your total apy is ${bill}")

# if extra_cheese=="Y":
#     bill+=1
# else:
#     bill
    
#print(f"Your total apy is ${bill}")
# else:
#     print("tank 4 visisting our store")

# if pepperroni=="Y":
#     if size=="S":
#         bill+=2
#     else:
#         bill+=3
# if extra_cheese=="Y":
#     bill+=1
# print(F"Your final bill is${bill}")

# name1=input('what is your name?\n')
# name2=input("what is your name?\n")
# combined_name=name1 + name2
# combined_name.lower()
# t=combined_name.count("t")
# r=combined_name.count("r")
# u=combined_name.count("u")
# e=combined_name.count("e")
# true=t+r+u+e
# l=combined_name.count("l")
# o=combined_name.count("o")
# v=combined_name.count("v")
# e=combined_name.count("e")
# love=l+o+v+e
# love_score=int(str(true)+str(love)) # replacing the position of the two varable changes the result
# #print(love_score)
# if love_score<10 or love_score>90:
#     print(f"Your score is {love_score},")
# elif love_score>40 and love_score<50:
#     print(f"Your score is {love_score}")
# else:
#     print(f"Your score is {love_score}")

#PASSWORD GENERATOR
# import random
# letter="QWEERTTYUIOPLKJHGFDSAZXCVBNM"
# numbers="0123456789"
# symbols="{}()/.,?><;'\][]"
# all=letter+numbers+symbols
# print(all)
# lenght=8
# password="".join(random.sample(all,lenght))
# print(password)        



# import random
# import my_modeule

# Another to do for executing the love calculator
# import random
# num=random.randint(1,100)
# print(num)

# Head=1
# Tail=0

# random_figure=random.randint(0,1)
# if random_figure==1:
#     print("You have tossed a Head")
# else:
#     print("You have tossed a Tail")


# import random
# name_string=input("Give me the evrybody's name seprated by commas! ")
# name=name_string.split(", ") #This can be used to generate lisst by inputtung a string
# # nums_item=len(name)
# # random_choice=random.randint(0,(nums_item-1))
# # personToPayTheBill=name[random_choice]
# personToPayTheBill=random.choice(name)
# print(personToPayTheBill+ " is to pay the bill")





# row1=["⬜","⬜","⬜"]
# row2=["⬜","⬜","⬜"]
# row3=["⬜","⬜","⬜"]
# map=[row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}\n")
# position=input("Please enter the postion? ")
# horizontal=int(position[0])
# vertical=int(position[1])
# selected_row=map[vertical-1] #
# selected_row[horizontal-1]="*"
# print(f"{row1}\n{row2}\n{row3}\n")


# student_height=[23, 54, 546, 647, 54]
# print(max(student_height))


# lenght=len(student_height)
# sum=sum(student_height)
# average=sum/lenght
# print(round(average))


# total_height=0
# for height in student_height:
#     total_height += height
# print(total_height)


# human_score=0
# for score in student_height:
#     if score>human_score:
#       human_score=score
# print(human_score)


# total=0
# for score in range(2,101,2):
#   total+=score
# print(total)

# total=0
# for i in range(1,100):
#     if i%2==0:
#         total+=i
#     print(sum(total))

# print("Welcome Fizzbuss game")
# for num in range(1,101):
#     if num%3==0 and num%5==0:
#         print("Fizzbuzz")
#     elif num%3==0:
#         print("Fizz")
#     elif num%5==0:
#         print("Buzz")
#     # elif num%3==0 and num%5==0:
#     #     print("Fizzbuzz")
#     else:
#         print(num)

# def great(name):
#     print(f"hello fatai{name}")
#     print(f"usman hassan {name}")
#     print(f"going ahmad {name}")
# great("usman")


# import math
# test_h=int(input("please enter the hight of the building"))
# test_w=int(input("please enter the width of the building"))
# cover=int(input("please enter the input"))

# def  num_of_can(height,width,coverage):
#     the_calculation=height*width/coverage
#     print(f"You will need  {math.ceil(the_calculation)} cans of paint")
# num_of_can(height=test_h, width=test_w,coverage=cover)


# n=int(input("PLease enter a number"))
# def prime_checker(number):
#     for i in range(2,number):
#         is_prime=True
#         if number%i==0:
#             is_prime=False
#     if is_prime:
#         print("it is a prime number")
#     else:
#         print("it is not a prime number")
# prime_checker(number=n)




# student_score={
#     "usman":99,
#     "Yusuf": 89,
#     "Abdul fatai":84
# }
# student_grade={}
# for key in student_score:
#     score=student_score[key]
#     if score>90:
#         student_grade[key]="Outstanding"
#     elif score>80:
#         student_grade[key]="Exceed expectation"
#     elif score>70:
#         student_grade[key]="Acceptable"
#     else:
#         student_grade[key]="Fail"
# print(student_grade)


# capital={
#     "lagos": ["ikeja", "alagbado", "Alimosho", "casso"],
#     "fct":["Abuja","none"]
# }
# print(capital)


# nesting list inside dictionary and dictionary inside dictionary
# travel_log={
#     "cities":{"cities_visited":["Alimosho", "casso", "alagbado"], "total":34},   
# }
# print(travel_log)

# #nesting dictionary in a list
# travel_log= [
#     {
#     "country":"cities",
#     "cities_visited":["Alimosho", "casso", "alagbado"],
#     "total":34
#     },
#     {
#     "country":"Germany",
#     "visit":5,
#     "cities":["Berlin", "hamburg","stuttgart"]
#     }    
# ]


# def add_new_country(country_visited, times, cities_visited):
#     new_counrty={}
#     new_counrty["country"]=country_visited
#     new_counrty["visit"]=times
#     new_counrty["cities"]=cities_visited
#     travel_log.append(new_counrty)
# add_new_country("Russia",2,["Moscow", "saint Petersbrug"])
# print(travel_log)




# def formatted_name(f_name,l_name):
#     """  DOCSTRING retuلاrn the formatted string in a pascal case version."""
   
#     formatted_f_name=print(f_name.title())
#     formatted_l_name=print(l_name.title())
#     return f"{formatted_f_name}, {formatted_l_name}"
#     # print(f"{formatted_f_name} {formatted_l_name}")
   
# formatted_name()


# print('Welcome to a leap year detection project')
# year=int(input('please enter the year to be tested! '))
# def is_leap(year):
#     if year%4==0:
#         if year%100==0:
#             if year%400==0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
# def days_in_month(year,month):
#     if month>12 or month<1:
#         return "Invalid month"
#     month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
#     if is_leap(year) and month==2:
#         return 29
#     return month_days[month-1]

# year=int(input("Enter a year "))
# month=int(input("Enter a month "))
# days=days_in_month(year,month)
# print(days)


# enemies=1
# def increase_enemies():
#     global enemies # but instaed of this you follow the step line  439
#     print(f"Enemies inside funtion{enemies}")
#     return enemies+1
# # print(increase_enemies())
    
#     print(f"Enemies inside funtion{enemies}")
# increase_enemies()
# print(f"Enemies inside funtion{enemies}")