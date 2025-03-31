#SUPER  MARKET BILL - GENERATION
from datetime import datetime

name=input("enter your name:")

# LIST OF ITEMS
lists='''
Rice    Rs    20/kg
Sugar   Rs    30/kg
Salt    Rs    20/kg
Oil     Rs    80/liter
Paneer  Rs    110/kg
Maggi   Rs    50/kg
Boost   Rs    90/each
Colgate Rs    85/each 
'''
# print(lists)
# DECLARATION
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

# RATE FOR ITEMS
items={'Rice':20,
       'Sugar':30,
       'Salt':20,'Oil':80,
       'Panner':110,
       'Maggi':50,
       'Boost':90,'Colgate':85}

option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to by press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry Your Enter Item is not Available")
    else:
        print("Your Entered Wrong Number")
    inp=input("Can I Bill The Items Yes Or No:")
    if inp=='Yes':
        pass
        if finalamount!=0:
            print(25*"=","Dev SuperMarket",25*"=")
            print(28*" ","wanaparty")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')

            for i in range(len(pricelist)):
                print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",40*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(75*"-")
            print(20*" ","Thanks for visiting")
            print(75*"-")