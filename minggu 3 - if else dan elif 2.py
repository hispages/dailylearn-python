print('\n------------Toko online--------------\n\n\n')

barang = "\n Duktape \n panci \n kulkas\n garam doa\n"

pesanan = input('Tentu kan barang yg ingin kamu beli.' + barang + '\n' )

if pesanan == "duktape" :
    price = int(23)
    dus = input('Mau membungkus barang mu dengan dus yang proper? (y/g) \n' )
    if dus == "y":
        print((price + 30), 'ribu.')

elif pesanan == "panci" :
    price = int(150)
    dus = input('Mau membungkus barang mu dengan dus yang proper? (y/g) \n' )
    if dus == "y":
        print((price + 30), 'ribu.')

elif pesanan == "kulkas" :
    price = float(1.5)
    dus = input('Mau membungkus barang mu dengan dus yang proper? (y/g) \n' )
    if dus == "y":
        print((price + 0.1), 'jt.')
    else:
        print(price, "jt.")
    

elif pesanan == "garam doa" :
    price = int(220)
    dus = input('Mau membungkus barang mu dengan dus yang proper? (y/g) \n' )
    if dus == "y":
        print((price + 30), 'ribu.')

elif pesanan == "garam" :
    price = int(220)
    dus = input('Mau membungkus barang mu dengan dus yang proper? (y/g) \n' )
    if dus == "y":
        print((price + 30), 'ribu.')


else :
    print("\n------------- Kita belum menyediakan itu untuk sekarang, kamu bisa kembali nanti !! --------------\n")
    price = 0

