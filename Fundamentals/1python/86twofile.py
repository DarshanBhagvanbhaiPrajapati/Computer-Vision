with open("my file.txt","r") as f:
   data1=f.read()
with open("new file.txt","r") as p:
   data2=p.read()
with open("merge file.txt","a") as d:
   data3=data1+data2
   d.write(data3)
with open("merge file.txt","r") as c:
   data=c.read()
   print(data)