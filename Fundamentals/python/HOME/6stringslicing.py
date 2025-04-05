#slicing = create a substring by extracting elements from another string
#     indexing[] or slice()
#    [start:stop:step]

name = "Bro code"

first_name = name[:3] #remember ending index and if we cant write start 
                       #indexing it will automatically takes zero

last_name = name[4:8] #or name[4:] it will print till end
step_up = name[::2]
reversed_name = name[::-1]


print(first_name)
print(last_name) #it will jumping by 2 
print(step_up)
print(reversed_name)


#using slice function

website1 = "http://google.com" 
website2 = "http://wikipidia.com"

#want to remove http:// and .com

slice = slice(7,-4)
print(website1[slice])  #print google
print(website2[slice]) #print wikipidia
