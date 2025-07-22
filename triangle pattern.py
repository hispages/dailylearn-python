rows = int(input("rows: ")) 
while rows <= 5 : 
    collums = 1
    while collums <= rows :
        print("*", end=" ")
        collums+=1
    rows+=1
    print()
    