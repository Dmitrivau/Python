import math
import random
import string

#x = float(input("Enter x"))
#z = float(input("Enter z"))
#w = float(input("Enter w"))
#a = float(input("Enter A"))
#b = float(input("Enter B"))
#c = float(input("Enter C"))
                    #Complex math expressions
#y = (x + 3) ** (5 * w) / (7 * (x-4))
#y = (3 * x ** 2 - x ** 3 / 4) ** (1/5)
#y = 7 * x / (2 * x + 4 * (x ** 2 + 4))
#h = 7 * x / (2 * x + 4 * (x * x + 4))
#y = x ** (x + 1) / (math.tan(2*w/3+5) - math.tan(x/2 + 1)) ** 3
#y = x ** x / (math.sin(2*w/3+5)-x) ** 2 + (math.sin(3*x)+w) ** (x+1) / math.sqrt(7*w)** (3/2)
#S = (a+b+c) / 2
#area = math.sqrt(S*(S-a)*(S-b)*(S-c))
#print("result: ", area)
#print("result: ", h)

                    #Quotient and remainder
    #60 sec in a minute, 3600 sec in a hour (60 * 60) 86400 sec in a day (3600 * 24)
#number = int(input("Enter number: "))
#number2 = int(input("Enter number: "))

#days,r = divmod(number, 86400)
#hours,r = divmod(r,3600)
#minutes,seconds = divmod(r,60)
#print(days, "days", hours, "hours")
#print(minutes, "minutes and seconds", seconds)


#“Write a Python program that prompts the user to enter a three-digit integer
#and then reverses it. For example, if the user enters the number 375, 
#the number 573 must be displayed.”

#number = int(input("Enter digits: "))
#digit3 = number % 10 #parempoolne
#r = number // 10
#digit2 = r % 10 #middle digit
#digit1 = r // 10 #leftmost digit
#reversed = digit3 * 100 + digit2 * 10 + digit1 * 1
#print(reversed)
#sum = digit3 * 100 + digit2 * 10 + digit1 * 1
#print(sum)


#n = int(input("Enter five digits"))
#digit5 = n % 10
#r = n // 10
#digit4 = r % 10
#r = r // 10
#digit3 = r % 10
#r = r // 10
#digit2 = r % 10
#digit1 = r // 10
#reversed = digit5 * 10000 + digit4 * 1000 + digit3 * 100 + digit2 * 10 + digit1 * 1
#print(digit5,digit4,digit3,digit2,digit1, r)
#print(reversed)


#n = int(input("Enter number:"))

#week 604800
#week, r = divmod(n,604800)
#day, r = divmod(r,86400)
#hour, r = divmod(r,3600)
#minute,second = divmod(r, 60)

#print(week,day,hour,minute,second)

#week = n// 604800
#r = n % 604800
#print(week, r)
#days = r // 86400
#r = r % 86400
#print(week,days, r)
#hour = r // 3600
#r = r % 3600
#print(week,days,hour, r)
#minutes = r // 60
#seconds = r % minutes
#print(week,days,hour,minutes,seconds)

#n = int(input("Enter amount: "))
#notes: 20,10,5,1
#twenty = n // 20
#r = n % 20 
#ten = r // 10
#r = r % 10
#five = r // 5
#one = r % 5

#print(twenty,ten,five,"one: ",one)


#1 mile = 63360 inches, 1 yard = 36 inches 1 foot = 12 inches
#n = int(input("Enter number of steps:"))

#miles = n // 63360
#r = n % 63360
#yard = r // 36
#r = r % 36
#foot = r // 12
#inches = r % 12
#print(miles,yard,foot, inches)


#a = "  Hello World   "
#b = "I am NEWBIE in Java. Java Rocks"
#c = b.replace("Java", "Python")
#i = b.find("Java")
#d = b.upper()
#e = b.lower()
#a = str(23)
#print(a)
#print(b,"Starts;",e,b[2].upper())
#print("HI" , len(a.strip()))

#name = "Dima"
#print(name[0:2])


#print(string.ascii_letters,string.hexdigits)


#s = input("Enter first and last name")
#space = s.find(" ")
#s_reversed = s[::-1]
#name1 = s[:space]
#name2 = s[space+1:]
#print(name1,name2)


#lastName = input("Enter last name: ")
#r = random.randrange(100,1000)
#print(lastName[:4].lower() + str(r))

#a = string.ascii_lowercase
#random_word = a[random.randrange(26)] + \
 #           a[random.randrange(26)] + \
 #           a[random.randrange(26)] + \
 #           a[random.randrange(26)] + \
 #           a[random.randrange(len(a))]


#print(random_word)

#n = int(input("Enter three digits"))
#s_n = str(n)

#d1,d2,d3 = s_n
#sum = int(d1) + int(d2) + int(d3)
#print(sum)

#name = input("Enter name: ")
#x = name.lower().replace(" ", "")
#s_pw = x[random.randrange(len(x))] + \
 #   x[random.randrange(len(x))] + \
  #  x[random.randrange(len(x))] + \
   # str(random.randrange(1000,10000))

#print(s_pw)

