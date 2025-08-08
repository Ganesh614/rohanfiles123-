
#grade sheet
'''print("enter the marks in particular subject") #this code is for calculating grade
mark_student_got=int(input())
if(0<=mark_student_got<=100):
  if(mark_student_got>=90):
      print('Grade A')
  if(90>mark_student_got>=80):
       print('Grade B')
  if(80>mark_student_got>=70):
    print('Grade C')
  if(70>mark_student_got>=60):
    print('Grade D')
  if(mark_student_got<60):
     print('Grade E')
else:
 print('invalid')'''

#import math

#simulate the coin tossing
'''import random
a=random.random()

if (a<.9):
    print("heads")
else:
    print("tails")'''



'''import calendar

print(calendar.month(1999, 10))
print(calendar.calendar(1999))
from calendar import*
print(month(2120, 12))
import calendar as c
from calander import month as m'''

#here we are in week three
#we willl be studying loops

#i would like to write a piece of code, which user attempt as many time as he wants
#the code will end when it get right answer
'''print("when did india got independence (year)?")
year=int(input())

while(year!=1947):
    print("try again")
    year=int(input())

print("you got it")'''



#i would like to write a piece of code fro the factorial of a number

'''print("eneter a number")
n=int(input())

i=1
answer=2
while(i<=n):
  answer=answer*i
  i=i+1

print(answer)'''

#i would like to write a piece of code fro the factorial of a number

'''n=int(input("eneter a number"))

fact=1
while(0<n):
    fact=fact*n
    n= n-1  
print(fact)

#i would like to write a piece of code fro the factorial of a number

n=int(input("eneter a number"))

fact=1
if (n<0):
    print("not defined")
else:
    while(n>0):
      fact=fact*n
      n= n-1  
    print(fact)'''

#i would like to write a piece of code fro the number of digits in given number
#abs=absolute variable

'''n=abs(int(input("eneter a number")))
digits=1
while(n>9):
    n=n//10
    digits=digits +1

print(digits)'''

#for example find the number of digits in the given number

'''num=abs(int(input("Enter the number: ")))
str_num=str(num)
digits=0
for c in str_num:
    digits=digits+1
print("digits: ",digits)'''


#i would like to write a piece of code fro the reversing the number
'''num=int(input("Enter the number"))
rev=num%10 #remainder
num=num//10 #quotient
while(num>0):
    r=num%10 #store the remaining number
    num=num//10 
    rev=rev*10+r
print(rev)'''

#i would like to write a piece of code fro the reversing the number
'''num=int(input("Enter the number"))
abs_num=abs(num)
rev=abs_num%10 #remainder
num=abs_num//10 #quotient
while(num>0):
    r=num%10
    num=num//10
    rev=rev*10+r
print(rev)'''

#i would like to write a piece of code fro the reversing the negative number
'''num=int(input("Enter the number"))
abs_num=abs(num)
if(num>=0):
  rev=num%10
  num=num//10
  while(num>0):
      r=num%10
      num=num//10
      rev=rev*10+r
  print(rev)
else:
  rev=abs_num%10 
  abs_num=abs_num//10 
  while(abs_num>0):
      r=abs_num%10 
      abs_num=abs_num//10
      rev=rev*10+r  
  print(rev-2*rev)'''

#i would like to write a piece of code fro the reversing the negative number
'''num=int(input("Enter the number:"))
abs_num=abs(num)
rev=abs_num%10
abs_num=abs_num//10
while(abs_num>0):
  r=abs_num%10 
  abs_num=abs_num//10
  rev=rev*10+r
if(num>=0):
   print(rev)
else:   
   print(rev-2*rev)'''

#pronlem1: reverse the given number

'''num=int(input("enter the number"))
abs_num=str(abs(num))
rev=" "
for i in abs_num:
    rev=i+rev
if (num>=0):
  print (rev)
else:
    print("-"+rev)'''

#i would like to write a piece of code to find the number is palindrome or not
'''num=int(input("Enter the number:"))
abs_num=abs(num)
rev=abs_num%10
abs_num=abs_num//10
while(abs_num>0):
  r=abs_num%10 
  abs_num=abs_num//10
  rev=rev*10+r
if(num<0):
   rev=rev-2*rev
if(num==rev):
   print("The number is palindrome")

else:   
   print("not pallindrome")'''


#i would like to write a piece of code to multiple tha same word
#example for loop ﻿namaste 
'''for i in range(1, 10):
  print(i, "hello world")

for r in range(15):
  if(r%3==0):
    print(r, "namaste")'''

#i would like to write a piece of code to print ths sum of intigers  
#example for loop 
'''print("enter the number:")
n=int(input())
sun=0
for i in range(n):
  sun=sun+i
print(sun)'''


#i would like to write a piece of code to print the date in single line

'''d=10
m=10
y=2023
print("youy birthday is on", end=' ') #end give the next print statement in same line
print(d, m, y, sep="/") # sep gives the space'''


#i would like to write a piece of code to print tabelof 5

'''num=int(input("enter the number"))
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)
    print(f'{num} x {i} = {num*i}')
    print('{0} x {1} = {2}'.format(num, i, num*i))
    print('%d x %d = %d'%(num, i, num*i))'''

'''num=int(input("enter the number"))
for i in range(11, 0, -1):
      print(num, 'x', i, '=', num*i)
      print(f'{num} x {i} = {num*i}')
      print('{0} x {1} = {2}'.format(num, i, num*i))
      print('%d x %d = %d'%(num, i, num*i))'''

#i would like to write a piece of code to print value of pi

'''pi=22/7
print(f'value of pi = {pi:.4f}')
print('value of pi = {0:.4f}'.format(pi))
print('value of pi = %.4f'%(pi))'''

#i would like to write a piece of code to print 
#1
#11
#111  tp
#  1
# 11
#111
'''print('{0:3d}'.format(1))
print('{0:3d}'.format(11))
print('{0:3d}'.format(111))'''


#to check if there is any repetation in the list

'''import random

l=[]

for i in range(30):
  l.append(random.randint(1, 365))
l.sort()
print(l)
#append random between 1 to 365
#append 30 of them


i=0
flag=0 #denotes that there is no repetation
while(i<=len(l)-1):
    if(l[i]==l[i+1]):
        print("repetation found")
        flag=1
        break
    i=i+1
if(flag==0):
    print("no repetation found")'''

#to check if there is any repetation in the list

'''import random

l=[]

for i in range(20):
  l.append(random.randint(1, 365))
l.sort()
print(l)
#append random between 1 to 365
#append 30 of them


i=0
flag=0 #denotes that there is no repetation
while(i<len(l)-1):
    if(l[i]==l[i+1]):
        print("repetation found", l[i],l[i+1])
        flag=1
        break
    i=i+1
if(flag==0):
    print("no repetation found")'''


#write a piece of code to find the dot oriduct

'''x=[1,2,3,4,5]
y=[6,7,8,9,10,2]

sum=0
if(len(x)==len(y)):
  for i in range(len(x)):
      sum=sum+x[i]*y[i]
print(sum)'''

print(1+2)









    





 
  
    
