print ("Hi, in this program you can do basic mathematics")
first = input("what your first number: ") # first number
second = input("what your  number: ") # second number
operation = input("Please choose: 1.Addition 2.Subtraction 3.Multiplication 4.Division 5.power 6.floor division\: ") #choices
#the operations
switcher = {
    "1": first + second, #addition
    "2": int(first) - int(second), #substraction
    "3": int(first) * int(second), # multiplication
    "4": int(first) / int(second), # division
    "5": int(first) ** int(second), # power
    "6": int(first) // int(second) #floor division
}
print (switcher.get(operation)) #the output
'''
---------------------------------------
-- Created by:     Amirmahdi Mersad  --
-- Created on:     Apr 7 2019        --
-- Created for:    Unit 0-05         --
-- Course Code:    ICS3U             --
-- Teacher Name:   Alireza TEimoori  --
---------------------------------------
-- this program is a calculator but  --
it can also do power and floor division calculations--

'''