#n = str(input("enter integer"))
#s = print(n[::-1])

#a = float(input())
#b = float(input())
#print("Greatest value: ", max(a,b))


#a = int(input("Enter number: "))
#if a % 2 == 0:
#    print("Even")
#else:
#    print("Odd")


#team1 = input("Enter first team and score")
#team2 = input("Enter second team and score")

#team1_score = team1.find(" ")
#team2_score = team2.find(" ")

#if team1[team1_score:] > team2[team2_score:]:
 #   print("Winner is",team1, " points")
  #  print("Better luck next time", team2, " points")
#else:
 #   print("Winner is", team2)
  #  print("Better luck next time",team1)


#n = float(input("Enter number"))

#if n % 6 == 0 or n % 7 == 0:
 #   print(n, " is multiple of 6 or 7")
#else:
#    print(n, " is not multiply of either")

#n = int(input("Enter: "))

#if 1000 <= n <= 9999: #between saab nii kirjutada.
#    print("NN is the given number")
#else:
#    print("NN is not four-digit integer")


#a = int(input("First value"))
#b = int(input("Second value"))
#c = int(input("Third value"))

#if a < b + c and b < a + c and c < a + b:
#    print("Given numbers can be")
#else:
#    print("Cant")

#a = int(input("First value"))
#b = int(input("Second value"))
#c = int(input("Third value"))

#if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
#    print("All g")
#else:
#    print("not G")    

#pay_rate = float(input())
#hours_worked = float(input())

#if hours_worked <= 40:
#    gross_payt = pay_rate * hours_worked
#else:
#    gross_pay = pay_rate * 40 + 2 * pay_rate * (hours_worked - 40)

#net_pay = 0.7 * gross_pay
#print(net_pay)

#miles = float(input("Enter miles: "))

#r = miles % 12000

#if r > 6000:
#    miles_left = 12000 - r
#    print("Your car needs a major service in", miles_left, "miles")
#else:
#    miles_left = 6000 - r
#    print("Your car needs minor service in", miles_left, "miles")

#time1 = float(input("car A"))
#time2 = float(input("car B"))
#a1 = float(input("acceleration car A"))
#a2 = float(input("acceleration car B"))
#carA = 0.5 * a1 * time1 ** 2 
#carB = 0.5 * a2 * time2 ** 2
#print("distance between themis : ", abs(carA-carB),"meters")
#if carA > carB:
#    print("Car A is first")
#else:
#    print("Car B is first")

#x = int(input("Enter integer (0 - 999):"))

#if 0 <= x <= 9:
#    digits = 1
#elif 10 <= x <= 99:
#    digits = 2
#elif 100 <= x <= 999:
#    digits = 3
#else:
#    print("Wrong")

#print("A ", digits, "-digit integer entered", sep = "")


#a = int(input("Enter integer between -9999 and 9999"))

#if -9999 <= a <= -1000 or 1000 <= a <= 9999:
#    d = 4
#elif -999 <= a <= -100 or 100 <= a <= 999:
#    d = 3
#elif -99 <= a <= -10 or 10 <= a <= 99:
#    d = 2
#else:
#    d = 1

#print("You entered a", d , "-digit integer", sep = "")

#a = int(input())   
#a_str = str(abs(a))
#print("You entered a ", len(a_str), "-digit integer", sep = "")


#print("Convert USD to Euro")
#print("Convert USD to GBP")
#print("Convert USD to JPY")
#print("Convert USD to CAD")
#x = int(input("Enter 1,2,3,4"))
#amount = float(input("Enter amount: "))

#if x == 1:
#    converted = amount * 0.87
#    print("Converted ", amount, "USD to EUR. You now have", converted, " EUR", sep ="")

#x = int(input("Enter number between 1 and 12"))

#if x <= 2 or x == 12:
#    print("Winter")
#elif x <= 5:
#    print("Spring")
#elif x <= 8:
#    print("Summer")
#elif x < 12 and x > 8:
#    print("Fall(Autumn)") 
#else:
#    print("Wrong number")


#a = float(input())
#b = float(input())
#c = float(input())

#if a >= b + c or b >= a + c or c >= a + b:
#    print("Can be a triangle")
#else:
#    if a == b == c:
#        print("equilateral")
#    elif a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
#        print("right-angled")
#    else:
#        print("Not special")

#pin = int(input("Enter pin: "))
#count = 0

#if pin == 1234:
#    w = int(input("Enter amount to withdraw"))
#    a = w // 10
#    r = w % 10
#    b = r // 5
#    r = b // 1
#    print(a,"note(s) of 10$", b, "note(s) of 5$", r, " and 1 note(s) of 1$", sep = "")
#else:
#    if pin != "1234":
#        count += 1
#        pin = int(input("Wrong PIN. Try again "))
#        count += 1
#        pin = int(input("Wrong PIN. Try again "))
#        count += 1
#        if count == 3:
#           print("PIN locked")


#print("1. Convert gallons to liters")
#print("2. Convert liters to gallons")
#choice = int(input("Enter 1 or 2"))


