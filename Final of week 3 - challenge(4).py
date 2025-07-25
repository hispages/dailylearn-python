usr = {
    "24682": {"pin": "42112","balance": 300000},
    "13579": {"pin": "82981","balance": 800000}}
def log_in():
    usrid = input("put your id: ")
    uspin = input("put your pin: ")

    if usrid in usr and usr[usrid]["pin"] == uspin :
        print("\n- Log in succed ! \n")
        return usrid
        
    else :
        print("\n- ID or PIN is must been wrong, try again\n")
        return None

def showbelance(usrid):
    if usrid:
        print(f"\n- Your balance is {usr[usrid]['balance']:,} dollars\n".replace(",","."))


def withdraw(usrid) :
    if usrid :
        Amount = int(input("How much do you want to withdraw? : "))

        if Amount > 0 and Amount <= usr[usrid]["balance"] :
            usr[usrid]["balance"] -= Amount
            print(f"\n- {Amount} dollars Withdraw is success ! Balance left {usr[usrid]["balance"]:,} dollars\n".replace (",","."))
        else:
            print("= Withdraw cannot executed. The Amount is Nonesense")
            

def send(usrid) :
    if usrid :

        idsend = int(input("Write down the ID to send :"))

        Amount = int(input("How much do you want to send? : "))

        if Amount > 0 and Amount <= usr[usrid]["balance"] :
            usr[usrid]["balance"] -= Amount
            print(f"\n- Sending {Amount} dollars to {idsend} is success ! Balace left {usr[usrid]["balance"]:,} dollars\n".replace (",","."))
        else:
            print("\n- Sending cannot executed. The Amount is Nonesense")

def main():
    usrid = None

    while True:
        if not usrid :
            usrid = log_in()
        
        else:
            print("Choose action: ")
            print("\n1. for Withdraw")
            print("2. Show balance")
            print("3. Send to another ID")
            print("4. Log out\n")

            action = input("Put your action : ")

            if action == "1" :
                withdraw(usrid)
            elif action == "2" :
                showbelance(usrid)
            elif action == "3" :
                send(usrid)
            elif action == "4" :
                usrid = None
                print("\n- log out Success !\n")
                break
            else:
                print("\n- that action is not available !\n")

main()
