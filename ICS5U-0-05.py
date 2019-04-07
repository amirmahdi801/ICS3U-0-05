print ("Hi, in this program you can do basic mathematics")
first = input("what your first number: ")
second = input("what your  number: ")
operation = input("Please choose: 1.Addition 2.Subtraction 3.Multiplication 4.Division 5.power: ")
switcher = {
    "1": first + second,
    "2": int(first) - int(second),
    "3": int(first) * int(second),
    "4": int(first) / int(second),
    "5": pow(first.second)
}
print (switcher.get(operation))