#if choice not in [1,2]:
#    print("Wrong choice")
#else:
#    quantity = float(input("Enter quantitity"))
#    if quantity < 0:
#        print("invalid quantity")
#    else: 
#        if choice == 1:
#            liters = quantity * 3.785
#            print(quantity, " gallons converted to ", liters, "liters")
#        else:
#            gallons = quantity * 3.785
#            print(quantity, " liters converted to ", gallons, "gallons")



#total = 0

#i = 1
#while i <= 4:
#    x = float(input("Enter n"))
#    total = total + x

#    i += 1
#print(total)

#sum = 0

#n = int(input())

#i = 1
#while i <=n:
#    x = float(input())
#    sum += x
#    i += 1
#print(i,sum)


#p = 1

#i = 0
#while i <= 20:
#    x = float(input("enter products:"))
#    p = p * x
#    i += 1
#print(p)


#n = int(input("enter n"))
#sum = 0
#i = 1
#while i <= n:
#    x = int(input("enter n"))
#    sum += x
#    i += 1
#    avg = sum / i
#print(avg)

#p = 1
#x = float(input("n"))

#while x != 0:
#    p += x
#    x = float(input("Enter numbers:"))
#print(p)    

#i = 0
#even = 0
#odd = 0
#while True:
#   x = float(input("n:"))
#   if x % 2 == 0:
#      even += x
#   else:
#      odd += x
#   i += 1
#   if i >= 5: break
     
#print("Even: ", even, " Odd: ", odd)

#i = 0
#eg = 0
#sum = 0
#while True:
#    x = float(input("n:"))
#    if x < 0:
#        neg = x
#        print(x)
#    else:
#        sum += x
#    i += 1 
#    if i >= x: break
    
#print(sum)

#a = 11
#b = 0
#for i in range(a,b, -2):
#    print(i)



#n = int(input("n:"))

#for i in range(n+1):
#    print(i,math.sqrt(i))

#sum = 1
#counter = 0
#for i in range(5):
#    x = int(input("enter n:"))
#    if x > 0:
#        sum *= x
#        counter += 1
        
#if counter != 0:
#        print(sum / counter)
#else:
#     print("No numbers entered")

#m = input("Enter an English message")
#vowels = "AEIOU"
#count = 0
#for c in m:
#    if c.upper() in vowels:
#       count += 1
#print("Vowels", count)     


#n = int(input())

#sum = 0
#for i in range(n):
#    a = float(input("Enter number No" + str(i + 1) + ": "))
#    sum += a

#print("Sum: ", sum)

#word = "Zeus"
#i =1 
#s = ""
#for l in word:
#    s =s + i * l
#    print(s)
#    i += 1
#print(s)

#i = 0

#while i <= 360:
#    print(math.sin(i * math.pi/180))
#    i += 0.5


#n = int(input("N:"))
#count = 0
#for i in range(n):
#    x = int(input("enter numbers " + str(i + 1) + ": "))
#    if x % 2 == 0:
#        count += 1
#if count > 0:
#        print("even numbers entered: ", count)
#else:
#     print("You entered no even nr")


# even = 0
# dd = 0
# counterEven = 0
# counterOdd = 0
# for i in range(50):
#     x = float(input("numbers: " + str(i +1 ) + ": "))
#     if x % 2 == 0:
#         even += x
#         counterEven += 1

#     else:
#         odd += x
#         counterOdd
# if counterEven > 0:
#     print(even / counterEven)
# if counterOdd > 0:
#     print(odd / counterOdd)
        
# start = int(input("Enter start:"))
# finish = int(input("Enter finish:"))

# if start > finish:
#     c = start
#     start = finish
#     finish = c
# for i in range(start, finish + 1):
#     print(i)

# start = int(input("Enter start: "))
# finish = int(input("Enter finish: "))

# if start > finish:
#     c = start
#     start = finish
#     finish = c
# for i in range(start,finish + 1):
#     if i % 5 == 0:
#         print(i)

#   ------- PRE-TEST LOOP ---------
# x = 0
# while x <= 3:
#     print("*")
#     x += 1
# --------- POST-TEST LOOP --------
# x = 0
# while True:
#     print("x")
#     x += 1
#     if x <= 3: break

# print("\t\t", end = "")
# for i in range(1,5):
#     print(i, "\t", end = "")
# print()

# for i in range(1,5):
#     print("------------", end ="")
# print()

# for i in range(1,5):
#     print(i, "\t\t", end = "")
#     for j in range(1,5):
#         print(i * j, end = "\t")
#     print()

# n = int(input("Enter number"))
# print("\t\t", end = "")
# for i in range(1,n):
#     print(i, "\t", end = "")
# print()

# for i in range(1,n):
#     print("--------------", end ="")
# print()

# for i in range(1,n):
#     print(i, "\t\t", end ="")
#     for j in range(1,n):
#         print(i * j, end="\t")
#     print()


# words = []
# for i in range(5):
#     words.append(input())
# for word in words[::-1]:
#     print(word)

# numbers = []
# for i in range(3):
#     numbers.append(int(input("No:" + str(i + 1) + ": ")))
# for number in numbers[::-1]:
#     print(number)



# ELEMENTS = 5

