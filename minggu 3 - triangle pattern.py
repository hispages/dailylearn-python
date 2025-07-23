rows = int(input("rows: "))      #run and put number 1-5 here, it will continue add ing more star until 5 star or you can extend it
while rows <= 5 :                # here you can extend it number so the star will continue to the number you pick
    collums = 1
    while collums <= rows :
        print("*", end=" ")
        collums+=1
    rows+=1
    print()
    