#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
class Admin:
    def __init__(self):
        self.email=None
        self.password=None
        self.admin_list={}
        self.food_items={}
        self.FoodId=1
    def admin_login(self):
        print("You are in the login page")
        self.email=input("enter the email:")
        self.password=input("enter the password:")
        regx='gmail.com$'
        if re.search(regx,self.email):
            if self.email in self.admin_list and self.password==self.admin_list[self.email]:
                print("login successful")
            else:
                print("admin not found,please sign up")
                self.email=input("enter the email:")
                self.password=input("enter the password:")
                if re.search(regx,self.email):
                    self.admin_list[self.email]=self.password
                    print("Your admin account has been created")
                else:
                    print("invalid Emailid")                  
        else:
            print("invalid Emailid")
            
    def add_new_food(self):
        details={}
        details['Name']=input("Enter the name of the receipe:")
        details['Quantity']=input("Enter the Quantity: ")
        details['Price']=input("Enter the price for the above quantity in rupees:")
        details['Discount']=input("Enter the discount in percentage: ")
        details['Stock']=input("Enter the stock available:")
        self.food_items[self.FoodId]=details
        self.FoodId+=1        
        print(self.food_items)
    def edit_food(self):
        num=int(input("Enter the FoodId to edit food item: "))
        if num in self.food_items:
            print("Enter the item to edit:\n1. Name\n2. Quantity\n3. Price\n4. Discount\n5. Stock")
            item=input()
            if item in self.food_items[num]:
                self.food_items[num][item]=input("Enter the new {}:".format(item))
            else:
                print("item not found")
        else:
            print("FoodId not found")
    def view_foodlist(self):
        print("Name:")
        for value in self.food_items:
            print(str(value)+'.',self.food_items[value]['Name'])
        print()
        print("Quantity:")
        for value in self.food_items:
            print(str(value)+'.',self.food_items[value]['Quantity'])
        print()
        print("Price:")
        for value in self.food_items:
            print(str(value)+'.',self.food_items[value]['Price'])
        print()
        print("Discount:")
        for value in self.food_items:
            print(str(value)+'.',self.food_items[value]['Discount'])
        print()
        print("Stock:")
        for value in self.food_items:
            print(str(value)+'.',self.food_items[value]['Stock'])
    def remove_food(self):
        num=int(input("Enter the FoodId to remove food item:"))
        if num in self.food_items:
            del self.food_items[num]
        else:
            print("Invalid FoodId")
admin_object=Admin()
admin_object.admin_login()
choice={1:'Add new food',2:'Edit food ',3:'View food list',4:'Remove food',5:'Exit'}
while True:
    for value in choice:
        print(str(value)+'.',choice[value])
    choice_input=int(input())
    if choice_input==1:
        admin_object.add_new_food()
    elif choice_input==2:
        admin_object.edit_food()
    elif choice_input==3:
        admin_object.view_foodlist()
    elif choice_input==4:
        admin_object.remove_food()
    elif choice_input==5:
        print("Admin logged out")
        break
    else:
        print("Invalid input try again")

