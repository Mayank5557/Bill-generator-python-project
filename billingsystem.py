from tkinter import*
import  random
from tkinter import messagebox


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #==================VARIABLES==================================================================================
        #==========================Cosmetics======================================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.lotion=IntVar()
        #=========================grocery================================
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.pulses=IntVar()
        self.wheat=IntVar()
        self.tea_bag=IntVar()
        self.sugar=IntVar()
        #=========================Cold Drinks================================
        self.coke=IntVar()
        self.apple_juice=IntVar()
        self.mango_drink=IntVar()
        self.soda=IntVar()
        self.hot_tea=IntVar()
        self.coffee=IntVar()
        #===============Total Product & Tax Variable==========================
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
        #=================================Customer======================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()


        #============Customer Detail Frame====================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,text=" Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)


        #=================COSMETICS FRAME==================================

        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)


        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_Cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Face_W_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_W_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Hair_s_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_g_lbl=Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_txt=Entry(F2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Body_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_txt=Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #=================Grocery FRAME==================================

        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)


        g1_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_cream_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_Cream_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(F3,text="Pulses",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.pulses,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g6_lbl=Label(F3,text="Tea Bag",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea_bag,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        g5_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)


        #=================Cold Drinks FRAME==================================

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=675,y=180,width=325,height=380)


        d1_lbl=Label(F4,text="Coke",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        d1_txt=Entry(F4,width=10,textvariable=self.coke,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=2,padx=10,pady=10)

        d2_cream_lbl=Label(F4,text="Apple Juice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        d2_Cream_txt=Entry(F4,width=10,textvariable=self.apple_juice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=2,padx=10,pady=10)

        d3_lbl=Label(F4,text="Mango Drink",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        d3_txt=Entry(F4,width=10,textvariable=self.mango_drink,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=2,padx=10,pady=10)

        d4_lbl=Label(F4,text="Soda",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        d4_txt=Entry(F4,width=10,textvariable=self.soda,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=2,padx=10,pady=10)

        d6_lbl=Label(F4,text=" Hot Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        d6_txt=Entry(F4,width=10,textvariable=self.hot_tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=2,padx=10,pady=10)

        d5_lbl=Label(F4,text="Coffee",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        d5_txt=Entry(F4,width=10,textvariable=self.coffee,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=2,padx=10,pady=10)


        #================Bill Area=================================================

        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=338,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #========================Button Frame==========================


        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
        m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

       
        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

       
        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        
        m3_lbl=Label(F6,text="Total Drinks Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        c1_lbl=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

       
        c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        
        c3_lbl=Label(F6,text="Drinks Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.bill_area()

    def total(self):
        

        self.total_cosmetic_price=float(
                                    (self.soap.get()*40) +
                                    (self.face_cream.get()*120) +
                                    (self.face_wash.get()*60) +
                                    (self.spray.get()*180)+
                                    (self.gell.get()*140)+
                                    (self.lotion.get()*180)

                                    
                                    )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.18),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))


        self.total_grocery_price=float(
                                    (self.rice.get()*80)+
                                    (self.food_oil.get()*180)+
                                    (self.pulses.get()*60)+
                                    (self.wheat.get()*240)+
                                    (self.tea_bag.get()*40)+
                                    (self.sugar.get()*150)
                                    )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.05),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))


        self.total_drinks_price=float(
                                    (self.coke.get()*40) +
                                    (self.apple_juice.get()*110) +
                                    (self.mango_drink.get()*20) +
                                    (self.soda.get()*30) +
                                    (self.hot_tea.get()*25) +
                                    (self.coffee.get()*150)
                                    )
        self.cold_drink_price.set("Rs. "+str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price*0.12),2)
        self.cold_drink_tax.set("Rs. "+str(self.d_tax))

        self.total_bill=float(self.total_cosmetic_price+self.total_grocery_price+self.total_drinks_price+self.c_tax+self.g_tax+self.d_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Aggarwal Retail\n")
        self.txtarea.insert(END,f"\nBill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone Number : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n=====================================")
        self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n=====================================")

    def bill_area(self):
        #if self.c_name.get()=="" or self.c_phon.get()=="":
          # messagebox.showerror("Error","Customer Details are must" )

        
        self.welcome_bill()
        if self.soap.get()!=0:
            self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.soap.get()*40}")

        if self.face_cream.get()!=0:
            self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.face_cream.get()*120}")

        if self.face_wash.get()!=0:
            self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.face_wash.get()*60}")

        if self.spray.get()!=0:
            self.txtarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.spray.get()*180}")

        if self.gell.get()!=0:
            self.txtarea.insert(END,f"\n Hair Gell\t\t{self.gell.get()}\t\t{self.gell.get()*140}")

        if self.lotion.get()!=0:
            self.txtarea.insert(END,f"\n Body Lotion\t\t{self.lotion.get()}\t\t{self.lotion.get()*180}")


            #grocery
        if self.rice.get()!=0:
            self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.rice.get()*80}")

        if self.pulses.get()!=0:
            self.txtarea.insert(END,f"\n Pulses\t\t{self.pulses.get()}\t\t{self.pulses.get()*60}")

        if self.wheat.get()!=0:
            self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.wheat.get()*240}")

        if self.tea_bag.get()!=0:
            self.txtarea.insert(END,f"\n Tea Bags\t\t{self.tea_bag.get()}\t\t{self.tea_bag.get()*40}")

        if self.sugar.get()!=0:
            self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.sugar.get()*150}")

        if self.food_oil.get()!=0:
            self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.food_oil.get()*180}")

            #drinka
        if self.coke.get()!=0:
            self.txtarea.insert(END,f"\n Coke\t\t{self.coke.get()}\t\t{self.coke.get()*40}")

        if self.apple_juice.get()!=0:
            self.txtarea.insert(END,f"\n Apple Juice\t\t{self.apple_juice.get()}\t\t{self.apple_juice.get()*110}")

        if self.mango_drink.get()!=0:
            self.txtarea.insert(END,f"\n Mango Drink\t\t{self.mango_drink.get()}\t\t{self.mango_drink.get()*20}")

        if self.hot_tea.get()!=0:
            self.txtarea.insert(END,f"\n Hot Tea\t\t{self.hot_tea.get()}\t\t{self.hot_tea.get()*25}")

        if self.gell.get()!=0:
            self.soda.insert(END,f"\n Soda\t\t{self.soda.get()}\t\t{self.soda.get()*30}")

        if self.coffee.get()!=0:
            self.txtarea.insert(END,f"\n Coffee\t\t{self.coffee.get()}\t\t{self.coffee.get()*150}")

            
        self.txtarea.insert(END,f"\n=====================================")
        if self.cosmetic_tax.get()!="Rs. 0.0":
            self.txtarea.insert(END,f"\nCosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
        if self.grocery_tax.get()!="Rs. 0.0":
            self.txtarea.insert(END,f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}")
        if self.cold_drink_tax.get()!="Rs. 0.0":
            self.txtarea.insert(END,f"\nCold TDrinks Tax Tax\t\t\t{self.cold_drink_tax.get()}")
        self.txtarea.insert(END,f"\n=====================================")


        #self.txtarea.insert(END,f"\n Total Bill : \t\t\t{float(self.cosmetic_price+self.grocery_price+self.cold_drink_price+self.c_tax+self.g_tax+self.d_tax).get()}")
        #self.txtarea.insert(END,f"\n=====================================")






            







root=Tk()
obj = Bill_App(root)
root.mainloop()