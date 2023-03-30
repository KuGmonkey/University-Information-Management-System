import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *    # 图形界面库
import tkinter.messagebox as messagebox    # 弹窗

'''
db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
cursor = db.cursor()
sql="SELECT * FROM student"
cursor.execute(sql)
result=cursor.fetchall()
print(result)
'''
'''
stu_id = []
les_id = []
db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
cursor = db.cursor()  # 使用cursor()方法获取操作游标
sql1 = "SELECT stu_id FROM student"
cursor.execute(sql1)
results = cursor.fetchall()
for row in results:
    stu_id.append(row[0])
sql2 = "SELECT lesson_id FROM lesson"
cursor.execute(sql2)
results = cursor.fetchall()
for row in results:
    les_id.append(row[0])
db.close()
print(stu_id)
print(les_id)
'''


# 开始界面
class StartPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁子界面,从别处返回后销毁原界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('大学信息管理系统')
        self.window.geometry('300x470')  # 这里的乘是小x

        label = Label(self.window, text="大学信息管理系统", font=("Verdana", 20))
        label.pack(pady=100)  # pady=100 界面的长度

        Button(self.window, text="管理员登录", font=tkFont.Font(size=16), command=lambda: AdminPage(self.window), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="学生登录", font=tkFont.Font(size=16), command=lambda: StudentPage(self.window), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="教师登录", font=tkFont.Font(size=16), command=lambda: TeacherPage(self.window), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="关于", font=tkFont.Font(size=16), command=lambda: AboutPage(self.window), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text='退出系统', height=2, font=tkFont.Font(size=16), width=30, command=self.window.destroy,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()

        self.window.mainloop()  # 主消息循环


# 管理员登陆页面
class AdminPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('管理员登陆页面')
        self.window.geometry('300x450')  # 这里的乘是小x

        label = tk.Label(self.window, text='管理员登陆', bg='red', font=('Verdana', 20), width=30, height=2)
        label.pack()

        Label(self.window, text='管理员账号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_username = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_username.pack()

        Label(self.window, text='管理员密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass.pack()

        Button(self.window, text="登陆", width=8, font=tkFont.Font(size=12), command=self.login).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login(self):
        print(str(self.admin_username.get()))
        print(str(self.admin_pass.get()))
        admin_pass = None

        # 数据库操作 查询管理员表
        # 打开数据库连接 autocommit为自动连接参数
        db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM admin_login WHERE admin_id = '%s'" % (self.admin_username.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                admin_id = row[0]
                admin_pass = row[1]
                # 打印结果
                print("admin_id=%s,admin_pass=%s" % (admin_id, admin_pass))
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登陆管理员管理界面")
        print("self", self.admin_pass)
        print("local", admin_pass)

        if self.admin_pass.get() == admin_pass:
            AdminManage(self.window)  # 进入管理员操作界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


# 学生登陆页面
class StudentPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('学生登陆')
        self.window.geometry('300x450')  # 这里的乘是小x

        label = tk.Label(self.window, text='学生登陆', bg='red', font=('Verdana', 20), width=30, height=2)
        label.pack()

        Label(self.window, text='学生账号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.student_id = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.student_id.pack()

        Label(self.window, text='学生密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.student_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.student_pass.pack()

        Button(self.window, text="登陆", width=8, font=tkFont.Font(size=12), command=self.login).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login(self):
        print(str(self.student_id.get()))
        print(str(self.student_pass.get()))
        stu_pass = None

        # 数据库操作 查询管理员表
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM student_login WHERE stu_id = '%s'" % (self.student_id.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                stu_id = row[0]
                stu_pass = row[1]
                # 打印结果
                print("stu_id=%s,stu_pass=%s" % (stu_id, stu_pass))
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登陆学生信息查看界面")
        print("self", self.student_pass.get())
        print("local", stu_pass)

        if self.student_pass.get() == stu_pass:
            StudentView(self.window, self.student_id.get())  # 进入学生信息查看界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


# 教师登陆页面
class TeacherPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('教师登陆')
        self.window.geometry('300x450')  # 这里的乘是小x

        label = tk.Label(self.window, text='教师登陆', bg='red', font=('Verdana', 20), width=30, height=2)
        label.pack()

        Label(self.window, text='教师账号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.teacher_id = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.teacher_id.pack()

        Label(self.window, text='教师密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.teacher_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.teacher_pass.pack()

        Button(self.window, text="登陆", width=8, font=tkFont.Font(size=12), command=self.login).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login(self):
        print(str(self.teacher_id.get()))
        print(str(self.teacher_pass.get()))
        tea_pass = None

        # 数据库操作 查询管理员表
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM teacher_login WHERE tea_id = '%s'" % (self.teacher_id.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                tea_id = row[0]
                tea_pass = row[1]
                # 打印结果
                print("tea_id=%s,tea_pass=%s" % (tea_id, tea_pass))
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登陆教师信息查看界面")
        print("self", self.teacher_pass.get())
        print("local", tea_pass)

        if self.teacher_pass.get() == tea_pass:
            TeacherView(self.window, self.teacher_id.get())  # 进入学生信息查看界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


# 管理员操作界面
class AdminManage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁子界面,从别处返回后销毁原界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('管理员操作界面')
        self.window.geometry('300x470')  # 这里的乘是小x

        label = Label(self.window, text="请选择操作", font=("Verdana", 20))
        label.pack(pady=100)  # pady=100 界面的长度

        Button(self.window, text="学生选课信息", font=tkFont.Font(size=16), command=lambda: Student(self.window), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="教师信息", font=tkFont.Font(size=16), command=lambda: Teacher(self.window), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="课程信息", font=tkFont.Font(size=16), command=lambda: Lesson(self.window), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="选课信息", font=tkFont.Font(size=16), command=lambda: Learn(self.window), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="授课信息", font=tkFont.Font(size=16), command=lambda: Teach(self.window), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text='退出系统', height=2, font=tkFont.Font(size=16), width=30, command=self.window.destroy,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 主消息循环

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

# 学生信息界面
class Student:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('学生信息')

        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("学号", "姓名", "课程代码", "得分")# 后两个改为性别、学院
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("学号", width=150, anchor='center')  # 表示列,不显示
        self.tree.column("姓名", width=150, anchor='center')
        self.tree.column("课程代码", width=100, anchor='center') # 性别
        self.tree.column("得分", width=100, anchor='center') # 学院

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = []
        self.name = []
        self.gender = []
        self.college = []
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM stu_les"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.college.append(row[3])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        # 写入数据
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.college))):
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.college[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        # 学生信息不展示入学年份
        self.top_title = Label(self.frame_left_top, text="学生信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明学号
        self.var_name = StringVar()  # 声明姓名
        self.var_gender = StringVar()  # 声明性别
        self.var_college = StringVar()  # 声明学院
        # 学号
        self.right_top_id_label = Label(self.frame_left_top, text="学号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 姓名
        self.right_top_name_label = Label(self.frame_left_top, text="姓名：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 性别
        self.right_top_gender_label = Label(self.frame_left_top, text="性别：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_gender,font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 学院
        self.right_top_gender_label = Label(self.frame_left_top, text="年龄：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_college,font=('Verdana', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建学生信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中学生信息', width=20,command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中学生信息', width=20,command=self.del_row)
        # self.right_top_button4 = ttk.Button(self.frame_right_top, text='返回首页', width=20, command=self.back())

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
        # self.right_top_button4.grid(row=5, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(bool(0))
        self.frame_right_top.grid_propagate(bool(0))
        self.frame_center.grid_propagate(bool(0))
        self.frame_bottom.grid_propagate(bool(0))

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        AdminManage(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_name.set(self.row_info[1])
        self.var_gender.set(self.row_info[2])
        self.var_college.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,font=('Verdana', 15))
        print('')

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new_row(self):
        print('123')
        print(self.var_id.get())
        print(self.id)
        if str(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '该学号已被占用！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_gender.get() != '':
                # 打开数据库连接
                db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                if(self.var_college!=''):
                    # SQL 插入语句
                    sql = "INSERT INTO student(stu_id, stu_name, stu_gender, stu_adm_time, stu_college) \
                           VALUES ('%s', '%s', '%s', '2022-05-25', '%s')" % \
                          (self.var_id.get(), self.var_name.get(), self.var_gender.get(), self.var_college.get())
                else:
                    sql = "INSERT INTO student(stu_id, stu_name, stu_gender, stu_adm_time, stu_college) \
                           VALUES ('%s', '%s', '%s', '2022-05-25', '未划分学院')" % \
                          (self.var_id.get(), self.var_name.get(), self.var_gender.get())

                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '插入成功！')
                    self.id.append(self.var_id.get())
                    self.name.append(self.var_name.get())
                    self.gender.append(self.var_gender.get())
                    self.college.append(self.var_college.get())
                    self.tree.insert('', len(self.id) - 1, values=(
                        self.id[len(self.id) - 1], self.name[len(self.id) - 1], self.gender[len(self.id) - 1],
                        self.college[len(self.id) - 1]))
                    self.tree.update()
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接

            else:
                messagebox.showinfo('警告！', '请填写必要学生数据')

    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row_info[0]:  # 如果所填学号与所选学号一致
                # 打开数据库连接
                db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                # SQL 插入语句
                sql = "UPDATE student SET stu_name = '%s', stu_gender = '%s', stu_college = '%s' \
                WHERE stu_id = '%s'" % \
                      (self.var_name.get(), self.var_gender.get(), self.var_college.get(), self.var_id.get())
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                    id_index = self.id.index(self.row_info[0])
                    self.name[id_index] = self.var_name.get()
                    self.gender[id_index] = self.var_gender.get()
                    self.college[id_index] = self.var_college.get()

                    self.tree.item(self.tree.selection()[0], values=(
                        self.var_id.get(), self.var_name.get(), self.var_gender.get(),
                        self.var_college.get()))  # 修改对于行信息
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                db.close()  # 关闭数据库连接

            else:
                messagebox.showinfo('警告！', '不能修改学生学号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
            # 打开数据库连接
            db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM student WHERE stu_id = '%s'" % (self.row_info[0])  # SQL 删除语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
                id_index = self.id.index(self.row_info[0])
                print(id_index)
                del self.id[id_index]
                del self.name[id_index]
                del self.gender[id_index]
                del self.college[id_index]
                print(self.id)
                self.tree.delete(self.tree.selection()[0])  # 删除所选行
                print(self.tree.get_children())
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接


# 教师信息界面
class Teacher:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('教师信息')

        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("职工号", "姓名", "职称", "薪水")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("职工号", width=150, anchor='center')  # 表示列,不显示
        self.tree.column("姓名", width=150, anchor='center')
        self.tree.column("职称", width=100, anchor='center')
        self.tree.column("薪水", width=100, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = []
        self.name = []
        self.title = []
        self.salary = []
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM teacher"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.title.append(row[2])
                self.salary.append(row[3])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        #print("test***********************")
        # 写入数据
        for i in range(min(len(self.id), len(self.name), len(self.title), len(self.salary))):
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.title[i], self.salary[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="教师信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明职工号
        self.var_name = StringVar()  # 声明姓名
        self.var_title = StringVar()  # 声明职称
        self.var_salary = StringVar()  # 声明薪水
        # 职工号
        self.right_top_id_label = Label(self.frame_left_top, text="职工号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 姓名
        self.right_top_name_label = Label(self.frame_left_top, text="姓名：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 职称
        self.right_top_title_label = Label(self.frame_left_top, text="职称：", font=('Verdana', 15))
        self.right_top_title_entry = Entry(self.frame_left_top, textvariable=self.var_title,font=('Verdana', 15))
        self.right_top_title_label.grid(row=3, column=0)  # 位置设置
        self.right_top_title_entry.grid(row=3, column=1)
        # 薪水
        self.right_top_salary_label = Label(self.frame_left_top, text="薪水：", font=('Verdana', 15))
        self.right_top_salary_entry = Entry(self.frame_left_top, textvariable=self.var_salary,font=('Verdana', 15))
        self.right_top_salary_label.grid(row=4, column=0)  # 位置设置
        self.right_top_salary_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建教师信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中教师信息', width=20,command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中教师信息', width=20,command=self.del_row)
        # self.right_top_button4 = ttk.Button(self.frame_right_top, text='返回首页', width=20, command=self.back())

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
        # self.right_top_button4.grid(row=5, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(bool(0))
        self.frame_right_top.grid_propagate(bool(0))
        self.frame_center.grid_propagate(bool(0))
        self.frame_bottom.grid_propagate(bool(0))

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        AdminManage(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_name.set(self.row_info[1])
        self.var_title.set(self.row_info[2])
        self.var_salary.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,font=('Verdana', 15))
        print('')

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new_row(self):
        print('123')
        print(self.var_id.get())
        print(self.id)
        if str(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '该职工号已被占用！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_salary.get() != '':
                # 打开数据库连接
                db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                if(self.var_title!=''):
                    # SQL 插入语句
                    sql = "INSERT INTO teacher(tea_id, tea_name, tea_title, tea_salary) \
                           VALUES ('%s', '%s', '%s', %d)" % \
                          (self.var_id.get(), self.var_name.get(), self.var_title.get(), int(self.var_salary.get()))
                else:
                    sql = "INSERT INTO teacher(tea_id, tea_name, tea_title, tea_salary) \
                           VALUES ('%s', '%s', '尚未分配职称', %d)" % \
                          (self.var_id.get(), self.var_name.get(), int(self.var_salary.get()))

                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    self.id.append(self.var_id.get())
                    self.name.append(self.var_name.get())
                    self.title.append(self.var_title.get())
                    self.salary.append(int(self.var_salary.get()))
                    self.tree.insert('', len(self.id) - 1, values=(
                        self.id[len(self.id) - 1], self.name[len(self.id) - 1], self.title[len(self.id) - 1],
                        self.salary[len(self.id) - 1]))
                    self.tree.update()
                    messagebox.showinfo('提示！', '插入成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接

            else:
                messagebox.showinfo('警告！', '请填写必要教师数据')

    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row_info[0]:  # 如果所填学号与所选学号一致
                # 打开数据库连接
                db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                # SQL 插入语句
                sql = "call updata_tea1('%s', '%s', %d, '%s')" % \
                      (self.var_name.get(), self.var_title.get(), int(self.var_salary.get()), self.var_id.get())
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')

                    id_index = self.id.index(self.row_info[0])
                    self.name[id_index] = self.var_name.get()
                    self.title[id_index] = self.var_title.get()
                    self.salary[id_index] = int(self.var_salary.get())

                    self.tree.item(self.tree.selection()[0], values=(
                        self.var_id.get(), self.var_name.get(), self.var_title.get(),
                        self.var_salary.get()))  # 修改对于行信息
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '教师工资太低了！')
                db.close()  # 关闭数据库连接
            else:
                messagebox.showinfo('警告！', '不能修改教师职工号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
            # 打开数据库连接admin

            db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql1 = "BEGIN"
            sql2 = "DELETE FROM lesson WHERE lesson_id in (SELECT lesson_id FROM teach WHERE tea_id = '%s')" % (self.row_info[0])
            sql3 = "DELETE FROM teacher WHERE tea_id = '%s'" % (self.row_info[0])
            sql4 = "COMMIT"   # SQL 删除语句
            try:
                cursor.execute(sql1)  # 执行sql语句
                cursor.execute(sql2)
                cursor.execute(sql3)
                cursor.execute(sql4)
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')

                id_index = self.id.index(self.row_info[0])
                print(id_index)
                del self.id[id_index]
                del self.name[id_index]
                del self.title[id_index]
                del self.salary[id_index]
                print(self.id)
                self.tree.delete(self.tree.selection()[0])  # 删除所选行
                print(self.tree.get_children())
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

class Lesson:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('课程信息')

        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("课程代码", "课程名称", "学分", "课时")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("课程代码", width=150, anchor='center')  # 表示列,不显示
        self.tree.column("课程名称", width=150, anchor='center')
        self.tree.column("学分", width=100, anchor='center')
        self.tree.column("课时", width=100, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = []
        self.name = []
        self.cre = []
        self.hour = []
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM lesson"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.cre.append(row[2])
                self.hour.append(row[3])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        # 写入数据
        for i in range(min(len(self.id), len(self.name), len(self.cre), len(self.hour))):
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.cre[i], self.hour[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        # 学生信息不展示入学年份
        self.top_title = Label(self.frame_left_top, text="课程信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明课号
        self.var_name = StringVar()  # 声明姓名
        self.var_cre = StringVar()  # 声明学分
        self.var_hour = StringVar()  # 声明课时
        # 学号
        self.right_top_id_label = Label(self.frame_left_top, text="课程代码：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 姓名
        self.right_top_name_label = Label(self.frame_left_top, text="课程名称：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 性别
        self.right_top_gender_label = Label(self.frame_left_top, text="学分：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_cre,font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 学院
        self.right_top_gender_label = Label(self.frame_left_top, text="课时：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_hour,font=('Verdana', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建课程信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中课程信息', width=20,command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中课程信息', width=20,command=self.del_row)
        # self.right_top_button4 = ttk.Button(self.frame_right_top, text='返回首页', width=20, command=self.back())

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
        # self.right_top_button4.grid(row=5, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(bool(0))
        self.frame_right_top.grid_propagate(bool(0))
        self.frame_center.grid_propagate(bool(0))
        self.frame_bottom.grid_propagate(bool(0))

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        AdminManage(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_name.set(self.row_info[1])
        self.var_cre.set(self.row_info[2])
        self.var_hour.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,font=('Verdana', 15))
        print('')

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new_row(self):
        print('123')
        print(self.var_id.get())
        print(self.id)
        if str(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '该课号已被占用！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_cre.get() != '':
                # 打开数据库连接
                db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                if(self.var_hour!=''):
                    # SQL 插入语句
                    sql = "INSERT INTO lesson(lesson_id, lesson_name, credit, class_hour) \
                           VALUES ('%s', '%s', '%s', '%s')" % \
                          (self.var_id.get(), self.var_name.get(), self.var_cre.get(), self.var_hour.get())
                else:
                    sql = "INSERT INTO lesson(lesson_id, lesson_name, credit, class_hour) \
                           VALUES ('%s', '%s', '%s', '尚未设置学时')" % \
                          (self.var_id.get(), self.var_name.get(), self.var_cre.get())

                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '插入成功！')
                    self.id.append(self.var_id.get())
                    self.name.append(self.var_name.get())
                    self.cre.append(self.var_cre.get())
                    self.hour.append(self.var_hour.get())
                    self.tree.insert('', len(self.id) - 1, values=(
                        self.id[len(self.id) - 1], self.name[len(self.id) - 1], self.cre[len(self.id) - 1],
                        self.hour[len(self.id) - 1]))
                    self.tree.update()
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '课时太多了！学不完！')
                db.close()  # 关闭数据库连接

            else:
                messagebox.showinfo('警告！', '请填写必要课程信息')

    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row_info[0]:  # 如果所填学号与所选学号一致
                # 打开数据库连接
                db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                # SQL 插入语句
                sql = "UPDATE lesson SET lesson_name = '%s', credit = '%s', class_hour = '%s' \
                WHERE lesson_id = '%s'" % \
                      (self.var_name.get(), self.var_cre.get(), self.var_hour.get(), self.var_id.get())
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                    id_index = self.id.index(self.row_info[0])
                    self.name[id_index] = self.var_name.get()
                    self.cre[id_index] = self.var_cre.get()
                    self.hour[id_index] = self.var_hour.get()

                    self.tree.item(self.tree.selection()[0], values=(
                        self.var_id.get(), self.var_name.get(), self.var_cre.get(),
                        self.var_hour.get()))  # 修改对于行信息
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                db.close()  # 关闭数据库连接

            else:
                messagebox.showinfo('警告！', '不能修改课程代码！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
            # 打开数据库连接
            db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM lesson WHERE lesson_id = '%s'" % (self.row_info[0])  # SQL 删除语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
                id_index = self.id.index(self.row_info[0])
                print(id_index)
                del self.id[id_index]
                del self.name[id_index]
                del self.cre[id_index]
                del self.hour[id_index]
                print(self.id)
                self.tree.delete(self.tree.selection()[0])  # 删除所选行
                print(self.tree.get_children())
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接


# 选课信息界面
class Learn:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('选课信息')

        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("学生学号", "课程代码", "教室", "成绩")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("学生学号", width=150, anchor='center')  # 表示列,不显示
        self.tree.column("课程代码", width=150, anchor='center')
        self.tree.column("教室", width=100, anchor='center')
        self.tree.column("成绩", width=100, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = [] # 学生学号
        self.les = [] # 课程代码
        self.cla = [] # 教室
        self.scr = [] # 成绩
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM learn"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.les.append(row[1])
                self.cla.append(row[3])
                self.scr.append(row[2])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        # 写入数据
        for i in range(min(len(self.id), len(self.les), len(self.cla), len(self.scr))):
            self.tree.insert('', i, values=(self.id[i], self.les[i], self.cla[i], self.scr[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="选课信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明学号
        self.var_les = StringVar()  # 声明课程代码
        self.var_cla = StringVar()  # 声明教室
        self.var_scr = StringVar()  # 声明成绩
        # 学号
        self.right_top_id_label = Label(self.frame_left_top, text="学生学号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 课程代码
        self.right_top_name_label = Label(self.frame_left_top, text="课程代码：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_les, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 教室
        self.right_top_gender_label = Label(self.frame_left_top, text="教室：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_cla,font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 成绩
        self.right_top_gender_label = Label(self.frame_left_top, text="成绩：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_scr,font=('Verdana', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建选课信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中选课信息', width=20,command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中选课信息', width=20,command=self.del_row)
        # self.right_top_button4 = ttk.Button(self.frame_right_top, text='返回首页', width=20, command=self.back())

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
        # self.right_top_button4.grid(row=5, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(bool(0))
        self.frame_right_top.grid_propagate(bool(0))
        self.frame_center.grid_propagate(bool(0))
        self.frame_bottom.grid_propagate(bool(0))

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        AdminManage(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_les.set(self.row_info[1])
        self.var_cla.set(self.row_info[2])
        self.var_scr.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,font=('Verdana', 15))
        print('')

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new_row(self):
        print('123')
        print(self.var_id.get())
        print(self.id)
        #if str(self.var_id.get()) in self.id and str(self.var_les.get()) == self.les[self.id.index(self.var_id.get())]:
            #messagebox.showinfo('警告！', '该学生已选过此课程！')
        #else:
        stu_id = [] # 所有学生
        les_id = [] # 开设的所有课程
        lesed_id = [] # 有人教的课
        db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标

        sql1 = "SELECT stu_id FROM student"
        cursor.execute(sql1)
        results = cursor.fetchall()
        for row in results:
            stu_id.append(row[0])

        sql2 = "SELECT lesson_id FROM lesson"
        cursor.execute(sql2)
        results = cursor.fetchall()
        for row in results:
            les_id.append(row[0])

        sql3 = "SELECT lesson_id FROM teach"
        cursor.execute(sql3)
        results = cursor.fetchall()
        for row in results:
            lesed_id.append(row[0])
        db.close()

        if self.var_id.get() == '' or self.var_les.get() == '':
            messagebox.showinfo('警告！', '请输入必要的选课信息')
        else:
            if self.var_id.get() not in stu_id or self.var_les.get() not in les_id:
                messagebox.showinfo('警告！', '该学生或该课程不存在！')
            elif self.var_les.get() not in lesed_id:
                messagebox.showinfo('警告！', '尚无人开此课程！')
            else:
                # 打开数据库连接
                db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标

                # SQL 插入语句
                sql = "INSERT INTO learn(stu_id, lesson_id, score, class_number) \
                       VALUES ('%s', '%s', '%s', '%s')" % \
                      (self.var_id.get(), self.var_les.get(), self.var_scr.get(), self.var_cla.get())

                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    self.id.append(self.var_id.get())
                    self.les.append(self.var_les.get())
                    self.cla.append(self.var_cla.get())
                    self.scr.append(self.var_scr.get())
                    self.tree.insert('', len(self.id) - 1, values=(
                        self.id[len(self.id) - 1], self.les[len(self.id) - 1], self.cla[len(self.id) - 1],
                        self.scr[len(self.id) - 1]))
                    self.tree.update()
                    messagebox.showinfo('提示！', '插入成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '该学生已经选过此课程！')
                db.close()  # 关闭数据库连接


    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row_info[0]:  # 如果所填学号与所选学号一致
                # 打开数据库连接
                db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                # SQL 插入语句
                sql = "UPDATE learn SET lesson_id = '%s', score = '%s', class_number = '%s' \
                WHERE stu_id = '%s' and lesson_id = '%s'" % \
                      (self.var_les.get(), self.var_scr.get(), self.var_cla.get(), self.row_info[0], self.row_info[1])
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                    id_index = self.id.index(self.row_info[0])
                    self.les[id_index] = self.var_les.get()
                    self.cla[id_index] = self.var_cla.get()
                    self.scr[id_index] = self.var_scr.get()

                    self.tree.item(self.tree.selection()[0], values=(
                        self.var_id.get(), self.var_les.get(), self.var_cla.get(),
                        self.var_scr.get()))  # 修改对于行信息
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '该学生已经选过此课程！')
                db.close()  # 关闭数据库连接

            else:
                messagebox.showinfo('警告！', '不能修改学生学号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
            # 打开数据库连接
            db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM learn WHERE stu_id = '%s' and lesson_id = '%s'" % (self.row_info[0],self.row_info[1])  # SQL 删除语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            print(id_index)
            del self.id[id_index]
            del self.les[id_index]
            del self.cla[id_index]
            del self.scr[id_index]
            print(self.id)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())


# 授课信息界面
class Teach:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('授课信息')

        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("教师职工号", "课程代码", "教室", "结课方式")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("教师职工号", width=150, anchor='center')  # 表示列,不显示
        self.tree.column("课程代码", width=150, anchor='center')
        self.tree.column("教室", width=100, anchor='center')
        self.tree.column("结课方式", width=100, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = [] # 教师职工号
        self.les = [] # 课程代码
        self.cla = [] # 教室
        self.scr = [] # 结课方式
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM teach"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.les.append(row[1])
                self.cla.append(row[3])
                self.scr.append(row[2])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        # 写入数据
        for i in range(min(len(self.id), len(self.les), len(self.cla), len(self.scr))):
            self.tree.insert('', i, values=(self.id[i], self.les[i], self.cla[i], self.scr[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="授课信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明职工号
        self.var_les = StringVar()  # 声明课程代码
        self.var_cla = StringVar()  # 声明教室
        self.var_scr = StringVar()  # 声明结课方式
        # 学号
        self.right_top_id_label = Label(self.frame_left_top, text="教师职工号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 课程代码
        self.right_top_name_label = Label(self.frame_left_top, text="课程代码：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_les, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 教室
        self.right_top_gender_label = Label(self.frame_left_top, text="教室：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_cla,font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 成绩
        self.right_top_gender_label = Label(self.frame_left_top, text="结课方式：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_scr,font=('Verdana', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建授课信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中授课信息', width=20,command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中授课信息', width=20,command=self.del_row)
        # self.right_top_button4 = ttk.Button(self.frame_right_top, text='返回首页', width=20, command=self.back())

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
        # self.right_top_button4.grid(row=5, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(bool(0))
        self.frame_right_top.grid_propagate(bool(0))
        self.frame_center.grid_propagate(bool(0))
        self.frame_bottom.grid_propagate(bool(0))

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        AdminManage(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_les.set(self.row_info[1])
        self.var_cla.set(self.row_info[2])
        self.var_scr.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,font=('Verdana', 15))
        print('')

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new_row(self):
        print('123')
        print(self.var_id.get())
        print(self.id)
        #if str(self.var_id.get()) in self.id and str(self.var_les.get()) == self.les[self.id.index(self.var_id.get())]:
            #messagebox.showinfo('警告！', '该学生已选过此课程！')
        #else:
        tea_id = []
        les_id = []
        db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql1 = "SELECT tea_id FROM teacher"
        cursor.execute(sql1)
        results = cursor.fetchall()
        for row in results:
            tea_id.append(row[0])
        sql2 = "SELECT lesson_id FROM lesson"
        cursor.execute(sql2)
        results = cursor.fetchall()
        for row in results:
            les_id.append(row[0])
        db.close()

        if self.var_id.get() == '' or self.var_les.get() == '':
            messagebox.showinfo('警告！', '请输入必要的授课信息')
        else:
            if self.var_id.get() not in tea_id or self.var_les.get() not in les_id:
                messagebox.showinfo('警告！', '该教师或该课程不存在！')
            else:
                # 打开数据库连接
                db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标

                # SQL 插入语句
                sql = "INSERT INTO teach(tea_id, lesson_id, class, end_way) \
                       VALUES ('%s', '%s', '%s', '%s')" % \
                      (self.var_id.get(), self.var_les.get(), self.var_cla.get(), self.var_scr.get())

                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    self.id.append(self.var_id.get())
                    self.les.append(self.var_les.get())
                    self.cla.append(self.var_cla.get())
                    self.scr.append(self.var_scr.get())
                    self.tree.insert('', len(self.id) - 1, values=(
                        self.id[len(self.id) - 1], self.les[len(self.id) - 1], self.cla[len(self.id) - 1],
                        self.scr[len(self.id) - 1]))
                    self.tree.update()
                    messagebox.showinfo('提示！', '插入成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '该授课信息已存在！')
                db.close()  # 关闭数据库连接


    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row_info[0]:  # 如果所填学号与所选学号一致
                # 打开数据库连接
                db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                # SQL 插入语句
                sql = "call updata_teach('%s', '%s', '%s', '%s', '%s')" % \
                      (self.var_les.get(), self.var_scr.get(), self.var_cla.get(), self.row_info[0], self.row_info[1])
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                    id_index = self.id.index(self.row_info[0])
                    self.les[id_index] = self.var_les.get()
                    self.cla[id_index] = self.var_cla.get()
                    self.scr[id_index] = self.var_scr.get()

                    self.tree.item(self.tree.selection()[0], values=(
                        self.var_id.get(), self.var_les.get(), self.var_cla.get(),
                        self.var_scr.get()))  # 修改对于行信息
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '该授课信息已存在！')
                db.close()  # 关闭数据库连接

            else:
                messagebox.showinfo('警告！', '不能修改教师职工号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
            # 打开数据库连接
            db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM teach WHERE tea_id = '%s' and lesson_id = '%s'" % (self.row_info[0],self.row_info[1])  # SQL 删除语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
                id_index = self.id.index(self.row_info[0])
                print(id_index)
                del self.id[id_index]
                del self.les[id_index]
                del self.cla[id_index]
                del self.scr[id_index]
                print(self.id)
                self.tree.delete(self.tree.selection()[0])  # 删除所选行
                print(self.tree.get_children())
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接


# 学生查看信息界面
class StudentView:
    def __init__(self, parent_window, student_id):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('学生信息查看')
        self.window.geometry('300x450')  # 这里的乘是小x

        label = tk.Label(self.window, text='学生信息查看', bg='green', font=('Verdana', 20), width=30, height=2)
        label.pack(pady=20)

        self.id = '学号:' + ''
        self.name = '姓名:' + ''
        self.gender = '性别:' + ''
        self.adm_time = '入学时间' + ''
        self.college = '学院:' + ''
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM student WHERE stu_id = '%s'" % (student_id)  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id = '学号:' + row[0]
                self.name = '姓名:' + row[1]
                self.gender = '性别:' + row[2]
                self.adm_time = '入学时间:' + str(row[3])
                self.college = '学院:' + row[4]
        except:
            print("Error: unable to fetch data")
        db.close()  # 关闭数据库连接

        Label(self.window, text=self.id, font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=self.name, font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=self.gender, font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=str(self.adm_time), font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=self.college, font=('Verdana', 18)).pack(pady=5)

        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=16), command=self.back).pack(pady=25)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


# 教师查看信息界面
class TeacherView:
    def __init__(self, parent_window, teacher_id):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('教师信息查看')
        self.window.geometry('300x450')  # 这里的乘是小x

        label = tk.Label(self.window, text='教师信息查看', bg='green', font=('Verdana', 20), width=30, height=2)
        label.pack(pady=20)

        self.id = '职工号:' + ''
        self.name = '姓名:' + ''
        self.title = '职称:' + ''
        self.salary = '薪水' + ''
        self.college = '学院:' + ''
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM teacher WHERE tea_id = '%s'" % (teacher_id)  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id = '职工号:' + row[0]
                self.name = '姓名:' + row[1]
                self.title = '职称:' + row[2]
                self.salary = '薪水:' + str(row[3])
                self.college = '学院:' + row[4]
        except:
            print("Error: unable to fetch data")
        db.close()  # 关闭数据库连接

        Label(self.window, text=self.id, font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=self.name, font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=self.title, font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=str(self.salary), font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=self.college, font=('Verdana', 18)).pack(pady=5)

        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=16), command=self.back).pack(pady=25)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


# About页面
class AboutPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('关于')
        self.window.geometry('300x450')  # 这里的乘是小x

        label = tk.Label(self.window, text='大学信息管理系统', bg='red', font=('Verdana', 20), width=30, height=2)
        label.pack()

        Label(self.window, text='姓名：姜志凯', font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text='学号：2011937', font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text='专业：信息安全', font=('Verdana', 18)).pack(pady=5)

        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack(pady=100)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


if __name__ == '__main__':
    try:
        '''
        # 打开数据库连接 连接测试
        db = pymysql.connect(host="localhost", user="root", password="jzk1314.", database="school", port=3306)
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # 如果数据表不存在则创建表 若存在则跳过
        # 设置主键唯一
        sql = """CREATE TABLE IF NOT EXISTS student(
				stu_id varchar(20) NOT NULL,
				stu_name varchar(255) default NULL,
				stu_gender varchar(20) default NULL,  
				stu_adm_time date(20) default NULL,
				stu_college varchar(255),
				PRIMARY KEY (stu_id)
				) 
				"""
        cursor.execute(sql)
        # 如果数据表不存在则创建表 若存在则跳过
        sql = """CREATE TABLE IF NOT EXISTS teacher(
        				tea_id varchar(20) NOT NULL,
        				tea_name varchar(255) default NULL,
        				tea_title varchar(255) default NULL,  
        				tea_salary decimal(10) default NULL,
        				tea_college varchar(255),
        				PRIMARY KEY (tea_id)
        				) 
        				"""
        cursor.execute(sql)
        # 如果数据表不存在则创建表 若存在则跳过
        sql = """CREATE TABLE IF NOT EXISTS admin_login(
						admin_id varchar(255) NOT NULL,
						admin_pwd varchar(255) default NULL,
						PRIMARY KEY (admin_id)
						) 
						"""
        cursor.execute(sql)
        # 如果数据表不存在则创建表 若存在则跳过
        sql = """CREATE TABLE IF NOT EXISTS student_login(
						stu_id varchar(255) NOT NULL,
						stu_pwd varchar(255) default NULL,
						PRIMARY KEY (stu_id)
						) 
						"""
        cursor.execute(sql)
        # 如果数据表不存在则创建表 若存在则跳过
        sql = """CREATE TABLE IF NOT EXISTS teacher_login(
        						tea_id varchar(255) NOT NULL,
        						tea_pwd varchar(255) default NULL,
        						PRIMARY KEY (tea_id)
        						) 
        						"""
        cursor.execute(sql)
        
        # 关闭数据库连接
        db.close()
        '''

        # 实例化Application
        window = tk.Tk()
        StartPage(window)
    except:
        messagebox.showinfo('错误！', '连接数据库失败！')