# values = [None] * ELEMENTS
# for i in range(ELEMENTS):
#     values[i] = float(input())

# for value in values[::-1]:
#     if value > 0:
#         print(value)



# ELEMENTS = 8

# nums = [None] * ELEMENTS
# for i in range(ELEMENTS):
#     nums[i] = float(input("No" + str (i + 1) + ": "))

# for i in range(ELEMENTS):
#     if i % 2 != 0:
#         print(nums[i])
        

# E = 8

# values = [None] * E
# for i in range(E):
#     values[i] = float(input("No" + str (i + 1) + ": "))

# for value in values[1::2]: #start from 1 and increment by 2
#     print(value)

#OBJECTS

# person = {
#     "firstName": "Dima",
#     "lastName": "Jou",
#     "age": 20,
#     "height": 176
# }

# x = [1,2,3,4,5,6,7,9]

# if "firstName" in person:
#     print("I found dima")

# for key in person:
#     print(key,person[key])
    
# grades = [[None] * 3 for i in range(4)] #column * row
# print(grades)

# nums = [[1,3,4,5,6],
#         [3,6,7,3,5,5],
#         [1,5,3,6,8,9]
#         ]

# i = 1 # refers to Row 
# for j in range(6): #this loop control structure processes all elements of row 0
#     print(nums[i][j], end ="\t")
# print()

# j = 1 # refers to Column
# for i in range(3):
#     print(nums[i][j])

# ROWS = 3
# COLUMNS = 2

# names = [[None] * COLUMNS for i in range(ROWS)]

# for i in range(ROWS):
#     for j in range(COLUMNS):
#         names[i][j] = input("Enter for Row" + str(i) + ", Column " + str(j) + ": ")
# print(names)

#SQUARE MATRIX

# N = 2
# a = []
# for i in range(N):
#     a.append([])
#     for j in range(N):
#         a[i].append(float(input()))

# sum = 0
# for k in range(N):
#     sum += a[k][k]

# print("Sum = ", sum)


# N = 4
# a = [[None] * N for i in range(N)]
# for i in range(N):
#     for j in range(N):
#         a[i][j] = float(input())

# total = 0
# for i in range(N):
#     j = N - i - 1
#     total += a[i][j]

# print("Sum: ", total)

# N = 5
# a = [[None] * N for i in range(N)]
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             a[i][j] = -1
#         elif i > j:
#             a[i][j] = 10
#         else:
#             a[i][j] = 20

# for i in range(N):
#     for j in range(N):
#         print(a[i][j], end ="\t")
#     print()


#row to column
# sum = 0
# a = [[1,4,4,5,6],
#      [2,3,4,5,6],
#      [3,1,2,3,4],
#      [9,6,5,4,1],
#      [0,2,3,4,5]]

# for j in range(2):
#     for i in range(5):
#         print(a[i][j])

#5 rida 3 tulpa  COLUMNS * ROWS

# N = 2
# a = [[None] * N for i in range(N)]
# for i in range(N):
#     for j in range(N):
#         a[i][j] = float(input())

# total = 0
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             total += a[i][j]
# print("Sum: ", total)


# N = 2
# a = []
# for i in range(N):
#     a.append([])
#     for j in range(N):
#         a[i].append(float(input()))

# total = 0
# for k in range(N):
#     total += a[k][k]
# print("Sum: ", total)

# a = [[4,2],
#      [14,9]
#               ]

# total = 0
# for i in range(2):
#         #if i == j:
#         j = 2 - i - 1
#         total += a[i][j]
# print("Sum: ", total)
        
# N = 5
# a = [[None] * N for i in range(N)]
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             a[i][j] = -1
#         elif i > j:
#             a[i][j] = 30
#         else:
#             a[i][j] = 20

# for i in range(N):
#     for j in range(N):
#         print(a[i][j], end ="\t")
#     print()
                                 
#column * row

# ROWS = 2
# COLUMNS = 2

# a = [[None]* COLUMNS for i in range(ROWS)]
# for i in range(ROWS):
#     for j in range(COLUMNS):
#         a[i][j] = int(input())

# for i in range(ROWS):
#     for j in range(COLUMNS):
#         if a[i][j] % 2 != 0:
#             print(a[i][j])

# a = [[None] * 3 for i in range(2)]
# for i in range(2): # rida
#     for j in range(3): #tulp
#         a[i][j] = int(input())

# for i in range(2):
#     for j in range(3):
#         if a[i][j] % 2 == 0:
#             print("Even:",a[i][j])


# a = [[None] * 3 for i in range(2)]
# for i in range(2):
#     for j in range(3):
#         a[i][j] = float(input())

# sum = 0
# for i in range(2):
#     for j in range(3):
#         if i == j and i % 2 != 0 and j % 2 != 0:
#             sum += a[i][j]
        
# print(sum)

# a = [[None] * 2 for i in range(2)]
# for i in range(2):
#     for j in range(2):
#         a[i][j] = int(input())
# count = 0
# sum = 0
# sum2 = 0
# avg = 0
# for i in range(2):
#     for j in range(2):
#         if i == j:
#             count += 1
#             sum += a[i][j]
            
