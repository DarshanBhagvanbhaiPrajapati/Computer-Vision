num1 = int(input("entre number1:"))
num2 = int(input("entre number2:"))

operator = input("entre operator:")

match operator:
    case "+":
        print("sum is",num1+num2)
    case "-":
        print("difference is",num1-num2)
    case "*":
        print("multiplication is",num1*num2)
    case "/":
        print("division is",num1/num2)
    case _ :
        print("entre a valid operator")