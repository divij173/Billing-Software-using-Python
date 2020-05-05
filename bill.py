from tkinter import*
import math,random
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#3498DB"
        title=Label(self.root,text="Billing Software",bd=13,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        #=======Variables
                     #====Chocolates 
        self.snic=IntVar()
        self.kitk=IntVar()
        self.cadb=IntVar()
        self.tobl=IntVar()
        self.hers=IntVar()
        self.mars=IntVar()
                     #====Chips
        self.lays=IntVar()
        self.kurk=IntVar()
        self.chee=IntVar()
        self.bing=IntVar()
        self.dori=IntVar()
        self.prin=IntVar()
                     #====Cold Drinks
        self.coke=IntVar()
        self.moun=IntVar()
        self.spri=IntVar()
        self.froo=IntVar()
        self.fizz=IntVar()
        self.fant=IntVar()
                     #==== Total price & Tax
        self.choc_price=StringVar()
        self.chip_price=StringVar()
        self.cold_price=StringVar()

        self.choc_tax=StringVar()
        self.chip_tax=StringVar()
        self.cold_tax=StringVar()
                     #==== Customer
        self.c_name=StringVar()
        self.c_phon=StringVar()
        
        self.bill_no=StringVar()
        x=random.randint(1000000,9999999)
        self.bill_no.set(str(x))
        
        self.search_bill=StringVar()
        


        #======Customer Detail Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15", bd=7,relief=SUNKEN ).grid(row=0,column=1,padx=10,pady=5)

        cphn_lbl=Label(F1,text="Contact No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15", bd=7,relief=SUNKEN ).grid(row=0,column=3,padx=10,pady=5)

        c_bill_lbl=Label(F1,text="Bill No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15", bd=7,relief=SUNKEN ).grid(row=0,column=5,padx=10,pady=5)

        bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)




        #=========Chocolates Freame
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Chocolates",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        snic_lbl=Label(F2,text="Snickers",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        snic_txt=Entry(F2,width=10,textvariable=self.snic,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        kitk_lbl=Label(F2,text="Kit Kat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        kitk_txt=Entry(F2,width=10,textvariable=self.kitk,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        cadb_lbl=Label(F2,text="Cadbury",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        cadb_txt=Entry(F2,width=10,textvariable=self.cadb,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        tobl_lbl=Label(F2,text="Toblerone",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        tobl_txt=Entry(F2,width=10,textvariable=self.tobl,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hers_lbl=Label(F2,text="Hershey's",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hers_txt=Entry(F2,width=10,textvariable=self.hers,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        mars_lbl=Label(F2,text="Mars",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        mars_txt=Entry(F2,width=10,textvariable=self.mars,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)




        #=========Chips Freame
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Chips",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)

        lays_lbl=Label(F3,text="Lays",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        lays_txt=Entry(F3,width=10,textvariable=self.lays,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        kurk_lbl=Label(F3,text="Kurkure",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        kurk_txt=Entry(F3,width=10,textvariable=self.kurk,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        chee_lbl=Label(F3,text="Cheetos",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        chee_txt=Entry(F3,width=10,textvariable=self.chee,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        bing_lbl=Label(F3,text="Bingo",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        bing_txt=Entry(F3,width=10,textvariable=self.bing,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        dori_lbl=Label(F3,text="Doritos",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        dori_txt=Entry(F3,width=10,textvariable=self.dori,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        prin_lbl=Label(F3,text="Pringles",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        prin_txt=Entry(F3,width=10,textvariable=self.prin,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)




         #=========Cold Drinks Freame
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=180,width=325,height=380)

        coke_lbl=Label(F4,text="Coke",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        coke_txt=Entry(F4,width=10,textvariable=self.coke,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        moun_lbl=Label(F4,text="Mountain Dew",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        moun_txt=Entry(F4,width=10,textvariable=self.moun,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        spri_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        spri_txt=Entry(F4,width=10,textvariable=self.spri,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        froo_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        froo_txt=Entry(F4,width=10,textvariable=self.froo,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        fizz_lbl=Label(F4,text="Fizz",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        fizz_txt=Entry(F4,width=10,textvariable=self.fizz,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        fant_lbl=Label(F4,text="Fanta",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        fant_txt=Entry(F4,width=10,textvariable=self.fant,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)




        #=========Bill Area Frame
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=350,height=380)
        bill_title=Label(F5,text="Bill Area",font="areal 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)




        #======Button Frame
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
        m1=Label(F6,text="Total Chocolate Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.choc_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2=Label(F6,text="Total Chips Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.chip_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3=Label(F6,text="Total Cold Drinks Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        c1=Label(F6,text="Chocolate Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.choc_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2=Label(F6,text="Chips Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.chip_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3=Label(F6,text="Cold Drinks Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.cold_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)


        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        gbill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_F,text="Clear",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    
    def total(self):

        self.c_s_p=self.snic.get()*80
        self.c_k_p=self.kitk.get()*70
        self.c_c_p=self.cadb.get()*120
        self.c_t_p=self.tobl.get()*140
        self.c_h_p=self.hers.get()*130
        self.c_m_p=self.mars.get()*170
        
        self.total_choc_price=float(
                                     self.c_s_p+
                                     self.c_k_p+
                                     self.c_c_p+
                                     self.c_t_p+
                                     self.c_h_p+
                                     self.c_m_p
                                   )
        self.choc_price.set(str(self.total_choc_price))
        self.cho_tax=round((self.total_choc_price*0.05),2)
        self.choc_tax.set(str(self.cho_tax))


        self.c_la_p=self.lays.get()*40
        self.c_ku_p=self.kurk.get()*35
        self.c_ch_p=self.chee.get()*20
        self.c_bi_p=self.bing.get()*25
        self.c_do_p=self.dori.get()*60
        self.c_pr_p=self.prin.get()*70

        self.total_chip_price=float(
                                     self.c_la_p+
                                     self.c_ku_p+
                                     self.c_ch_p+
                                     self.c_bi_p+
                                     self.c_do_p+
                                     self.c_pr_p
                                   )
        self.chip_price.set(str(self.total_chip_price))
        self.chi_tax=round((self.total_chip_price*0.1),2)
        self.chip_tax.set(str(self.chi_tax))
         
        self.c_cok_p=self.coke.get()*90
        self.c_mou_p=self.moun.get()*85
        self.c_spr_p=self.spri.get()*80
        self.c_fro_p=self.froo.get()*80
        self.c_fiz_p=self.fizz.get()*65
        self.c_fan_p=self.fant.get()*70


 
        self.total_cold_price=float(
                                     self.c_cok_p+
                                     self.c_mou_p+
                                     self.c_spr_p+
                                     self.c_fro_p+
                                     self.c_fiz_p+
                                     self.c_fan_p
                                   )
        self.cold_price.set(str(self.total_cold_price))
        self.col_tax=round((self.total_cold_price*0.18),2)
        self.cold_tax.set(str(self.col_tax))

        self.total_bill=float(self.total_choc_price + self.cho_tax + self.total_chip_price + self.chi_tax + self.total_cold_price + self.col_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t     Retail Invoice\n\n\t  JALEBI PHAPHDA WORLD\n")
        self.txtarea.insert(END,"--------------------------------------")
        self.txtarea.insert(END,f"\nBill No: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone No: {self.c_phon.get()}")    
        self.txtarea.insert(END,"\n======================================")
        self.txtarea.insert(END,"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END,"\n======================================")


    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Details are must")
        elif self.choc_price.get()=="0.0" and self.chip_price=="0.0" and self.cold_price=="0.0":
            messagebox.showerror("Error","No Product Purchased")
        else:
            self.welcome_bill()
            #=====Choclate
            if self.snic.get()!=0:
                self.txtarea.insert(END,f"\n Snicker\t\t{self.snic.get()}\t\t{self.c_s_p}")
            if self.kitk.get()!=0:
                self.txtarea.insert(END,f"\n KitKat\t\t{self.kitk.get()}\t\t{self.c_k_p}")
            if self.cadb.get()!=0:
                self.txtarea.insert(END,f"\n Cadbury\t\t{self.cadb.get()}\t\t{self.c_c_p}")
            if self.tobl.get()!=0:
                self.txtarea.insert(END,f"\n Toblerone\t\t{self.tobl.get()}\t\t{self.c_t_p}")
            if self.hers.get()!=0:
                self.txtarea.insert(END,f"\n Hersheys\t\t{self.hers.get()}\t\t{self.c_h_p}")
            if self.mars.get()!=0:
                self.txtarea.insert(END,f"\n Mars\t\t{self.mars.get()}\t\t{self.c_m_p}")
            

            #====Chips
            if self.lays.get()!=0:
                self.txtarea.insert(END,f"\n Lays\t\t{self.lays.get()}\t\t{self.c_la_p}")
            if self.kurk.get()!=0:
                self.txtarea.insert(END,f"\n Kurkure\t\t{self.kurk.get()}\t\t{self.c_ku_p}")
            if self.chee.get()!=0:
                self.txtarea.insert(END,f"\n Cheetos\t\t{self.chee.get()}\t\t{self.c_ch_p}")
            if self.bing.get()!=0:
                self.txtarea.insert(END,f"\n Bingo\t\t{self.bing.get()}\t\t{self.c_bi_p}")
            if self.dori.get()!=0:
                self.txtarea.insert(END,f"\n Doritos\t\t{self.dori.get()}\t\t{self.c_do_p}")
            if self.prin.get()!=0:
                self.txtarea.insert(END,f"\n Pringles\t\t{self.prin.get()}\t\t{self.c_pr_p}")


            #====Cold Drinks
            if self.coke.get()!=0:
                self.txtarea.insert(END,f"\n Coke\t\t{self.coke.get()}\t\t{self.c_cok_p}")
            if self.moun.get()!=0:
                self.txtarea.insert(END,f"\n Mountain Dew\t\t{self.moun.get()}\t\t{self.c_mou_p}")
            if self.spri.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.spri.get()}\t\t{self.c_spr_p}")
            if self.froo.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.froo.get()}\t\t{self.c_fro_p}")
            if self.fizz.get()!=0:
                self.txtarea.insert(END,f"\n Fizz\t\t{self.fizz.get()}\t\t{self.c_fiz_p}")
            if self.fant.get()!=0:
                self.txtarea.insert(END,f"\n Fanta\t\t{self.fant.get()}\t\t{self.c_fan_p}")
            


            self.txtarea.insert(END,"\n--------------------------------------")
            if self.choc_tax.get()!="0.0":
               self.txtarea.insert(END,f"\n Chocolate Tax\t\t\t\t{self.choc_tax.get()}")
            if self.chip_tax.get()!="0.0":
               self.txtarea.insert(END,f"\n Chips Tax\t\t\t\t{self.chip_tax.get()}")
            if self.cold_tax.get()!="0.0":
               self.txtarea.insert(END,f"\n Cold Drink Tax\t\t\t\t{self.cold_tax.get()}")
            
            self.txtarea.insert(END,f"\n Total Bill\t\t\t\t{self.total_bill}")
            self.txtarea.insert(END,"\n--------------------------------------")

    

root=Tk()
obj=Bill_App(root)
root.mainloop()