#             j = 2 - i - 1
#             sum2 += a[i][j]
#     avg = sum / count
# print("sum", sum)          
# print("sum2: ", sum2) 
# print("avg: ",avg)     

# STUDENTS = 20
# LESSONS = 10

# grades = [[None] * LESSONS for i in range(STUDENTS)]
# for i in range(STUDENTS):
#     print("For student No.", (i + 1, "..."))
#     for j in range(LESSONS):
#         grades[i][j] = int(input("Enter grade for lesson No."+ str(j + 1) + ":"))
# #create list averages. Iterate throught rows.
# average = [None] * STUDENTS
# for i in range(STUDENTS):
#     average[i] = 0
#     for j in range(LESSONS):
#         average[i] += grades[i][j]
#     average[i] / LESSONS
# #display all average values that are greater than 89
# for i in range(STUDENTS):
#     if average[i] > 89:
#         print(average[i])
        
# STUDENTS = 20
# LESSONS = 10
# grades = [[None] * LESSONS for i in range(STUDENTS)]
# for i in range(STUDENTS):
#     print("For student No.",(i + 1),"...")
#     for j in range(LESSONS):
#         grades[i][j] = int(input("Enter grade for lesson No." + str(j + 1) + ":"))

# #create list average. Iterate through rows
# average = []
# for row in grades:
#     average.append(math.fsum(row) / LESSONS)

# #display all average values that are greater than 89
# for i in range(STUDENTS):
#     if average[i] > 89:
#         print(average[i])

# STUDENTS = 10
# LESSONS = 5
# grades = [[None] * LESSONS for i in range(STUDENTS)]
# for i in range(STUDENTS):
#     print("For student No.",(i + 1),"...")
#     for j in range(LESSONS):
#         grades[i][j] = int(input("enter grade for lesson No" + str(j + 1) + ":"))

# #create list average. Iterate throught columns
# average = [None] * LESSONS
# for j in range(LESSONS):
#     average[j] = 0
#     for i in range(STUDENTS):
#         average[j] += grades[i][j]
#     average[j] /= STUDENTS

# #display all average values greater than 89
# for j in range(LESSONS):
#     if average[j] > 89:
#         print(average[j])

# STUDENTS = 1

# names = [None] * STUDENTS
# grades_l1 = [None] * STUDENTS
# grades_l2 = [None] * STUDENTS

# for i in range(STUDENTS):
#     names[i] = input("Enter student name No" + str(i + 1) +":")
#     grades_l1[i] = int(input("Enter grade for lesson 1: "))
#     grades_l2[i] = int(input("Enter grade for lesson 2: "))
# #calculate avg grade

# for i in range(STUDENTS):
#     total = grades_l1[i] + grades_l2[i]
#     average = total / 3
#     if average > 89:
#         print(names[i])

# STUDENTS = 10
# LESSONS = 5

# names = [None] * STUDENTS
# grades = [[None] * LESSONS for i in range(STUDENTS)]

# for i in range(STUDENTS):
#     names[i] = input("Enter name for student No." + str(i + 1) + ":")
#     for j in range(LESSONS):
#         grades[i][j] = int(input("Enter grade No." + str(j + 1) + " for " +names[i]+ ":"))
# count = [None] * STUDENTS
# for i in range(STUDENTS):
#     count[i] = 0
#     for j in range(LESSONS):
#         if grades[i][j] > 89:
#             count[i] += 1
# #displays the names of the students who have more than one grade greater than 89            
# for i in range(STUDENTS):
#     if count[i] > 1:
#         print(names[i])                          

# STUDENTS = 3
# grades_table = {"A": "90-100","B":"80-89","C":"70-79","D":"60-69","E":"0-59","F":"0-59"}

# names = [None] * STUDENTS
# grades = [None] * STUDENTS

# for i in range(STUDENTS):
#     names[i] = input("Enter student name No" +str(i + 1) + ":")
#     grades[i] = input("Enter his or her grade: ")

# for i in range(STUDENTS):
#     grade = grades[i]
#     grade_as_percentage = grades_table[grade]

#     print(names[i], grade_as_percentage)

# ROWS = 3
# COLUMNS = 4
# ELEMENTS = ROWS * COLUMNS
# a = [[5,9,3,2],
#      [11,12,4,1],
#      [10,25,22,18]
#      ]
# b = [None] * ELEMENTS

# k = 0 #this is the index of the new list b
# for j in range(COLUMNS):
#     for i in range(ROWS):
#         b[k] = a[i][j]
#         k += 1

# for k in range(ELEMENTS):
#     print(b[k], end="\t")        


# a = [[5,9,3,2],
#       [11,12,4,1],
#       [10,25,22,18]
#       ]

# print(list(enumerate(a, start=1)))



# ROWS = 3
# COLUMNS = 4
# a = [5,11,10,9,12,25,3,4,22,2,1,18]
# b = [[None] * COLUMNS for i in range(ROWS)]

# k = 0 #this is the index of list a
# for j in range(COLUMNS): #iterate through columns
#     for i in range(ROWS):
#         b[i][j] = a[k]
#         k += 1

