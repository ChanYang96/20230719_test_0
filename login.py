import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter import ttk
import main_interface
import admin_main_interface
import random

def join_page():
    global join_main, j_U_name, j_birth, j_gender, j_address, j_phone
    join_main = Toplevel()
    join_main.title("회원가입 서비스")

    j_U_name, j_birth, j_gender, j_address, j_phone = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
    ttk.Label(join_main, text = "사용자 이름 : ").grid(row = 0, column = 0, padx = 5, pady = 10)
    ttk.Entry(join_main, textvariable = j_U_name).grid(row = 0, column = 1, padx = 5, pady = 10)

    ttk.Label(join_main, text = "사용자 생년월일 : ").grid(row = 1, column = 0, padx = 5, pady = 10)
    ttk.Entry(join_main, textvariable = j_birth).grid(row = 1, column = 1, padx = 5, pady = 10)

    ttk.Label(join_main, text = "사용자 성별 : ").grid(row = 2, column = 0, padx = 5, pady = 10)
    ttk.Entry(join_main, textvariable = j_gender).grid(row = 2, column = 1, padx = 5, pady = 10)

    ttk.Label(join_main, text = "사용자 주소 : ").grid(row = 3, column = 0, padx = 5, pady = 10)
    ttk.Entry(join_main, textvariable = j_address).grid(row = 3, column = 1, padx = 5, pady = 10)

    ttk.Label(join_main, text = "사용자 전화번호 : ").grid(row = 4, column = 0, padx = 5, pady = 10)
    ttk.Entry(join_main, textvariable = j_phone).grid(row = 4, column = 1, padx = 5, pady = 10)

    ttk.Button(join_main, text = "회원가입", command = insert_book_Button).grid(row = 5, column = 1, padx = 5, pady = 10)

def insert_book_Button():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='anyangu_db', charset='utf8')
    cur = conn.cursor()
    sql = "INSERT INTO User_table VALUES('" + str(j_U_name.get()) + "', '" + str(j_birth.get()) + "', '" + str(j_gender.get()) + "', '" + str(j_address.get()) + "', '" + str(j_phone.get()) + "');"
    cur.execute(sql)
    conn.commit()

    random_card_number = random.randint(1000, 9999)
    sql = "INSERT INTO card_table VALUES('" + str(random_card_number) + "', '" + str(j_U_name.get()) + "', " + " DATE_FORMAT(now(), '%Y-%m-%d'), DATE_ADD(NOW(), INTERVAL 6 MONTH), 'False');"
    cur.execute(sql)
    conn.commit()
    conn.close()
    messagebox.showinfo('회원가입 성공', "회원가입 완료! 환영합니다 '" + str(j_U_name.get()) + "' 님! \n발급된 카드번호 : " + str(random_card_number) )
    join_main.destroy()

def check_data():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='anyangu_db', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT C_name, admin_check FROM card_table WHERE U_name = " + "'" + str(U_name.get()) + "'" + " AND C_name = " + "'" + str(C_name.get()) + "';"
    Cname = str(C_name.get())
    Uname = str(U_name.get())
    cur.execute(sql)
    row = cur.fetchone()
    if row is None:
        messagebox.showinfo('인증실패', "다시 입력 하세요")
    elif row[0] != None and row[1] == 'True':
       messagebox.showinfo('인증성공', "환영합니다. 관리자 " + str(U_name.get()) + "님!")
       Login_page.destroy()
       admin_main_interface.main_page(Uname, Cname)

    elif row[0] != None and row[1] == 'False':
        messagebox.showinfo('인증성공', "환영합니다 " + str(U_name.get()) + "님!")
        Login_page.destroy()
        main_interface.main_page(Uname, Cname)

    conn.close()

def go_log_page():
    global Login_page, U_name, C_name
    Login_page = Tk()
    Login_page.geometry("300x150+800+350")       # 창 크기설정
    Login_page.title("도서관 인증 페이지")
        
    U_name, C_name = StringVar(), StringVar()
    # id와 password, 그리고 확인 버튼의 UI를 만드는 부분
    ttk.Label(Login_page, text = "이름 : ").grid(row = 0, column = 0, padx = 10, pady = 10)
    ttk.Label(Login_page, text = "카드 번호 : ").grid(row = 1, column = 0, padx = 10, pady = 10)
    ttk.Entry(Login_page, textvariable = U_name).grid(row = 0, column = 1, padx = 10, pady = 10)
    ttk.Entry(Login_page, textvariable = C_name).grid(row = 1, column = 1, padx = 10, pady = 10)
    ttk.Button(Login_page, text = "로그인", command = check_data).grid(row = 2, column = 0, padx = 10, pady = 10)
    ttk.Button(Login_page, text = "회원가입", command = join_page).grid(row = 2, column = 1, padx = 10, pady = 10)

    Login_page.mainloop()

def main():
    go_log_page()

if __name__ == "__main__":
    main()