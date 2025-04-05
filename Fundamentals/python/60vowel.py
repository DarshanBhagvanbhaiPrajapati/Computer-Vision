#2) write a programme to replace the vowel character with special symbols
string = "Darshan prajapati"

newlist = list(string) 


for i in range(0,len(newlist)):
    if newlist[i] in ["a"]:
        newlist[i] = "@"

print(newlist)

   