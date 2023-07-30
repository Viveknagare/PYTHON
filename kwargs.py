def person(name,**data):#don star dene se variable length keyword argument lee sakte hein
    print(name)
    for i in data:
        print(i)

    print()
    for i,j in data.items():
        print(i,j)

person('vivek',age=28,city='mumbai',pincode=400075)
