l1=['vivek','john']
l2=['ms','google']

zipped=list(zip(l1,l2))#we ca also use set here insted of list but it will be unordered.also if we have common values then set will print it only once
print(zipped)
#also we can use dictionary instead of list
#also we can iterate through loops

print()

for a,b in zipped:
    print(a,b)