numbers = {'odd':3,'even':4,'prime':1,'complex':0}
numbers1 = {'yes':4,'no':0}

print(numbers.keys())
print(numbers.copy())
print(numbers.values())
print(numbers.pop('prime'))

numbers.update(numbers1)
print(numbers)

numbers['anonoumus'] = 90
print(numbers)

for val in numbers.values():
    print("values: ",val)

for key in numbers.keys():
    print("values: ",key)