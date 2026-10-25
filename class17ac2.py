try:
    number1 = int(input("Enter first number:  "))
    number2 = int(input("Enter second number:  "))
    result = number1 / number2
    print ("After dividing results are: ", result)
except ZeroDivisionError:
    print ("Division by zero is error! ! !")
except ValueError as ex:
    print ("Enter valid whole number! ! !")
except:
    print ("Wrong input")
else:
    print ("No exception")
finally:
    print ("This will execute no matter what")
