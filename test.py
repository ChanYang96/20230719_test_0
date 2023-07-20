
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter import ttk
import random

def insert_book_Button():
    sql = "INSERT INTO User_table VALUES('" + str(j_U_name.get()) + "', '" + str(j_birth.get()) + "', '" + str(j_gender.get()) + "', '" + str(j_address.get()) + "', '" + str(j_phone.get()) + "');"
    print(sql)

    random_card_number = random.randint(1000, 9999)
    sql = "INSERT INTO card_table VALUES('" + str(random_card_number) + "', '" + str(j_U_name.get()) + "', " + " DATE_FORMAT(now(), '%Y-%m-%d'), DATE_ADD(NOW(), INTERVAL 6 MONTH), 'False');"
    messagebox.showinfo('회원가입 성공', "회원가입 완료! 환영합니다 '" + str(j_U_name.get()) + "' 님! \n발급된 카드번호 : " + str(random_card_number) )
    print(sql)

global join_main, j_U_name, j_birth, j_gender, j_address, j_phone
join_main = Tk()
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

join_main.mainloop()
