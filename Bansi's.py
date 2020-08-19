import tkinter
from tkinter import*
import time
import datetime
import math,random
from tkinter import messagebox
import os

localtime=time.asctime(time.localtime(time.time()))


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x650+0+0")
        self.root.title("Restaurant Billing System")
        bg_color="#074463"
        title=Label(self.root,text="Bansiwala's General Store",bd=12,relief=GROOVE,
                    bg='#b2bec3',fg="#2d3436",font=('arial',30,'bold'),pady=2).pack(fill=X)
        #========================================================================================================
        #                             VARIABLES
        #========================================================================================================
        
        #======cosmetics===============
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        #======grocery=================
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        #======cold drinks==============
        self.mazza=IntVar()
        self.litchi=IntVar()
        self.frooti=IntVar()
        self.orange=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()
        #======total tax price===========
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drinks_price=StringVar()
        
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drinks_tax=StringVar()
        
        #======customer================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        
        self.bill_no=StringVar()
        x=random.randint(10000,99999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        #======customer================
        
        time=Label(root,font=('arial 20 bold'),text=localtime,fg='gold',bg=bg_color).pack(fill=X)

        #========================================================================================================
        #                             CUSTOMER DETAIL FRAME
        #========================================================================================================

        F1=LabelFrame(self.root,text="CUSTOMER DETAILS",bd=12,relief=GROOVE,font=('arial',15,'bold'),fg='gold',bg=bg_color)
        F1.place(x=0,y=100,relwidth=1)
            
        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font='arial 15',bd=3,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_lbl=Label(F1,text="Customer Contact",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt=Entry(F1,width=15,textvariable=self.c_phone,font='arial 15',bd=3,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font='arial 15',bd=3,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,command=self.find_bill,text="Search",width=10,bd=7,font=('arial', 18, 'bold'),padx=5)
        bill_btn.grid(row=0,column=6)

        #========================================================================================================
        #                             Cosmetics Frame
        #========================================================================================================

        F2=LabelFrame(self.root,text="COSMETICS",bd=12,relief=GROOVE,font=('arial',15,'bold'),fg='gold',bg=bg_color)
        F2.place(x=0,y=174,width=335,height=335)

        bath_lbl=Label(F2,text="Bath Soap",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=15,textvariable=self.soap,font='arial 15',bd=3,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        Face_cream_lbl=Label(F2,text="Face Cream",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=15,textvariable=self.face_cream,font='arial 15',bd=3,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        Face_w_lbl=Label(F2,text="Face Wash",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt=Entry(F2,width=15,textvariable=self.face_wash,font='arial 15',bd=3,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        Hair_s_lbl=Label(F2,text="Hair Spray",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt=Entry(F2,width=15,textvariable=self.spray,font='arial 15',bd=3,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        Hair_g_lbl=Label(F2,text="Hair Gel",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_txt=Entry(F2,width=15,textvariable=self.gell,font='arial 15',bd=3,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        Body_lbl=Label(F2,text="Body Loshan",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_txt=Entry(F2,width=15,textvariable=self.loshan,font='arial 15',bd=3,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

        #========================================================================================================
        #                             GROCERY FRAME
        #========================================================================================================

        F3=LabelFrame(self.root,text="GROCERY",bd=12,relief=GROOVE,font=('arial',15,'bold'),fg='gold',bg=bg_color)
        F3.place(x=335,y=174,width=300,height=335)

        g1_lbl=Label(F3,text="Rice",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=15,textvariable=self.rice,font='arial 15',bd=3,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        g2_lbl=Label(F3,text="Food Oil",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=15,textvariable=self.food_oil,font='arial 15',bd=3,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        g3_lbl=Label(F3,text="Daal",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=15,textvariable=self.daal,font='arial 15',bd=3,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        g4_lbl=Label(F3,text="Wheat",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=15,textvariable=self.wheat,font='arial 15',bd=3,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        g5_lbl=Label(F3,text="Sugar",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=15,textvariable=self.sugar,font='arial 15',bd=3,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        g6_lbl=Label(F3,text="Tea",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=15,textvariable=self.tea,font='arial 15',bd=3,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
        #========================================================================================================
        #                             COLD DRINKS
        #========================================================================================================

        
        F4=LabelFrame(self.root,text="COLD DRINKS",bd=12,relief=GROOVE,font=('arial',15,'bold'),fg='gold',bg=bg_color)
        F4.place(x=635,y=174,width=300,height=335)

        c1_lbl=Label(F4,text="Maaza",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=15,textvariable=self.mazza,font='arial 15',bd=3,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        c2_lbl=Label(F4,text="Litchi",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=15,textvariable=self.litchi,font='arial 15',bd=3,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        c3_lbl=Label(F4,text="Frooti",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=15,textvariable=self.frooti,font='arial 15',bd=3,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        c4_lbl=Label(F4,text="Orange",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=15,textvariable=self.orange,font='arial 15',bd=3,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        c5_lbl=Label(F4,text="Limca",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=15,textvariable=self.limca,font='arial 15',bd=3,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        c6_lbl=Label(F4,text="Sprite",bg=bg_color,fg='white',font=('arial',18,'bold')).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=15,textvariable=self.sprite,font='arial 15',bd=3,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

        #========================================================================================================
        #                             BILL AREA
        #========================================================================================================

        F5=Frame(self.root,bd=12,relief=GROOVE)
        F5.place(x=935,y=174,width=410,height=335)
        bill_title=Label(F5,text='Bill Area',font=('arial 15 bold'),bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)      
        #========================================================================================================
        #                             BUTTON FRAME
        #========================================================================================================

        F6=LabelFrame(self.root,text="Bill Menu",bd=12,relief=GROOVE,font=('arial',15,'bold'),fg='gold',bg=bg_color)
        F6.place(x=0,y=510,relwidth=1,height=142)
        
        m1_lbl=Label(F6,text='Cost of Cosmetics',bg=bg_color,fg="white",font=('arial',15,'bold')).grid(row=1,column=0,padx=5,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font=('arial',10,'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text='Cost of Grocery',bg=bg_color,fg="white",font=('arial',15,'bold')).grid(row=2,column=0,padx=5,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font=('arial',10,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text='Cost of Cold Drinks',bg=bg_color,fg="white",font=('arial',15,'bold')).grid(row=3,column=0,padx=5,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drinks_price,font=('arial',10,'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text='Cosmetic Tax',bg=bg_color,fg="white",font=('arial',15,'bold')).grid(row=1,column=2,padx=5,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font=('arial',10,'bold'),bd=5,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text='Grocery Tax',bg=bg_color,fg="white",font=('arial',15,'bold')).grid(row=2,column=2,padx=5,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font=('arial',10,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text='Cold Drinks Tax',bg=bg_color,fg="white",font=('arial',15,'bold')).grid(row=3,column=2,padx=5,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.cold_drinks_tax,font=('arial',10,'bold'),bd=5,relief=SUNKEN).grid(row=3,column=3,padx=10,pady=1)



        #m5_lbl=Label(F6,text='Total Amount',bg=bg_color,fg="white",font=('arial',15,'bold')).grid(row=2,column=4,padx=5,pady=1,sticky="w")
        #m5_txt=Entry(F6,width=18,textvariable=self.total_amount,font=('arial',10,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=5,padx=10,pady=1)


        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=820,y=15,width=470,height=80)

        total_btn=Button(btn_F,command=self.total,text='Total',bg=bg_color,fg="black",pady=15,width=11,font='arial 15 bold').grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text='Generate Bill',command=self.bill_area,bg="#b2bec3",fg="black",pady=15,width=11,font='arial 15 bold').grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,command=self.clear_data,text='Clear',bg="#b2bec3",fg="black",pady=15,width=11,font='arial 15 bold').grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,command=self.Exit_app,text='Exit',bg="#b2bec3",fg="black",pady=15,width=11,font='arial 15 bold').grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

        #========================================================================================================
        #                             PROGRAM
        #========================================================================================================

    def total(self):
        self.c_s_p=self.soap.get()*30
        self.c_fc_p=self.face_cream.get()*50
        self.c_fw_p=self.face_wash.get()*100
        self.c_hs_p=self.spray.get()*70
        self.c_hg_p=self.gell.get()*30
        self.c_bl_p=self.loshan.get()*60
                     
        self.total_cosmetic_price=float(
                                     self.c_s_p+
                                     self.c_fc_p+
                                     self.c_fw_p+
                                     self.c_hs_p+
                                     self.c_hg_p+
                                     self.c_bl_p
                                    )
        self.cosmetic_price.set("Rs."+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs."+str(self.c_tax))



        self.g_r_p=self.rice.get()*180
        self.g_f_p=self.food_oil.get()*180
        self.g_d_p=self.daal.get()*200
        self.g_w_p=self.wheat.get()*240
        self.g_s_p=self.sugar.get()*45
        self.g_t_p=self.tea.get()*100

        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_f_p+
                                    self.g_d_p+
                                    self.g_w_p+
                                    self.g_s_p+
                                    self.g_t_p
                                    )
        self.grocery_price.set("Rs."+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.01),2)
        self.grocery_tax.set("Rs."+str(self.g_tax))



        self.d_m_p=self.mazza.get()*40
        self.d_l_p=self.litchi.get()*30
        self.d_f_p=self.frooti.get()*20
        self.d_o_p=self.orange.get()*50
        self.d_l_p=self.limca.get()*50
        self.d_s_p=self.sprite.get()*40
        
 
        self.total_drinks_price=float(
                                    self.d_m_p+
                                    self.d_l_p+
                                    self.d_f_p+
                                    self.d_o_p+
                                    self.d_l_p+
                                    self.d_s_p
                                    )
        self.cold_drinks_price.set("Rs."+str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price*0.05),2)
        self.cold_drinks_tax.set("Rs."+str(self.d_tax))

        self.Total_bill=float(self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_drinks_price+
                              self.c_tax+
                              self.g_tax+
                              self.d_tax
                            ) 
        



    def welcome_bill(self):
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END,"\t     Bansiwala's General Store")
        self.txtarea.insert(END,f"\nBill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone Number : {self.c_phone.get()} ")
        self.txtarea.insert(END,f"\n===================================================")
        self.txtarea.insert(END,f"\n Products\t\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n===================================================")

        
    def bill_area(self):

        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer Details are must!")


        else:
            self.welcome_bill()
            #============cosmetics=============
            
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t\t{self.soap.get()}\t\t{self.c_s_p}")

            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")

            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")

            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair spray\t\t\t{self.spray.get()}\t\t{self.c_hs_p}")

            if self.gell.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gell\t\t\t{self.gell.get()}\t\t{self.c_hg_p}")

            if self.loshan.get()!=0:
                self.txtarea.insert(END,f"\n Body loshan\t\t\t{self.loshan.get()}\t\t{self.c_bl_p}")


            #============grocery=============
                
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice \t\t\t{self.rice.get()}\t\t{self.g_r_p}")

            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food oil\t\t\t{self.food_oil.get()}\t\t{self.g_f_p}")

            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t\t{self.daal.get()}\t\t{self.g_d_p}")

            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t\t{self.wheat.get()}\t\t{self.g_w_p}")

            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t\t{self.sugar.get()}\t\t{self.g_s_p}")

            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t\t{self.tea.get()}\t\t{self.g_t_p}")



            #============Cold Drinks=============
                
            if self.mazza.get()!=0:
                self.txtarea.insert(END,f"\n Mazza \t\t\t{self.mazza.get()}\t\t{self.d_m_p}")

            if self.litchi.get()!=0:
                self.txtarea.insert(END,f"\n Litchi\t\t\t{self.litchi.get()}\t\t{self.d_l_p}")

            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t\t{self.frooti.get()}\t\t{self.d_f_p}")

            if self.orange.get()!=0:
                self.txtarea.insert(END,f"\n Orange\t\t\t{self.orange.get()}\t\t{self.d_o_p}")

            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t\t{self.limca.get()}\t\t{self.d_l_p}")

            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t\t{self.sprite.get()}\t\t{self.d_s_p}")



            self.txtarea.insert(END,f"\n---------------------------------------------------")
            
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nCosmetics Tax\t\t\t\t\t{self.cosmetic_tax.get()}")

            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nGrosery Tax\t\t\t\t\t{self.grocery_tax.get()}")

            if self.cold_drinks_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nCold Drink Tax\t\t\t\t\t{self.cold_drinks_tax.get()}")

            self.txtarea.insert(END,f"\n---------------------------------------------------")

            self.txtarea.insert(END,f"\nTotal Bill:\t\t\t\t\tRs.{str(self.Total_bill)}")

            
            self.txtarea.insert(END,f"\n---------------------------------------------------")

            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op > 0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill Number: {self.bill_no.get()} Saved Successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill Number")

    def clear_data(self):

        op=messagebox.askyesno("Clear","Do you want Clear Data?")
        if op > 0:
            
            #======cosmetics===============
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)
            #======grocery=================
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            #======cold drinks==============
            self.mazza.set(0)
            self.litchi.set(0)
            self.frooti.set(0)
            self.orange.set(0)
            self.limca.set(0)
            self.sprite.set(0)
            #======total tax price===========
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")
            
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")
            
            #======customer================
            self.c_name.set("")
            self.c_phone.set("")
            
            self.bill_no.set("")
            x=random.randint(10000,99999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
            #======customer================

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want Exit")
        if op > 0:
            self.root.destroy()
            
        #========================================================================================================
        #                             PROGRAM EXIT
        #========================================================================================================
    
            
root=Tk()
obj=Bill_App(root)
root.mainloop()
                    
        
