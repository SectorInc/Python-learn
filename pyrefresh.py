# #  FUNCTIONS

# #1)Pythogras Theorem
# a=int(input("Enter height : "))
# b=int(input("Enter width : "))
# py=(pow(a,2) + b ** 2) **(0.5)
# print(round(py,2)) 



# #2) Area of a Right-Angled Triangle
# base=int(input("Enter triangle base : "))
# height=int(input("Enter triangle height : "))
# triangle_area=base * height/2
# print(triangle_area)

# #3) Checking for a Pythagorean Triple
# a=int(input("Enter height : "))
# b=int(input("Enter width : "))
# c=int(input("Enter pythogras : "))
# if pow(a,2) + pow(b,2) == pow(c,2):
#     print(True)
# else:
#     print(False)

# #4)Distance Between Two 2D Points
# x1=int(input("Enter distance : "))
# x2=int(input("Enter distance : ")) 
# cal_distanceX=x2-x1
# print(cal_distanceX)
# y1=int(input("Enter distance : "))
# y2=int(input("Enter distance : "))
# cal_distanceY=y2-y1
# print(cal_distanceY)
# Distance=pow(cal_distanceX,2) + pow(cal_distanceY,2)
# print(Distance)
# Distance=pow(Distance,0.5)
# print(Distance)


#CONTAINERS(tuples,lists,sets,dictionaries)

# tuple=(2,21,2,'a')
# set={1,2,3,4} 
# list=[1,2,3,'a',1]
# dict={'key':'value', '123':[1,2,3]}
#to add new value to dict
#new_dict={'key':'value', '123':[1,2,3]}
#new_dict['goat']=['messi']
#print(new_dict)
#to get values from list using index
#new_list=[1,2,3,4,5,6,7,8,9,10]
#print(new_list[2:9:2]) #first value is start value, reperesnting the index of the value to start from, 
                      #second is the stop value, representing the index after where the list stops,
                      #third is the step value, stating how many steps the list takes.
                      #these three steps are called list slicing
#to get valuyes in reverse
#new_list.reverse()
#print(new_list[2:9:2])
#or
#new_list=[1,2,3,4,5,6,7,8,9,10]
#print(new_list[7::-2])# if stop value is left empty, list continues till it reaches the lowest value available.

#1) Set Operations (De-duplication & Comparison)
# raw_guests=['Alice','Bob', 'Alice', 'Charile', 'Bob', 'David']
# print(set(raw_guests))#convert list to set
# vip_guests={'Alice', 'Eve'}
# #compare both sets
# print(vip_guests & set(raw_guests))#used only when both containers are sets
# #or
# print(vip_guests.intersection(raw_guests))#used when one is not a set      
# from collections import Counter
# #2) Word Frequency Counter (Dictionary + List)
# words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
# counts = Counter(words)
# print(counts)
# #or
# word_counts={}
# for word in words:
#    word_counts[word]=word_counts.get(word,0)+1
# print(word_counts)
# #to print only entries that appear more than once
# repeated_only={key:word_count for key, word_count in word_counts.items() if word_count >1}
# print(repeated_only)

# #3) Dictionary of Lists (Nested Data Retrieval)
# students = {
#     'Alice': [85,90,92],
#     'Bob': [78,81,85]
# }
# #to add new score to existing student
# students['Alice'].append(95)
# #to add new student
# students['Charile']=[88,92]
# print(students)
# #print alice second grade
# print(students['Alice'][1])

# #Functions + Tuples Exercises
# #Exercise 4: Function Returning Multiple Values (Tuples)
# def get_min_max(numbers):
#     max_val=max(numbers)
#     min_val=min(numbers)
#     return min_val, max_val 

# numbers=[]        

# lowest, highest=get_min_max([14, 2, 45, 8, 99])
# print(lowest)
# print(highest)
# # #get_min_max(numbers=[14, 2, 45, 8, 99])

# #5)Unpacking Tuples as Function Arguments

# def rectangle_properties(dimensions):
#     length,width = dimensions
#     area = length * width
#     perimeter = 2 * (length + width)
#     return area, perimeter
   
# rect_dim=rectangle_properties(10,5)
# area, perimeter = rectangle_properties(rect_dim)
# print(f"Area: {area}, Perimeter: {perimeter}")

#CONTROL FLOWS(loops,if,else, etc..)
# num=[1,2,3,4,5]
# x=0
# rep=0
# for x in num:
#     if x== 2:
#         print(" The value is 2")
#     else:
#         print(" The value is not 2")
# while rep==range(6):
#     print("last item")
#     rep+=1

#1) Filter Even and Odd Numbers
# odd_even= [12, 7, 19, 24, 3, 8, 15]
# evens=[] 
# odds=[]
# for x in odd_even:
#     if x % 2==0:
#         evens.append(x)
#     else:
#         odds.append(x)
# print(odds,evens)

# #2) Number Guessing Loop with break
# import random
# while True:
#     lucky_number=random.randint(1,7)
#     user_guess=int(input(" Guess the number between 1-7 : "))
#     if user_guess==lucky_number:
#         print(f"Correct!The lucky number was {lucky_number}")
#         break
#     else:
#         print(f"Opps.The lucky number was {lucky_number}. Try again.") 

# #3) Summing Values in a Dictionary using a Loop
# cart = {"apple": 1.50, "banana": 0.75, "milk": 2.50, "bread": 2.00}
# total_price = 0.0
# for price in cart.values():
#     total_price+=price# or total_price = sum(cart.values())
# print(f" Total bill: ${total_price}")

#collect two arguments(string andd interger)
#print the string the amout of time given by the interger argument
#i.e if interger is 5, string should print 5 times
def shouter(x_str='hey',y_num=4):
    counter=0
    if y_num <= 10:
        while counter < y_num:
            print(x_str.upper())
            counter+=1
#or
        #for i in range(y_num):
           #print(x_str.upper()) 
    else:
        print(' You are too loud')
    return('done')
result=shouter('Daniel',7)
print(result)

#1: E-Commerce Discount & Tax Calculator
prices = [12.00, 85.00, 45.00, 150.00, 8.50]
discount_price=[ 
        f"{(price* 0.91* 0.95):.2f}" 
        if price>50  
        else f"{(price * 0.95):.2f}"
         for price in prices
        ]
print(discount_price)

#Challenge 2: Log File Alert Filter
logs = [
    "INFO: Server started on port 8080",
    "WARNING: Disk usage high (85%)",
    "ERROR: Database connection failed",
    "INFO: User 102 logged in",
    "CRITICAL: System running out of memory"
]

filter_log=[log.upper() 
            for log in logs 
            if log.startswith("CRITICAL") or log.startswith("ERROR")]
print(filter_log)

#3Extracting Domain Names from Web URLs
urls = [
    "https://www.google.com/search?q=python",
    "http://github.com/repository",
    "https://www.youtube.com/watch?v=123",
    "https://wikipedia.org/wiki/Main_Page"
]

domain_name=[url.replace("https://","") 
            .replace("http://","") 
            .replace("www.","") 
            .split("/")[0] 
            for url in urls ]
print(domain_name)