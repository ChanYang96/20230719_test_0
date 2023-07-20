import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter import ttk
from functools import partial
import admin_book_list
import login
import admin_borrow_list
import admin_user_list

def Who_login(Uname):
    messagebox.showinfo('현재세션', "현재 " + Uname + "님의 계정을 사용 중 입니다!")

def logout_page():
    messagebox.showinfo('로그아웃', "이용해 주셔서 감사합니다!")
    main.destroy()
    login.go_log_page()

def main_page(Uname, Cname):
    global main
    main = Tk()                      # root라는 창을 생성
    main.geometry("800x400")       # 창 크기설정
    main.title("도서 관리 서비스")    # 창 제목설정
    main.option_add("*Font","돋움 15 bold") # 폰트설정
    main.resizable(False, False) # 사이즈 변경 불가

    book = Button(main, text="서적 관리",  command = lambda : admin_book_list.book_list_main(Uname, Cname))
    book.place(x=50,y=100,width=200,height=200,)

    Check_out = Button(main, text="대여 목록 관리", command = lambda : admin_borrow_list.borrow_list_main(Cname))
    Check_out.place(x=300,y=100,width=200,height=200)

    user = Button(main, text="사용자 관리",  command = lambda : admin_user_list.user_list_main(Uname))
    user.place(x=550,y=100,width=200,height=200)

    logout = Button(main, text="로그아웃", command = logout_page)
    logout.place(x=10,y=10)

    logout = Button(main, text="현재세션", command = lambda :  Who_login(Uname))
    logout.place(x=125,y=10)

    main.mainloop()

