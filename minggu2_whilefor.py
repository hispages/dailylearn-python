print('---------------- Seberapa sehat dan idela kamu -------------------\n\n\n') #How good and ideal your body is

print("example height (cm) and wheight (kg): \n1.77 \n65\n")

while True :
    tinggi = input('berapa tinggi mu: ') # run and put your height here
    beratbadan = input('berat badan mu: ') # and also you bady wheight
    
    if tinggi == '' or beratbadan == '': # if you put nothing we gonna respon "you're not putting your height and body wheight yet"
        print('\n- kamu tidak menulis tinggi atau berat badan\n')
        continue

    try:
        tinggi = float(tinggi)
        beratbadan = int(beratbadan)
        break
    except ValueError:
        print('\n- tulis yang bener lahh... pake angka\n')  # "pls write with number"
BMInya = beratbadan / tinggi ** 2


if BMInya >= 19 and BMInya < 24 :
    print("\n- kamu ideal tetap jaga hidup sehat dgn latihan teratur\n")   # you're in ideal BMI, keep your healthy life

elif BMInya >= 24 and BMInya < 40 :
    print("\n- kamu obesitas coba lah latihan simpel atau hanya sekedar berjalan\n") # you're potentialy get obesity or already got one, try little exercise or just take a little walk

elif BMInya >= 40 and BMInya < 60 :
    print("\n- bola daging kamu ya!?\n") # meat ball !?

elif BMInya >= 17 and BMInya < 19 : 
    print('\n- kurang sehat kamu perlu makanan yang lebih bergizi\n') # you're lack of nutrition, you need food that have a good nutrition

elif BMInya >= 10 and BMInya < 17 :
    print("\n- kamu manusia atau ranting berjalan njir\n")  # stick man


print(BMInya, "\n")
