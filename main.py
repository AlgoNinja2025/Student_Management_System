import tkinter as tk
from tkinter import ttk, messagebox
import pymysql

# ------------------- Student Record Management System -------------------

class std():
    def __init__(self,root):
        self.root = root
        self.root.title("Student Record")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        # Modern title bar
        title = tk.Label(self.root, text="Student Record Management System", bd=0, relief="flat", 
                         bg="#3a7ca5", fg="white", font=("Segoe UI", 38, "bold"), pady=20)
        title.pack(side="top", fill="x")

        # option frame
        optFrame = tk.Frame(self.root, bd=0, relief="flat", bg="#e3eafc")
        optFrame.place(width=self.width/3, height=self.height-180, x=50, y=100)

        btn_style = {"bd":0, "relief":"flat", "bg":"#3a7ca5", "fg":"white", "activebackground":"#28527a", 
                     "activeforeground":"white", "width":20, "font":("Segoe UI", 20, "bold"), "cursor":"hand2"}

        addBtn = tk.Button(optFrame,command=self.addFrameFun, text="Add Student", **btn_style)
        addBtn.grid(row=0, column=0, padx=30, pady=30, sticky="ew")

        srchBtn = tk.Button(optFrame,command=self.searchFrameFun, text="Search Student", **btn_style)
        srchBtn.grid(row=1, column=0, padx=30, pady=30, sticky="ew")

        updBtn = tk.Button(optFrame, command=self.updFrameFun,text="Update Record", **btn_style)
        updBtn.grid(row=2, column=0, padx=30, pady=30, sticky="ew")

        allBtn = tk.Button(optFrame,command=self.showAll, text="Show All", **btn_style)
        allBtn.grid(row=3, column=0, padx=30, pady=30, sticky="ew")

        delBtn = tk.Button(optFrame,command=self.delFrameFun, text="Remove Student", **btn_style)
        delBtn.grid(row=4, column=0, padx=30, pady=30, sticky="ew")
    
        # detail Frame
        self.detFrame = tk.Frame(self.root, bd=0, relief="flat", bg="#f6f9fb")
        self.detFrame.place(width=self.width/2+50, height=self.height-180, x=self.width/3+100, y=100)

        lbl = tk.Label(self.detFrame, text="Record Details", font=("Segoe UI", 28, "bold"),bg="#f6f9fb", fg="#28527a")
        lbl.pack(side="top", fill="x", pady=10)

        self.tabFun()

    def tabFun(self):
        tabFrame = tk.Frame(self.detFrame, bd=0, relief="flat", bg="#f6f9fb")
        tabFrame.place(width=self.width/2, height=self.height-280, x=23,y=70 )

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#f6f9fb", foreground="#28527a", rowheight=35, fieldbackground="#f6f9fb", font=("Segoe UI", 14))
        style.configure("Treeview.Heading", font=("Segoe UI", 16, "bold"), background="#3a7ca5", foreground="white")
        style.map('Treeview', background=[('selected', '#b4d2e7')])

        x_scrol = tk.Scrollbar(tabFrame, orient="horizontal")
        x_scrol.pack(side="bottom", fill="x")

        y_scrol = tk.Scrollbar(tabFrame, orient="vertical")
        y_scrol.pack(side="right", fill="y")

        self.table = ttk.Treeview(tabFrame, xscrollcommand=x_scrol.set, yscrollcommand=y_scrol.set,
                                  columns=("roll","name","fname","sub","grade"))
        
        x_scrol.config(command=self.table.xview)
        y_scrol.config(command=self.table.yview)

        self.table.heading("roll", text="Roll No")
        self.table.heading("name", text="Name")
        self.table.heading("fname", text="Father Name")
        self.table.heading("sub", text="Subject")
        self.table.heading("grade", text="Grade")
        self.table["show"]= "headings"
        
        self.table.pack(fill="both", expand=1, padx=10, pady=10)

    def addFrameFun(self):
        self.addFrame = tk.Frame(self.root, bd=0, relief="flat", bg="#e3eafc")
        self.addFrame.place(width=self.width/3, height=self.height-180, x=self.width/3+80, y=100)

        lbl_style = {"bg":"#e3eafc", "font":("Segoe UI",15,"bold"), "fg":"#28527a"}
        entry_style = {"width":18, "font":("Segoe UI",15,"bold"), "bd":2}

        rnLbl = tk.Label(self.addFrame, text="Roll No:", **lbl_style)
        rnLbl.grid(row=0, column=0, padx=20, pady=25, sticky="e")
        self.rollNo = tk.Entry(self.addFrame, **entry_style)
        self.rollNo.grid(row=0, column=1, padx=10, pady=25)

        nameLbl = tk.Label(self.addFrame, text="Name:", **lbl_style)
        nameLbl.grid(row=1, column=0, padx=20, pady=25, sticky="e")
        self.name = tk.Entry(self.addFrame, **entry_style)
        self.name.grid(row=1, column=1, padx=10, pady=25)

        fLbl = tk.Label(self.addFrame, text="Father Name:", **lbl_style)
        fLbl.grid(row=2, column=0, padx=20, pady=25, sticky="e")
        self.fname = tk.Entry(self.addFrame, **entry_style)
        self.fname.grid(row=2, column=1, padx=10, pady=25)

        subLbl = tk.Label(self.addFrame, text="Subject:", **lbl_style)
        subLbl.grid(row=3, column=0, padx=20, pady=25, sticky="e")
        self.sub = tk.Entry(self.addFrame, **entry_style)
        self.sub.grid(row=3, column=1, padx=10, pady=25)

        gLbl = tk.Label(self.addFrame, text="Grade:", **lbl_style)
        gLbl.grid(row=4, column=0, padx=20, pady=25, sticky="e")
        self.grade = tk.Entry(self.addFrame, **entry_style)
        self.grade.grid(row=4, column=1, padx=10, pady=25)

        okBtn = tk.Button(self.addFrame,command=self.addFun, text="Enter", 
                          bg="#3a7ca5", fg="white", activebackground="#28527a", activeforeground="white",
                          font=("Segoe UI",20,"bold"), bd=0, width=20, cursor="hand2")
        okBtn.grid(row=5, column=0, padx=30, pady=25, columnspan=2)

    def desAdd(self):
        self.addFrame.destroy()

    def addFun(self):
        rn = self.rollNo.get()
        name = self.name.get()
        fname = self.fname.get()
        sub = self.sub.get()
        grade = self.grade.get()

        if rn and name and fname and sub and grade:
            rNo = int(rn)
            try:
                self.dbFun()
                self.cur.execute("insert into student(rollNo,name,fname,sub,grade) values(%s,%s,%s,%s,%s)",(rNo,name,fname,sub,grade))
                self.con.commit()
                tk.messagebox.showinfo("Success", f"Student {name} with Roll_No.{rNo} is Registered!")
                self.desAdd()

                self.cur.execute("select * from student where rollNo=%s",rNo)
                row = self.cur.fetchone()
                self.table.delete(*self.table.get_children())
                self.table.insert('', tk.END, values=row)

                self.con.close()
            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")
                self.desAdd()
        else:
            tk.messagebox.showerror("Error", "Please Fill All Input Fields!")

    def searchFrameFun(self):
        self.addFrame = tk.Frame(self.root, bd=0, relief="flat", bg="#e3eafc")
        self.addFrame.place(width=self.width/3, height=self.height-350, x=self.width/3+80, y=100)

        lbl_style = {"bg":"#e3eafc", "font":("Segoe UI",15,"bold"), "fg":"#28527a"}
        entry_style = {"width":18, "font":("Segoe UI",15,"bold"), "bd":2}

        optLbl = tk.Label(self.addFrame, text="Select:", **lbl_style)
        optLbl.grid(row=0, column=0, padx=20, pady=25, sticky="e")
        self.option = ttk.Combobox(self.addFrame, width=17, values=("rollNo","Name","Sub"),font=("Segoe UI",15,"bold"))
        self.option.set("Select Option")
        self.option.grid(row=0, column=1, padx=10, pady=30)

        valLbl = tk.Label(self.addFrame, text="Value:", **lbl_style)
        valLbl.grid(row=1, column=0, padx=20, pady=25, sticky="e")
        self.value = tk.Entry(self.addFrame, **entry_style)
        self.value.grid(row=1, column=1, padx=10, pady=25)

        okBtn = tk.Button(self.addFrame,command=self.searchFun, text="Enter", 
                          bg="#3a7ca5", fg="white", activebackground="#28527a", activeforeground="white",
                          font=("Segoe UI",20,"bold"), bd=0, width=20, cursor="hand2")
        okBtn.grid(row=2, column=0, padx=30, pady=25, columnspan=2)

    def searchFun(self):
        opt = self.option.get()
        val = self.value.get()

        if opt == "rollNo":
            rn = int(val)
            try:
                self.dbFun()
                self.cur.execute("select * from student where rollNo=%s",rn)
                row = self.cur.fetchone()
                self.table.delete(*self.table.get_children())
                self.table.insert('',tk.END, values=row)

                self.desAdd()
                self.con.close()
            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")
        else:
            try:
                self.dbFun()
                query = f"select * from student where {opt}=%s "
                self.cur.execute(query,(val))
                data = self.cur.fetchall()
                self.table.delete(self.table.get_children())

                for i in data:
                    self.table.insert('',tk.END, values=i)

                self.desAdd()
                self.con.close()    
            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")

    def dbFun(self):
        self.con = pymysql.connect(host="localhost", user="root", passwd="Basanta@2005", database="rec")
        self.cur = self.con.cursor()

    def updFrameFun(self):
        self.addFrame = tk.Frame(self.root, bd=0, relief="flat", bg="#e3eafc")
        self.addFrame.place(width=self.width/3, height=self.height-300, x=self.width/3+80, y=100)

        lbl_style = {"bg":"#e3eafc", "font":("Segoe UI",15,"bold"), "fg":"#28527a"}
        entry_style = {"width":18, "font":("Segoe UI",15,"bold"), "bd":2}

        optLbl = tk.Label(self.addFrame, text="Select:", **lbl_style)
        optLbl.grid(row=0, column=0, padx=20, pady=25, sticky="e")
        self.option = ttk.Combobox(self.addFrame, width=17, values=("Name","Sub","grade"),font=("Segoe UI",15,"bold"))
        self.option.set("Select Option")
        self.option.grid(row=0, column=1, padx=10, pady=30)

        valLbl = tk.Label(self.addFrame, text="New Value:", **lbl_style)
        valLbl.grid(row=1, column=0, padx=20, pady=25, sticky="e")
        self.value = tk.Entry(self.addFrame, **entry_style)
        self.value.grid(row=1, column=1, padx=10, pady=25)

        rollLbl = tk.Label(self.addFrame, text="Roll No:", **lbl_style)
        rollLbl.grid(row=2, column=0, padx=20, pady=25, sticky="e")
        self.roll = tk.Entry(self.addFrame, **entry_style)
        self.roll.grid(row=2, column=1, padx=10, pady=25)

        okBtn = tk.Button(self.addFrame,command=self.updFun, text="Enter", 
                          bg="#3a7ca5", fg="white", activebackground="#28527a", activeforeground="white",
                          font=("Segoe UI",20,"bold"), bd=0, width=20, cursor="hand2")
        okBtn.grid(row=3, column=0, padx=30, pady=25, columnspan=2)  

    def updFun(self):
        opt = self.option.get()
        val = self.value.get() 
        rNo = int(self.roll.get()) 

        try:
            self.dbFun()
            query = f"update student set {opt}=%s where rollNo=%s"
            self.cur.execute(query,(val,rNo))
            self.con.commit()
            tk.messagebox.showinfo("Success", f"Record is Updated for Student with Roll_No.{rNo}")
            self.desAdd()

            self.cur.execute("select * from student where rollNo=%s",rNo)
            row = self.cur.fetchone()

            self.table.delete(*self.table.get_children())
            self.table.insert('',tk.END, values=row)

            self.con.close()
             
        except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")

    def showAll(self):
        try:
            self.dbFun()
            self.cur.execute("select * from student")
            data = self.cur.fetchall()
            self.table.delete(*self.table.get_children())

            for i in data:
                self.table.insert('', tk.END, values=i)

            self.con.close()
        
        except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")

    def delFrameFun(self):
        self.addFrame = tk.Frame(self.root, bd=0, relief="flat", bg="#e3eafc")
        self.addFrame.place(width=self.width/3, height=self.height-400, x=self.width/3+80, y=100)

        lbl_style = {"bg":"#e3eafc", "font":("Segoe UI",15,"bold"), "fg":"#28527a"}
        entry_style = {"width":18, "font":("Segoe UI",15,"bold"), "bd":2}

        rnLbl = tk.Label(self.addFrame, text="Roll No:", **lbl_style)
        rnLbl.grid(row=0, column=0, padx=20, pady=25, sticky="e")
        self.rollNo = tk.Entry(self.addFrame, **entry_style)
        self.rollNo.grid(row=0, column=1, padx=10, pady=25)

        okBtn = tk.Button(self.addFrame,command=self.delFun, text="Enter", 
                          bg="#3a7ca5", fg="white", activebackground="#28527a", activeforeground="white",
                          font=("Segoe UI",20,"bold"), bd=0, width=20, cursor="hand2")
        okBtn.grid(row=1, column=0, padx=30, pady=25, columnspan=2)

    def delFun(self):
        rNo = int(self.rollNo.get())

        try:
            self.dbFun()
            self.cur.execute("delete from student where rollNo=%s",rNo)
            self.con.commit()
            tk.messagebox.showinfo("Success", f"Student with Roll_No.{rNo} is Removed")
            self.con.close()
            self.desAdd()

        except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")

    def clr(self, r,g,b):
        return f"#{r:02x}{g:02x}{b:02x}"

