from datetime import datetime
from unicodedata import name
#input function for name
Name =input("Enter your name :")

#list create
list = '''
    Rice Rs 40/kg
    Atta Rs 70/kg
    Maida Rs 40/kg
    Bombai Rava Rs 42/kg
    Organic Dal Rs 143/kg
    Saffola oats Rs 137/kg
    Fortune oli Rs 174/kg
    Tata salt Rs 24/kg
    Maggi Rs 7/pare pack
    B natural juice Rs 77/litter
    Honey Rs 399/kg
    Cadbury shots 101/pare pack
    Tea Rs 20/100g
    Ariel liquid 200/litter
    
'''

Price = 0
Pricelist =[]
Totalprice = 0
Finalprice = 0
ilist =[]
qlist =[]
plist =[]

#rates for items

items ={'Rice':40,'Atta':70,'Maida':40,'Bombai Rava':42,'Organic Dal':143,'Saffola oats':137,'Fotune oli':174,'Tata salt':24,'Maggi':7,
        'B natural juice':77,'Honey':399,'Cadbury shots':101,'Tea':20,'Ariel liquid':200}

#Decalration functions

option =int(input("for list of items press 1:"))
if option ==1:
    print(list)
for i in range(len(items)):
    inp1 =int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1 ==2:
        break
    if inp1 ==1:
        item =input("Enter items:")
        quantity =int(input("Enter your quantity:"))
        if item in items.keys():
            price = quantity*(items[item])

# print(price)

            Pricelist.append((item,quantity,items,price))
            Totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(Totalprice*3)/100
            finalamount =gst+Totalprice
        else:
            print("sorry you entered items not available")
    else:
        print("you entered wrong number")
        
inp =input("can i bill the items yes or no:")
if inp =='yes':
    pass
if finalamount!=0:
    print(25*"=","Friends supermarkte",25*"=")
    print(28*"=","AShok nagar")
    print("Name :",name,30*" ","Date:",datetime.now())
    print(75*" ")
    print("Sno",8*" ",'items',8*" ","Quantity",3*" ",'price')

    for i in range(len(Pricelist)):
        print(i,8*" ",8*" ",ilist[i],3*" ",qlist[i],plist[i])

        print(75*"-")
        print(50*"-",'Totalamount:','Rs',Totalprice)
        print("gst amount",50*"-",'Rs',gst)
        print(75*"-")
        print(50*" ",'finalamount:','Rs',finalamount)
        print(75*" ")
        print(20*" ","Thanks for visiting")
        print(75*" ")
