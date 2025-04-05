#tuples = collection which is ordered and unchangable immutable
#         used to group together related data

student = ("DARSHAN",21,"male")

print(student.count("DARSHAN"))
print(student.index("male"))

for x in student:
    print(x)

if "DARSHAN" in student:
    print("yes he is here")
    