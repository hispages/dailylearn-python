print('---------------- Seberapa sehat dan idela kamu -------------------\n\n\n')

while True :
    tinggi = input('berapa tinggi mu: ')
    beratbadan = input('berat badan mu: ')
    
    if tinggi == '' or beratbadan == '':
        print('\n- kamu tidak menulis tinggi atau berat badan\n')
        continue

    try:
        tinggi = float(tinggi)
        beratbadan = int(beratbadan)
        break
    except ValueError:
        print('\n- tulis yang bener lahh... pake angka\n')
BMInya = beratbadan / tinggi ** 2


if BMInya >= 19 and BMInya < 24 :
    print("\n- kamu ideal tetap jaga hidup sehat dgn latihan teratur\n")

elif BMInya >= 24 and BMInya < 40 :
    print("\n- kamu obesitas coba lah latihan simpel atau hanya sekedar berjalan\n")

elif BMInya >= 40 and BMInya < 60 :
    print("\n- bola daging kamu ya!?\n")

elif BMInya >= 17 and BMInya < 19 : 
    print('\n- kurang sehat kamu perlu makanan yang lebih bergizi\n')

elif BMInya >= 10 and BMInya < 17 :
    print("\n- kamu manusia atau ranting berjalan njir\n")


print(BMInya, "\n")
