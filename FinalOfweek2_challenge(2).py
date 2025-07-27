print("\n---------------Log in to your account ---------------\n")



uname = input(" Username : ")
passw = input(" Password : ")

hitung = 0

if uname == "JonhSmith" and passw == "J2sd1cn&1" :
        print("\n     Log in Succes.\n")

while uname != "JonhSmith" and passw != "J2sd1cn&1" and hitung < 3:

    uname = input(" Username : ")
    passw = input(" Password : ")

    if uname == "JonhSmith" and passw == "J2sd1cn&1" :
        print("\n     Log in Succes.\n")
             
        
        
    else:
        print("\n     Log in Failed. Username or Password Must been wrong\n")
        hitung +=  1

    if hitung == 3 :
        print("\n     No more Attempts left!\n")
