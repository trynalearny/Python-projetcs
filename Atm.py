import time
print("Please enter your card detials")
time.sleep(5)
password=1234
pin=int(input("enter ur pin :"))
balance =5000
if pin==password:
    while True:
        print("""
        1==balance
        2== withdraw balance
        3==deposit balance
        4== exit""")
        try:
            option=int(input("please enter your choice:"))
        except:
            print("Please enter valid option:")
        if option==1:
            print(f"Your current balanec is {balance}")
            print("============================================================")
        if option ==2:
            withdraw_amount=int(input("please enter wihtdraw amount:"))
            balance =balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account ")
            print(f"your cureent balance is {balance}")
            print("============================================================")

        if option ==3:
            deposit_amount=int(input("please enter deposit amount:"))
            balance =balance+deposit_amount
            print(f"{deposit_amount} is credited to your account ")
            print(f"your cureent balance is {balance}")
           
        print("============================================================")

        if option==4:
            break


else:
    print("wrong pin")
