from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='blue')

        title=Label(self.root,text='Student Management System',font=('times new roman',40,'bold'),bg='yellow',fg='red',bd=10,relief=GROOVE)
        title.pack(side=TOP,fill=X)

        # All Variable------------------------
        self.Roll_no=StringVar()
        self.Name_var=StringVar()
        self.Email_var=StringVar()
        self.Gender_var=StringVar()
        self.Contect_var=StringVar()
        self.DOB_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        #-------------------------------------------Manage frame-------------------------------
        Manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg='red')
        Manage_frame.place(x=20,y=100,width=450,height=580)
        m_title=Label(Manage_frame,text='Manage Student',font=('times new roman',30,'bold'),bg='red',fg='white')
        m_title.grid(row=0,columnspan=2,pady=20)
        # roll part-------------------------------------------------------------------------------------------
        lbl_roll = Label(Manage_frame, text='Roll No.', font=('times new roman', 20, 'bold'), bg='red',fg='white')
        lbl_roll.grid(row=1, column=0, padx=20,pady=5,sticky=W)
        text_roll=Entry(Manage_frame,font=('times new roman',15),bd=5,relief=GROOVE,textvariable=self.Roll_no)
        text_roll.grid(row=1,column=1,pady=5,padx=20,sticky=W)
        text_roll.focus()
        # name part ---------------------------------------------------------------------------------------
        lbl_name = Label(Manage_frame, text='Name ', font=('times new roman', 20, 'bold'), bg='red', fg='white')
        lbl_name.grid(row=2, column=0, padx=20, pady=5, sticky=W)
        text_name = Entry(Manage_frame, font=('times new roman', 15), bd=5, relief=GROOVE,textvariable=self.Name_var)
        text_name.grid(row=2, column=1, pady=5, padx=20, sticky=W)
        # Email part --------------------------------------------------------------------------
        lbl_email = Label(Manage_frame, text='Email', font=('times new roman', 20, 'bold'), bg='red', fg='white')
        lbl_email.grid(row=3, column=0, padx=20, pady=5, sticky=W)
        text_email = Entry(Manage_frame, font=('times new roman', 15), bd=5, relief=GROOVE,textvariable=self.Email_var)
        text_email.grid(row=3, column=1, pady=5, padx=20, sticky=W)
        # Gender part-------------------------------------------------------------------------------------
        lbl_gender = Label(Manage_frame, text='Gender', font=('times new roman', 20, 'bold'), bg='red', fg='white')
        lbl_gender.grid(row=4, column=0, padx=20, pady=5, sticky=W)
        combo_box=ttk.Combobox(Manage_frame,font=('times new roman',15),width=19,state='readonly',justify=CENTER,textvariable=self.Gender_var)
        combo_box['values']=('Male','Female','Another')
        combo_box.grid(row=4,column=1,sticky=W,padx=20,pady=5)
        combo_box.current(0)
        # contect part---------------------------------------------------------------------------------------
        lbl_contect = Label(Manage_frame, text='Contect', font=('times new roman', 20, 'bold'), bg='red', fg='white')
        lbl_contect.grid(row=5, column=0, padx=20, pady=5, sticky=W)
        text_contect = Entry(Manage_frame, font=('times new roman', 15), bd=5, relief=GROOVE,textvariable=self.Contect_var)
        text_contect.grid(row=5, column=1, pady=5, padx=20, sticky=W)
        #Date of birth part---------------------------------------------------------------------------
        lbl_dob = Label(Manage_frame, text='D.O.B', font=('times new roman', 20, 'bold'), bg='red', fg='white')
        lbl_dob.grid(row=6, column=0, padx=20, pady=5, sticky=W)
        text_dob = Entry(Manage_frame, font=('times new roman', 15), bd=5, relief=GROOVE,textvariable=self.DOB_var)
        text_dob.grid(row=6, column=1, pady=5, padx=20, sticky=W)
        # address part------------------------------------------------------------------------------------------
        lbl_address = Label(Manage_frame, text='Address', font=('times new roman', 20, 'bold'), bg='red', fg='white')
        lbl_address.grid(row=7, column=0, padx=20, pady=5, sticky=W)
        self.text_address=Text(Manage_frame,width=26,height=5)
        self.text_address.grid(row=7,column=1,padx=20,pady=5,sticky=W)
        # button frame---------------------------------------------------------
        btn_frame=Frame(Manage_frame,bd=5,relief=RIDGE,bg='blue')
        btn_frame.place(x=15,y=500,width=410)
        Add_btn=Button(btn_frame,text='Add',width=10,height=2,bg='green',command=self.Add_students).grid(row=0,column=0,padx=10,pady=5)
        update_btn = Button(btn_frame, text='Update', width=10,height=2,bg='yellow',command=self.update).grid(row=0, column=1, padx=10, pady=5)
        delete_btn = Button(btn_frame, text='Delete', width=10,height=2,bg='red',command=self.Delete).grid(row=0, column=2, padx=10, pady=5)
        clear_btn = Button(btn_frame, text='Clear', width=10,height=2,command=self.clear).grid(row=0, column=3, padx=10, pady=5)




        #------------------------Detail frame---------------------------------------------------
        Detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg='red')
        Detail_frame.place(x=500, y=100, width=825, height=580)
        lbl_search=Label(Detail_frame,text='Search By',bg='red',fg='white',font=('times new roman',20,'bold'))
        lbl_search.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        # search part------------------------------
        combo_search = ttk.Combobox(Detail_frame, font=('times new roman', 17), width=12, state='readonly',justify=CENTER,textvariable=self.search_by)
        combo_search['values'] = ('Roll_no', 'Name', 'Contact')
        combo_search.grid(row=0, column=1, sticky=W, padx=10, pady=10)
        combo_search.current(0)
        txt_search=Entry(Detail_frame,font=('time new roman',14,'bold'),width=15,bd=5,relief=GROOVE,textvariable=self.search_txt)
        txt_search.grid(row=0,column=2,pady=5,padx=10,sticky=W)
        search_btn = Button(Detail_frame, text='Search', width=10,font=('time new roman',15),command=self.search_data).grid(row=0, column=3, padx=10,pady=10)
        showall_btn = Button(Detail_frame, text='Show All', width=10,font=('time new roman',15),command=self.Fetch_data).grid(row=0, column=4, padx=10,pady=10)

        # table frame-------------------------------------------------------------------------------------------------------------------------------------------------------
        Table_frame=Frame(Detail_frame,bd=4,relief=RIDGE,bg='red')
        Table_frame.place(x=10,y=70,width=790,height=490)
        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_frame,columns=('Roll','Name','Email','Gender','Contect','D.O.B','Address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fil=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading('Roll',text="Roll No.")
        self.student_table.heading('Name', text="Name")
        self.student_table.heading('Email', text="Email")
        self.student_table.heading('Gender', text="Gender")
        self.student_table.heading('Contect', text="Contect")
        self.student_table.heading('D.O.B',text='D.O.B')
        self.student_table.heading('Address', text="Address")
        self.student_table['show']='headings'
        self.student_table.column('Roll',width=150)
        self.student_table.column('Name', width=200)
        self.student_table.column('Email', width=250)
        self.student_table.column('Gender', width=68)
        self.student_table.column('Contect', width=100)
        self.student_table.column('D.O.B', width=100)
        self.student_table.column('Address', width=500)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.Fetch_data()
    def Add_students(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()
        if self.Roll_no.get()=='' or self.Name_var.get()=='' or self.Email_var.get()=='' or self.Contect_var.get()=='' or self.DOB_var.get()=='':
            messagebox.showerror('Error ','All fields are required!!!!!')
        else:
            cur.execute('insert into students values(%s,%s,%s,%s,%s,%s,%s)',(
                self.Roll_no.get(),
                self.Name_var.get().title(),
                self.Email_var.get().lower(),
                self.Gender_var.get(),
                self.Contect_var.get(),
                self.DOB_var.get(),
                self.text_address.get('1.0',END).title()
            ))
            con.commit()
            self.Fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo('Success','Record has been inserted !!!')
    def Fetch_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()
        cur.execute('select * from students')
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.Roll_no.set('')
        self.Name_var.set('')
        self.Email_var.set('')
        self.Gender_var.set('Male')
        self.Contect_var.set('')
        self.DOB_var.set('')
        self.text_address.delete('1.0',END)

    def get_cursor(self,a):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content['values']
        self.Roll_no.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contect_var.set(row[4])
        self.DOB_var.set(row[5])
        self.text_address.delete('1.0', END)
        self.text_address.insert(END,row[6])
    def update(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='stm')
        cur = con.cursor()
        cur.execute('update students set Name=%s,Email=%s,Gender=%s,Contact=%s,DOB=%s,Address=%s where Roll_no=%s',(
            self.Name_var.get().title(),
            self.Email_var.get().lower(),
            self.Gender_var.get(),
            self.Contect_var.get(),
            self.DOB_var.get(),
            self.text_address.get('1.0', END).title(),
            self.Roll_no.get()
        ))
        con.commit()
        self.Fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo('Update', 'Record has been Updated')
    def Delete(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()
        cur.execute('delete from students where Roll_no=%s',self.Roll_no.get())
        con.commit()
        con.close()
        self.Fetch_data()
        self.clear()
        messagebox.showinfo('Delete','Record has been Deleted')
    def search_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

root=Tk()
ob=Student(root)
root.mainloop()