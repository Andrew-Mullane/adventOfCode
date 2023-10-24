import string

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

priorities = ['0'] + lowercase + uppercase

with open('./input.txt') as f:
    contents = f.readlines()

commonItems = []
itemPriorities = []

for sack in contents:
    mid = int(len(sack)/2)
    firstCompartment = sack[:mid]
    secondCompartment = sack[mid:] 
    for item in firstCompartment:
        if item in secondCompartment:
            commonItems.append(item)
            break
        
print(len(commonItems))

for item in commonItems:
    itemPriorities.append(priorities.index(item))    
    
# print(itemPriorities)

sumPriorities = sum(itemPriorities)


print(sumPriorities)   
