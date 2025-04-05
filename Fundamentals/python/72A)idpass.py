
import csv
with open("file.csv", "w", newline="") as obj:
    fileobj = csv.writer(obj)
    fileobj.writerow(["User Id", "password"])
    while True:
        user_id = input("Enter user id: ")
        password = input("Enter password: ")
        record = [user_id, password]
        fileobj.writerow(record)
        x = input("Press Y/y to continue and N/n to terminate the program\n")
        if x in "Nn":
            break
        elif x in "Yy":
            continue

with open("file.csv", "r") as obj2:
    fileobj2 = csv.reader(obj2)
    given = input("Enter the user id to be searched\n")
    found = False
    for i in fileobj2:
        if i[0] == given:
            print("Password:", i[1])
            found = True
            break
    if not found:
        print("User id not found.")