# for i in range(ROWS): #iterate thought rows
#     for j in range(COLUMNS):
#         print(b[i][j], end ="\t")
#     print()        

# a = [5,11,10,9,12,25,3,4,22,2,1,18]
# c = ["Apollo", "Hermes", "Athena", "Aphrodite", "Dionysus"]
# print(a.sort(), a.sort(reverse=True))
# print(max(a), max(c))
# print(min(a), min(c))
# c.sort()
# print(c)
# newList = sorted(a)
# print(newList)

# for elements in sorted(c,reverse = True):
#     print(elements, end=" ")

# b = [ [4, 6, 8],
# [3, 11, 9],
# [2, 9, 1]
# ]


# for row in b:
#     for element in row:
#         print(element, end="\t")
#     print()

# STUDENTS = 2


# names = [None] * STUDENTS
# grades = [None] * STUDENTS

# grades_percentages = {"A": "90-100","B":"80-89","C":"70-79","D":"60-69","E":"0-59","F":"0-59"}
# #{90-100:"A",80-89:"B",70-79:"C",60-69:"D",0-59:"E",0-59:"F"}


# for i in range(STUDENTS):
#     names[i] = input("Enter name of a student No" + str(i + 1) + ":")
#     grades[i] = input("Enter his or her grade: " + str(i + 1) + ":")

# for i in range(STUDENTS):
#     grade = grades[i]
#     grades_table = grades_percentages[grade]
# print(names[i],grades_table)
    


# STUDENTS = 15
# TESTS = 5

# grades = [[None] * TESTS for i in range(STUDENTS)]

# for i in range(STUDENTS):
#     for j in range(TESTS):
#         grades[i][j] = int(input())

# average = [None] * STUDENTS
# for i in range(STUDENTS):
#     average[i] = 0
#     for j in range(TESTS):
#         average[i] += grades[i][j]
#     average[i] /= TESTS

# for i in range(STUDENTS):
#     print("Student No", (i + 1), ":")

#     if average[i] < 60:
#         print("E/F")
#     elif average[i] < 70:
#         print("D")
#     elif average[i] < 80:
#         print("C")
#     elif average[i] < 90:
#         print("B")
#     else:
#         print("A")


#PROCESS EACH ROW INDIVIDUALLY


# STUDENTS = 4
# LESSONS = 2
# grades = [[None] * LESSONS for i in range(STUDENTS)]
# for i in range(STUDENTS):
#     #print("For student No", (i + 1), "...")
#     for j in range(LESSONS):
#         grades[i][j] = int(input("Enter grade for lesson No."+ str(j+1) + ":"))

# average = [None] * STUDENTS
# for i in range(STUDENTS):
#     average[i] = 0
#     for j in range(LESSONS):
#         average[i] += grades[i][j]
#     average[i] /= LESSONS    

# for i in range(STUDENTS):
#     if average[i] > 89:
#         print(average[i])


# STUDENTS = 2
# LESSONS = 3
# grades = [[None] * LESSONS for  i in range(STUDENTS)]

# for i in range(STUDENTS):
#     print("Enter student name No", (i + 1), "...")
#     for j in range(LESSONS):
#         grades[i][j] = int(input("Enter grades for lesson No" + str(j + 1) + ":"))

# average = [None] * STUDENTS
# for i in range(STUDENTS):
#     average[i] = 0
#     for j in range(LESSONS):
#         average[i] += grades[i][j]
#     average[i] /= LESSONS
#     if average[i] > 89:
#         print(average[i])

# STUDENTS = 10
# LESSONS = 5
# grades = [[None] * LESSONS for i in range(STUDENTS)]

# for i in range(STUDENTS):
#     print("For student No", (i +1), ":")
#     for j in range(LESSONS):
#         grades[i][j] = int(input("Grade for lesson No" + str(j+1)+ ":"))

# average = [None] * LESSONS
# for j in range(LESSONS):
#     average[j] = 0
#     for i in range(STUDENTS):
#         average[j] += grades[i][j] 
#     average[j] /= STUDENTS

# for j in range(LESSONS):
#     if average[j] > 89:
#         print(average[j])

# STUDENTS = 2

# names = [None] * STUDENTS
# gradeOne = [None] * STUDENTS
# gradeTwo = [None] * STUDENTS

# for i in range(STUDENTS):
#     names[i] = input("Enter student name No" + str(i + 1) + ":")
#     gradeOne[i] = int(input("Enter first grade: " ))
#     gradeTwo[i] = int(input("Enter second grade: "))


# for i in range(STUDENTS):
#     total = gradeOne[i] + gradeTwo[i]
#     average = total / 2
#     if average > 89:
#         print(names[i])
        

# STUDENTS = 10
# LESSONS = 5
# names = [None] * 10
# grades = [[None] * LESSONS for i in range(STUDENTS)]
# for i in range(STUDENTS):
#     names[i] = input("Enter student name No" + str(i + 1) + ":")
#     for j in range(LESSONS):
#         grades[i][j] = int(input("Enter grade No" + str(j + 1) + ":"))

# count = [None] * STUDENTS
# for i in range(STUDENTS):
#     count[i] = 0
#     for j in range(LESSONS):
#         if grades[i][j] > 89:
#             count[i] += 1

