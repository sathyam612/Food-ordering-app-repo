#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
class User:
    def __init__(self):
        self.email=None
        self.password=None
        self.user_list={}
        self.user_details={}
        self.food_items={1:'Tandoori Chiken (4 pieces) [INR 240]',2:'Vegan Burger (1 Piece) [INR 320]',3:'Truffle Cake (500gm) [INR 900]'}
        self.order_list=[]
        self.order_id=1
    def user_login(self):
        self.success=None
        while self.success is None:
            details={}
            print("You are in the login page")
            self.email=input("enter the email:")
            self.password=input("enter the password:")
            regx='gmail.com$'
            if re.search(regx,self.email):
                if self.email in self.user_list and self.password==self.user_list[self.email]:
                    print("login successful")
                    self.success=1
                else:
                    print("User not found,please register")
                    self.email=input("enter the email:")
                    self.password=input("enter the password:")
                    if re.search(regx,self.email):
                        self.user_list[self.email]=self.password
                        details['Full name']=input("enter your full name:")
                        details['Phone number']=input("enter your phone number:")
                        details['Address']=input("enter your address:")
                        self.user_details[self.email]=details
                        print("Your user account has been created")
                        self.success=1
                    else:
                        print("invalid Emailid")                  
            else:
                print("invalid Emailid")
    def place_new_order(self):
        my_dict={}
        print("Menu:")
        for value in self.food_items:
            print(str(value)+'.',self.food_items[value])
        choice=list(input("select the required food items by entering numbers from above list"))
        print("Your selections are:")
        for i in choice:
            if i=='1':
                print(i+'.',self.food_items[1])
                my_dict[self.order_id]=self.food_items[1]
                self.order_id+=1
            elif i=='2':
                print(i+'.',self.food_items[2])
                my_dict[self.order_id]=self.food_items[2]
                self.order_id+=1            
            elif i=='3':
                print(i+'.',self.food_items[3])
                my_dict[self.order_id]=self.food_items[3]
                self.order_id+=1
            else:
                pass
        print("To confirm the order enter 1")
        num=input()
        if num=='1':
            print("order confirmed")
            self.order_list.append(my_dict)
        else:
            print("order cancelled")
    def order_history(self):
        if self.order_list==[]:
            print("No orders found")
        else:
            print("Orders history:")
            print(self.order_list)
    def profile_update(self):
        print("1. edit password\n2. edit full name\n3. edit phone number\n4. edit address")
        num=input("enter your choice:")
        if num=='1':
            self.password=input("enter the new password:")
            print("password updated")
        elif num=='2':
            self.user_details[self.email]['Full name']=input("enter the new name:")
        elif num=='3':
            self.user_details[self.email]['Phone number']=input("enter the new phone number:")
        elif num=='4':
            self.user_details[self.email]['Address']=input("enter the new address:")
        else:
            print("invalid choice")    
        
user_object=User()
user_object.user_login()
choice={1:'Place New Order',2:'Order History',3:'Update Profile',4:'Exit'}
while True:
    print("Options:")
    for value in choice:
        print(str(value)+'.',choice[value])
    choice_input=int(input())
    if choice_input==1:
        user_object.place_new_order()
    elif choice_input==2:
        user_object.order_history()
    elif choice_input==3:
        user_object.profile_update()
    elif choice_input==4:
        print("user logged out")
        break
    else:
        print("Invalid input try again")

