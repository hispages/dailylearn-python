#print('---------perkalian * 1 - 99--------- \n\n\n')

#a = int(input("angka pertama : "))
#b = int(input("angka kedua : "))



#if a >= 1000:
    #print("Apalagi 1000 !!")
    #exit()
#elif a >= 100 :
    #print("aku gak sepintar itu untuk bisa perkalian 100")
    #exit()
#else:
    #print(f" hasil nya adalah {a * b}")
#if b >= 100 :
    #print("aku gak sepintar itu untuk bisa perkalian 100")
    #exit()
#elif b >= 1000 :
    #print("Apalagi 1000 !!")
    #exit()
#if a <= 0 :
    #print("masukkan angka kalo gak, gak dikasih hasil")
    #exit()
#if b <= 0 :
 #   print("masukkan angka kalo gak, gak dikasih hasil")
    #exit()

print('------------Toko online--------------\n\n\n')

barang = "\n Duktape \n panci \n kulkas\n garam doa\n"

pesanan = input('Tentu kan barang yg ingin kamu beli.' + barang + '\n' )
dus = input('Mau membungkus barang mu dengan dus yang proper? (y/g) \n' )

if pesanan == "duktape" :
    price = int(23)

elif pesanan == "panci" :
    price = int(150)

elif pesanan == "kulkas" :
    price = float(1.5)

elif pesanan == "garam doa" :
    price = int(220)

elif pesanan == "garam" :
    price = int(220)

else :
    print("Kita belum menyediakan itu untuk sekarang")
    price = 0


if pesanan == "kulkas":
    if dus == "y":
        print((price + 0.1), 'jt.')

    else: 
        print(price, 'jt.')

    
    

else:
    if dus == "y":
        print((price + 30), 'ribu.')

    else: 
        print(price, 'ribu.')