# for i in range(STUDENTS):
#     if count[i] > 1:
#         print(names[i])
        
# STUDENTS = 3        
# grades_table = {"A": "90-100", "B": "80-89", "C": "70-79",
# "D": "60-69", "E": "0-59", "F": "0-59"}

# names = [None] * STUDENTS
# grades = [None] * STUDENTS

# for i in range(STUDENTS):
#     names[i] = input("Enter name No" + str(i+1)+":")
#     grades[i] = input("Enter his/her grade " + str(i+1)+ ":")

# for i in range(STUDENTS):
#     grade = grades[i]
#     grade_as_percentage = grades_table[grade]
#     print(names[i], grade_as_percentage)

# ROWS = 3
# COLUMNS = 4
# E = ROWS * COLUMNS

# a = [ [5, 9, 3, 2],
# [11, 12, 4, 1],
# [10, 25, 22, 18]
# ]

# b = [None] * E

# k = 0 #index of new list
# for j in range(COLUMNS): #iterate throught columns
#     for i in range(ROWS):
#         b[k] = a[i][j]
#         k += 1
        

# for k in range(E):                
#         print(b[k], end="\t")
    
# ROWS = 3
# COLUMS = 4
# a = [5, 9, 3, 2,11, 12, 4, 1,10, 25, 22, 18]
# b = [[None] * COLUMS for i in range(ROWS)]


# k = 0
# for j in range(COLUMS):
#     for i in range(ROWS):
#         b[i][j] = a[k]
#         k +=1

# for i in range(ROWS):
#     for j in range(COLUMS):
#         print(b[i][j], end ="\t")    
#     print()  

# total = 0
# a = [5, 9, 3, 2,11, 12, 4, 1,10, 25, 22, 18]
# for i in range(len(a)):
#     if a[i] > 5:
#         total += a[i]
#     average = total / len(a)
# print(average)    

# STUDENTS = 2
# TESTS = 2

# #grades_table = {"A": "90-100", "B": "80-89", "C": "70-79","D": "60-69", "E": "0-59", "F": "0-59"}
# grades_table = {"90-100": "A", "80-89": "B", "70-79": "C","60-69": "D", "0-59": "E", "0-59": "F"}
# names = [None] * STUDENTS 
# grades = [[None] * TESTS for i in range(STUDENTS)]

# for i in range(STUDENTS):
#     names[i] = input("Enter student name No" + str(i + 1) + ":")
#     for j in range(TESTS):
#       grades[i][j] = float(input("Enter his/her grades: " + str(j + 1) + ":"))

# average = 0
# for i in range(STUDENTS):
#    total = 0
#    for j in range(TESTS):
#       total += grades[i][j]
#    average = total / TESTS
#    if average > 90:
#       print(names[i],"A")
#    elif average > 80:
#       print(names[i],"B")
   
# OBJECTS = 2
# TIMES = 2
# g = [[None] * TIMES for i in range(OBJECTS)]
# name = [None] * OBJECTS

# for i in range(OBJECTS):
#     name[i] = input("Enter object No" + str(i + 1) + ":")
#     for j in range(TIMES):
#         g[i][j] = float(input("Enter calculated value No" + str(j+1) + ":"))

# total = 0
# for i in range(TIMES):
#     average = 0
#     for j in range(TIMES):
#         total += g[i][j]
#     average = total / TIMES
#     print(name[i], average)


# PLAYERS = 2
# MATCHES = 2
# points_scored = [[None] * MATCHES for i in range(PLAYERS)]
# points_per_match = [None] * MATCHES
# names = [None] * PLAYERS

# for i in range(PLAYERS):
#     names[i] = input("Enter player No" + str(i + 1)+ ":")
#     for j in range(MATCHES):
#       points_scored[i][j] = int(input("Enter points scored for match No" + str(j + 1) + ":"))
    
# for i in range(PLAYERS):
#     total = 0
#     for j in range(MATCHES):
#       total += points_scored[i][j]
#     print(names[i], "scored: ", total, " points")

# for i in range(PLAYERS):
#    print(names[i], " scored ", points_scored[i], " in " + str(i + 1) + " match")
#    for j in range(MATCHES):
#       print(names[i], " scored ", points_scored[j], " in " + str(j + 1) + " match")

# HOURS = 2
# CITY = 2

# temp = [[None] * HOURS for i in range(CITY)]
# for i in range(HOURS):
#     for j in range(CITY):
#         temp[i][j] = int(input())

# for j in range(HOURS):
#     total = 0
#     for i in range(CITY):
#         total += temp[i][j]
#     if total / CITY < 10:
#         print("Hour", (j+ 1))        
"""         
PLAYERS = 2
MATCHES = 2
names = [None] * PLAYERS
goals = [[None] * MATCHES for i in range(PLAYERS)]

for i in range(PLAYERS):
    names[i] = input("Player name No" + str(i + 1) + ":")
    for j in range(MATCHES):
        goals[i][j] = int(input("Enter score for player No" + str(j +1) + ":"))


for i in range(PLAYERS):
    total = 0
    for j in range(MATCHES):
        total += goals[i][j]
    print(names[i], ":", total / MATCHES)

for j in range(MATCHES):
    print("Match No", j+1)
    for i in range(PLAYERS):
        print("Goals scored: ",goals[i][j], end="\t")
    print()

     """

