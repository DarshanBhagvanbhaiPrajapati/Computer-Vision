eng_marks = int(input("entre the english marks : "))
math_marks = int(input("entre the maths marks: "))

#if both aree more than 80,print A grade
if eng_marks >80 and math_marks > 80 :
    print("A grade")
#if either of marks are more than 80
elif eng_marks >80 or math_marks >80:
    print("B grade")
#if neither marks grater than 80
else:
    print("c grade")