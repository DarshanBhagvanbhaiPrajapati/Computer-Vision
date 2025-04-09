#check whether palidrom or not
def isPal(s):
    return s == s[::-1]
input_string = input("Enter a string: ")
if isPal(input_string):
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")