# ------------------- Login Window -------------------

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login - Student Record Management System")
        self.master.geometry("400x300")
        self.master.configure(bg="#e3eafc")

        tk.Label(master, text="Login", font=("Segoe UI", 24, "bold"), bg="#e3eafc", fg="#28527a").pack(pady=20)

        frame = tk.Frame(master, bg="#e3eafc")
        frame.pack(pady=10)

        tk.Label(frame, text="Username:", font=("Segoe UI", 14), bg="#e3eafc").grid(row=0, column=0, pady=10, sticky="e")
        self.username_entry = tk.Entry(frame, font=("Segoe UI", 14), bd=2)
        self.username_entry.grid(row=0, column=1, pady=10)

        tk.Label(frame, text="Password:", font=("Segoe UI", 14), bg="#e3eafc").grid(row=1, column=0, pady=10, sticky="e")
        self.password_entry = tk.Entry(frame, show="*", font=("Segoe UI", 14), bd=2)
        self.password_entry.grid(row=1, column=1, pady=10)

        login_btn = tk.Button(master, text="Login", font=("Segoe UI", 14, "bold"),
                              bg="#3a7ca5", fg="white", bd=0, width=15, command=self.check_login)
        login_btn.pack(pady=20)

        # Bind Enter key to login
        self.master.bind('<Return>', lambda event: self.check_login())

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Set your desired username and password here
        if username == "admin" and password == "1234":
            self.master.destroy()  # Close login window
            open_main_app()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

def open_main_app():
    root = tk.Tk()
    app = std(root)
    root.mainloop()

if __name__ == "__main__":
    login_root = tk.Tk()
    login_app = LoginWindow(login_root)
    login_root.mainloop()
