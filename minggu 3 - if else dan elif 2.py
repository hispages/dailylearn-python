print('\n------------Toko online--------------\n\n\n')        #Online shop

barang = "\n Duktape \n panci \n kulkas\n garam doa\n"        #items available today

pesanan = input('Tentu kan barang yg ingin kamu beli.' + barang + '\n' )   #what items do you want?

if pesanan == "duktape" :                                                 #ducktape
    price = int(23)
    dus = input('Mau membungkus barang mu dengan dus yang proper? (y/g) \n' ) # do you want a proper box?
    if dus == "y":
        print((price + 30), 'ribu.')

elif pesanan == "panci" :                                                  #pan
    price = int(150)
    dus = input('Mau membungkus barang mu dengan dus yang proper? (y/g) \n' ) # do you want a proper box?
    if dus == "y":
        print((price + 30), 'ribu.')

elif pesanan == "kulkas" :                                                 #freezer
    price = float(1.5)
    dus = input('Mau membungkus barang mu dengan dus yang proper? (y/g) \n' ) # do you want a proper box?
    if dus == "y":
        print((price + 0.1), 'jt.')
    else:
        print(price, "jt.")
    

elif pesanan == "garam doa" :                                             #weird salt
    price = int(220)
    dus = input('Mau membungkus barang mu dengan dus yang proper? (y/g) \n' ) # do you want a proper box?
    if dus == "y":
        print((price + 30), 'ribu.')

elif pesanan == "garam" :                                                 #salt
    price = int(14)
    dus = input('Mau membungkus barang mu dengan dus yang proper? (y/g) \n' ) # do you want a proper box?
    if dus == "y":
        print((price + 30), 'ribu.')


else :
    print("\n------------- Kita belum menyediakan itu untuk sekarang, kamu bisa kembali nanti !! --------------\n")  # We didn't have that for now, you can come back here later !!
    price = 0

