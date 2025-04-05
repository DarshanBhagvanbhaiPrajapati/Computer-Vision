def check_palidrome(str):
    first_str = str.replace(" ","").lower()

    second_str = first_str[::-1]
    return first_str == second_str

str = input("entre string: ")
if check_palidrome(str):
    print("it is palidrome string")
else:
    print("it is not palidrome")