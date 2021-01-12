import time
import os
from datetime import datetime
now=datetime.now()
def bill():
    os.system("cls")
    print(""" 
        ================================================================
        ----------------------Reliance - SuperMarket--------------------
        ================================================================   
        """)
    print("Date:", now.strftime("%d/%m/%Y"))#Display time and date
    print("Time:", now.strftime("%H:%M %p"))
    item = {'apple': 12,'orange':200, 'wheat': 150, 'maida': 230,'rava': 100,'semiya': 200,       }
    print("""\n1.View list\n2.Purchase item\n3.Add items\n4.Search item\n5.Delete items  """)
    while True:
        try:
            u=int(input("\nEnter your choice:"))# Enter the valid input 1 o 5
            if u < 6:# if the input grater then 5 then it execute break and exception
                break
        except(ValueError,UnboundLocalError):
            print("Enter valid option")

    if u == 1:
        print("Items are available:\n",item)
        input("Press enter to continue..")
        bill()
    if u == 2:
        while True:
            try:
                while True:
                    item_name = str(input('Item name:', ))
                    if item_name not in item:
                        print("Out of stack!!")
                    else:
                        break
            except(TypeError, AttributeError):
                print("Enter valid product !!")
                bill()
            try:
                kilo = int(input('Kg :'))
                gram = int(input('Grams :'))
            except(AttributeError, ValueError):
                print("Enter valid kilo and gram!!")
                bill()
            price = item.get(item_name)
            c = round((((1000 * kilo) + gram) / 1000) * price)
            p_m = str(input("Want to puchase more y/n:"))
            if p_m == 'y':
                print("Purchase.....")
            else:
                print("-----------------------Receipt--------------------------")
                print("Date:", now.strftime("%d/%m/%Y"))
                print("Time:", now.strftime("%H:%M %p"))
                print(item_name, '\t\t', (((1000 * kilo) + gram) / 1000), 'kg\t\t', 'Rs %.2f' %(price),'\t\tRs %.2f' % (c))
                print("---------------------------------------------------------")
                print('TOTAL Rs %.2f' % (c))
                print("---------------------------------------------------------")
                print("""No 5,Junction Road,\t\t\tOpen-Close\nMeyyanur,salem-636004\t\tMon-Sun 8:00 am-10:00pm\nph.no:9578686435""")
                print("-----------------------THANK YOU FOR SHOPPING--------------------------- ")
                #print(ri,rp,rkg)
                input("Press enter to continue..")
                bill()
    if u ==3:
        try:
            while True:
                key = str(input("Add item name :"))
                if key in item:
                    print(key, "already in the list")
                else:
                    break
            val=int(input("Enter item price:"))
            item.update({key:val})
            print(item)
            x=input("Press enter to continue y/n:")
            if x=='y':
                bill()
            else:
                input("Press enter to continue ")
                bill()
        except(ValueError):
            print("Enter valid input!!")
            input("Press enter to continue..")
            bill()
    if u == 4:
        s_item=str(input("Enter item name:"))
        if s_item in item.keys():
            print("Item is found;",s_item,':','Rs',item.get(s_item))
        else:
            print("Item Not available!!")
        input("Press enter to continue..")
        bill()
    if u == 5:
        while True:
            del_item=str(input("Enter item name:"))
            if del_item not in item:
                print("No Item in list..! ")
            if del_item in item:
                del item[del_item]
                print(item)

            d_m=input("Want delete more y/n:")
            if d_m == 'y':
                print("delte...")
            else:
                input("Press enter to continue..")
                bill()
bill()
