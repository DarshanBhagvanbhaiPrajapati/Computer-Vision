#WAP to read a text file (e.g., a.txt) and copy its content to another file (e.g., b.txt). 
#using file operations
def copy_file_content(source_file, destination_file):
  with open(source_file, 'r') as source:
    with open(destination_file, 'w') as destination:
      destination.write(source.read())
source_file = "a.txt"
destination_file = "b.txt"
f1=open('a.txt','r')
data1=f1
print(data1.read())
copy_file_content(source_file, destination_file)
print(f"Content copied from '{source_file}' to '{destination_file}' successfully.")