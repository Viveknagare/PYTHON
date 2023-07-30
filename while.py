x = int(input('enter a number of times you want to print the statement\n'))
i = 0

while i < x:
    print('vivek ', end="")#end use kiya toh woh statement ko print krke usee hein line pe rahega age nahi jayega
    j = 1
    while j <= 5:
        print('rocks ', end="")
        j = j + 1
    i += 1
    print()#yeh use kiya toh new line pe cursour gaya
if i == x:
    print('program terminated')

