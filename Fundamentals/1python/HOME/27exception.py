#exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("entre the num to divide: "))
    denominator = int(input("entre a number to divide by: "))
    result = numerator/denominator

except ZeroDivisionError as e:
    print(e)
    print("you can divide by zero ! idiot!")

except ValueError as e:
    print(e)
    print("entre only number plz")

except Exception as e:
    print(e)
    print("something went wrong")

else:
    print(result)
finally:
    print("this will always execute")