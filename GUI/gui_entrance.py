import tkinter as tk
import login_add_user as la
import upload_file as up
import download_file as dof
import create_bucket as cb
import tkinter.messagebox as msgbox

from user_info_db import db_ops


if __name__ == '__main__':
    root = tk.Tk()
    user_db = db_ops()
    if user_db.query_users():
        index = la.Login_Page(root)
    else:
        # msgbox.showerror(title='无账户', message='请添加账户')
        index = la.Add_User_Page(root)
    # p2 = Page_2(root)
    root.mainloop()
