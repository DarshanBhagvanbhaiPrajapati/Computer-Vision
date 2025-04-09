#dictionary = A changable,unordered collection of unique key:value pairs
#             fast beacause thay are hasing allow us to acces a value quikely
#muttable

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'}) #to add newone
# capitals.pop('China') #it will remove china

print(capitals['Russia']) #we have to give key it will print value pair
print(capitals.get('Germany')) #return none

print(capitals.keys()) #only print keys
print(capitals.values()) #only values
print(capitals.items()) #print whole
      
for key,value in capitals.items():
    print(key,value)