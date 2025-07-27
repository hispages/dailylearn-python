import random



print("                 welcome to                 ")
print("____________Number Guessing Game____________")

print("\n *in this game you will guessing what number i pick\n*to make it easier \n*i will say 'Cool' when your number is Bellow my number and 'Hot' when it Above to my number\n\n")

number = None
Count = 0



randomnum = random.randint (1 , 100)

if randomnum % 2 == 0 :
    hintt = "even"

elif randomnum % 2 == 1 :
    hintt = "odd"

while number != randomnum :
    try:
        number = int(input("Your number: "))

        
        Count += 1


        if number < randomnum:
            print("Cool! Bro\n")

                 
        elif number > randomnum:
            print("Hot! bro\n")
            
        else :
            print(f"You're right!! You're Succed Guessing my number {randomnum}, Your Attempts is {Count}\n")


        if Count == 7 :

            ask = input("do you want do hint?")
                
            if ask == "y" or ask == "Y" or ask == "yes" or ask == "Yes" or ask == "YES" :
                print(f"Your hint is '{hintt}'\n")



                


    except ValueError:
            print('put a "Number"')