""" 
STUDENTS = 12
LESSONS = 6
names = [None] * STUDENTS
grades = [[None] * LESSONS for i in range(STUDENTS)]

for i in range(STUDENTS):
    names[i] = input("Enter student name No" + str(i +1) + ":")
    for j in range(LESSONS):
        grades[i][j] = int(input("Enter grade No" + str(j + 1) + ":"))

for i in range(STUDENTS):
    total = 0
    for j in range(LESSONS):
        total += grades[i][j]
    print(names[i], " average ", total / LESSONS)
     

for j in range(LESSONS):
    total = 0
    for i in range(STUDENTS):
        total += grades[i][j]
    print("avg for each lesson: ", total / LESSONS)

for i in range(STUDENTS):
    total = 0
    for j in range(LESSONS):
        total += grades[i][j]
    average = total / LESSONS
    if average < 60:
        print(names[i], " has average ", average)
    else:
        if average > 89:
            print(names[i], " Bravo!")
                
     """
""" 
JUDGES = 5
ARTISTS = 15
judgeNames = [None] * JUDGES
for j in range(JUDGES):
    judgeNames[j] = input("Enter name for a judge No" + str(j + 1) + ": ")

artistNames = [None] * ARTISTS    
songTitles = [None] * ARTISTS
score = [[None] * JUDGES for i in range(ARTISTS)]
for i in range(ARTISTS):
    artistNames[i] = input("Enter name for artist No" + str(i + 1) + ": ")
    songTitles[i] = input("Enter song title for artist " + artistNames[i] + ": ")
    for j in range(JUDGES):
        score[i][j] = int(input("Enter score for artist " + artistNames[i] + " from judge " + judgeNames[j] + ": "))

for i in range(ARTISTS):
    total = 0
    for j in range(JUDGES):
        total += score[i][j]
    print(artistNames[i], ",", songTitles[i], ":", total)

for j in range(JUDGES):
    total = 0
    for i in range(ARTISTS):
        total += score[i][j]
    print(judgeNames[i], ":", total / ARTISTS)
           """
          
""" PEOPLE = 30
MONTHS = 12

weight = [[None] * MONTHS for i in range(PEOPLE)]
height = [[None] * MONTHS for i in range(PEOPLE)]
for i in range(PEOPLE):
    for j in range(MONTHS):
        weight[i][j] = int(input())
        height[i][j] = int(input())

for i in range(PEOPLE):
    sumWeights = 0
    sumHeights = 0
    for j in range(MONTHS):
        sumWeights += weight[i][j]
        sumHeights += height[i][j]
    averageWeight = sumWeights / MONTHS
    averageHeight = sumHeights / MONTHS
    print(averageWeight, ", ", averageHeight)
    print(averageWeight * 702 / averageHeight ** 2)

for i in range(PEOPLE):
    print(weight[i][4] * 702 / height[i][4] ** 2)
    print(weight[i][7] * 702 / height ** 2)
 """

""" VAT = 0.19
CONSUMERS = 1000
meterRead = [[None] * 2 for i in range(CONSUMERS)]
for i in range(CONSUMERS):
    meterRead[i][0] = int(input())
    meterRead[i][1] = int(input())

total = 0
for i in range(CONSUMERS):
    consumed = meterRead[i][1] - meterRead[i][0]
    print(consumed)
    payment = consumed * 0.07
    payment += VAT * payment
    print(payment)

    total += consumed

print(total, total * 0.07 + total * 0.07 * VAT)
 """

""" ELEMENTS_OF_A = 100
ELEMENTS_OF_NEW = ELEMENTS_OF_A - 2
a = [None] * ELEMENTS_OF_A
for i in range(ELEMENTS_OF_A):
    a[i] = float(input())

newArr = [None] * ELEMENTS_OF_NEW
for i in range(ELEMENTS_OF_NEW):
    newArr[i] = (a[i] + a[i + 1] + a[i + 2]) / 3

for i in range(ELEMENTS_OF_NEW):
    print(newArr[i]) """
          
""" from math import fsum
ELEMENTS_OF_A = 2

a = []
for i in range(ELEMENTS_OF_A):
    a.append(float(input()))

newArr = []
for i in range(ELEMENTS_OF_A - 2):
    newArr.append(fsum(a[i:i*3])/3)

for element in newArr:
    print(element)          
           """
"""


ELEMENTS = 2

#read lists a and b
a = [None] * ELEMENTS
b = [None] * ELEMENTS
for i in range(ELEMENTS):
    a[i] = float(input())
for i in range(ELEMENTS):
    b[i] = float(input())

#Create list newArr
newArr = [None] * ELEMENTS
for i in range(ELEMENTS):
    if a[i] > b[i]:
        newArr[i] = a[i]
    else:
        newArr[i] = b[i]

#display list newArr
for i in range(ELEMENTS):
    print(newArr[i])
 """


print("123")







   
      