print("----------------Pak Somad Tukang kayu-------------------")

kayu_an = "\n kayu jati \n kayu sonokeling \n kayu merbau \n kayu ulin \n kayu bengkirai \n kayu meranti \n kayu sengon \n kayu trembesi \n kayu kamper"

print(kayu_an)


kayuanput = input('\n\nkayu apa yang kamu cari? ')             #what kind of wood you're looking for?


if kayuanput == 'kayu jati' or kayuanput == 'kayu sonokeling' or kayuanput == 'kayu merbau' or kayuanput == 'kayu ulin' or kayuanput == 'kayu bengkirai' or kayuanput == 'kayu sengon' or kayuanput == 'kayu trembesi' or kayuanput == 'kayu kemper':
    print('\n- Ada kayu nya!\n')  #yea we have it



elif kayuanput == 'kayu apaaja' or kayuanput == 'yang penting kayu' or kayuanput == 'apa aja' or kayuanput == 'yang mana aja' :           #you said any wood, so it give you any
    import random
    kayura_ = ["\n\nkayu jati\n\n","\n\nkayu sonokeling\n\n","\n\nkayu merbau\n\n","\n\nkayu ulin\n\n","\n\nkayu bengkirai\n\n","\n\nkayu meranti\n\n","\n\nkayu sengon\n\n","\n\nkayu trembesi\n\n","\n\nkayu kamper\n\n"]
    randomsel = random.choice(kayura_)
    print(randomsel)         


elif kayuanput == "" or kayuanput == "." or kayuanput == "..." :
    print('\n\n\n\n\n\n... kok diam aja?\n\n\n\n')             #what make you freeze?

else : 
    print('\n- Kayu itu gak ada disini...\n')       #we don't have that here
