# 前端包
from user_info_db import db_ops
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import tkinter as tk


# 后端包
import sys
import os  # NOQA: E402
sys.path.append(os.getcwd())  # NOQA: E402
from BACKEND import get_list  # NOQA: E402
from BACKEND import connection   # NOQA: E402
from BACKEND import credentials  # NOQA: E402

# login


class Login_Page:

    def __init__(self, window):
        self.window = window
        self.window.title('自制B2操作客户端')
        self.frame = tk.Frame(self.window)
        self.frame.grid(padx=30, pady=25)

        ttk.Label(self.frame, text='登录连接', font=('微软雅黑', 16, 'bold')).grid(
            column=1, row=0, columnspan=5, pady=5)

        ttk.Label(self.frame, text='User').grid(
            column=1, row=2, columnspan=2, pady=5)

        self.user_db = db_ops()  # 连接tinydb数据库

        # 下拉框获取用户信息
        if self.user_db.query_users():
            choices = self.user_db.query_users()
        else:
            choices = ['请添加账户信息']   # 完全没有信息时显示

        # 为了后期获取var值
        self.var_select = tk.StringVar()  # 用var_select来接收string
        user = ttk.Combobox(self.frame, values=choices,
                            textvariable=self.var_select, state='readonly')
        user.grid(column=4, row=2, columnspan=2)
        user.current(0)  # 设定下拉框的第一个为默认选项

        def callbackFunc(*args):  # 第二层func不需要self变量
            pass
            # print('选择新账户')
            # print(args[0])
            # print(self.var_select.get())

        user.bind('<<ComboboxSelected>>', callbackFunc)
        # user.bind(func=self.callbackFunc)

        ttk.Button(self.frame, text='连接', command=self.login_command).grid(
            column=3, columnspan=2, row=5, pady=10)
        ttk.Button(self.frame, text='添加用户', command=self.add_user_command).grid(
            column=5, row=5, pady=10)
        # print(y)
        # user.current(1)

        # ttk.Label(self.frame, text='Key_ID').grid(
        #     column=1, row=3, columnspan=2, pady=5)
        # self.key_id = tk.StringVar()
        # ttk.Entry(self.frame, textvariable=self.key_id).grid(
        #     column=3, row=3, columnspan=3)

        # ttk.Label(self.frame, text='App_Key').grid(
        #     column=1, row=4, columnspan=2, pady=5)
        # self.app_key = tk.StringVar()
        # ttk.Entry(self.frame, textvariable=self.app_key, show='*').grid(column=3,
        #                                                                 row=4, columnspan=3,  padx=5, pady=5)

        # print(user.current)

    def login_command(self):
        account = self.var_select.get()
        user_info = self.user_db.query_info(account)[0]
        # print(user_info)
        # 注入登录信息
        KEY_ID = user_info['key_id']
        APPLICATION_KEY = user_info['app_key']
        ENDPOINT = user_info['endpoint']
        CUSTOM_URL = user_info['custom_url']
        conn = connection.Connection(ENDPOINT, KEY_ID, APPLICATION_KEY)
        b2_client = conn.get_b2_client()
        a = get_list.list_buckets(b2_client=b2_client)
        print(a)

    def add_user_command(self):
        # print('添加ing')
        self.frame.destroy()
        Add_User_Page(self.window)

# add user


class Add_User_Page:
    def __init__(self, window):
        self.window = window
        self.window.title('自制B2操作客户端')
        self.frame = tk.Frame(self.window)
        self.frame.grid(padx=30, pady=25)
        # self.window.geometry("400x200")
        ttk.Label(self.frame, text='添加账户', font=('微软雅黑', 16, 'bold')).grid(
            column=1, row=0, columnspan=5, pady=5)

        ttk.Label(self.frame, text='Account').grid(
            column=1, row=2, columnspan=2, pady=5)
        self.username = tk.StringVar()
        ttk.Entry(self.frame, textvariable=self.username).grid(
            column=3, row=2, columnspan=3)

        ttk.Label(self.frame, text='Key_ID').grid(
            column=1, row=3, columnspan=2, pady=5)
        self.key_id = tk.StringVar()
        ttk.Entry(self.frame, textvariable=self.key_id).grid(
            column=3, row=3, columnspan=3)

        ttk.Label(self.frame, text='App_Key').grid(
            column=1, row=4, columnspan=2, pady=5)
        self.app_key = tk.StringVar()
        ttk.Entry(self.frame, textvariable=self.app_key, show='*').grid(column=3,
                                                                        row=4, columnspan=3,  padx=5, pady=5)
        ttk.Label(self.frame, text='Endpoint').grid(
            column=1, row=5, columnspan=2, pady=5)
        self.endpoint = tk.StringVar()
        ttk.Entry(self.frame, textvariable=self.endpoint).grid(
            column=3, row=5, columnspan=3)

        ttk.Label(self.frame, text='Custom Url').grid(
            column=1, row=6, columnspan=2, pady=5)
        self.custom_url = tk.StringVar()
        ttk.Entry(self.frame, textvariable=self.custom_url).grid(
            column=3, row=6, columnspan=3)

        ttk.Button(self.frame, text='添加', command=self.add_user).grid(
            column=3, columnspan=1, row=7, pady=10)
        ttk.Button(self.frame, text='返回', command=self.back_to_login).grid(
            column=5, columnspan=1, row=7, pady=10)

    def back_to_login(self):
        self.frame.destroy()
        Login_Page(self.window)

    def add_user(self):
        account = self.username.get()
        key_id = self.key_id.get()
        app_key = self.app_key.get()
        endpoint = self.endpoint.get()
        custom_url = self.custom_url.get()
        user_db = db_ops()
        user_db.add_user(account, key_id, app_key, endpoint, custom_url)
        # print(account, key_id, app_key)

        msgbox.showinfo(title='添加成功', message='已添加账户信息：%s' % account)
        self.back_to_login()

        # is_login = msgbox.askyesno('成功！', '已添加【用户】，是否直接连接数据库？')
        # # is_added =
        # if is_login:
        #     pass
        # else:
        #     pass
