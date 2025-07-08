name="renuka"
password="reddy"
s='''
   1.credit
   2.debit
   3.mini stmt
   4.exit
'''
amonut=1000
username=input("enter your name:")
pass_word=input("enter your password:")
if name==username and password==pass_word :
    while True:
        print(s)
        option=int(input("enter the option:"))
        if option==1:
            credit_amount=float(input("enter your amount:"))
            print(credit_amount+amonut)
        elif option==2:
            debit_amount=float(input("enter the amount:"))
            print(amonut-debit_amount)
        elif option==3:
            print("###mimi stmt amont###",amonut)
        elif option==4:
            break
else :
    print("incorrect")       