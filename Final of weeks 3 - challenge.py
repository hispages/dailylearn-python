

print("---------------Tabel Perkalian 1 - 10--------------") # Multiplication Table


angka = int(input("the Multiple number: "))
for f in range (1,11):
    print(f"{angka} X {f} = {angka  *  f}")

ask = input("do you want to see another Multiplication? (Y/G): ")
while ask == "y" or ask == "Y" :
    angka = int(input("the Multiple number: "))
    for f in range (1,11):
            print(f"{angka} X {f} = {angka  *  f}")
    ask = input("do you want to see another Multiplication? (Y/G): ")
    