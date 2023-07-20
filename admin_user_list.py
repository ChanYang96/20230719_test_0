import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter import ttk

def user_list_main(Uname):
    book_list = Tk()  
    book_list.geometry("1100x220")
    book_list.title("사용자 정보")

    global frame1, frame2, frame3, frame4, frame5
    listFrame = Frame(book_list)
    listFrame.pack(side = BOTTOM,fill=BOTH, expand=1)
            
    frame1 = Listbox(book_list, relief='ridge', bd=1);
    frame1.pack(side='left', fill='both', expand=True);
    frame2 = Listbox(book_list, relief='ridge', bd=1);
    frame2.pack(side='left', fill='both', expand=True);
    frame3 = Listbox(book_list, relief='ridge', bd=1);
    frame3.pack(side='left', fill='both', expand=True);
    frame4 = Listbox(book_list, relief='ridge', bd=1);
    frame4.pack(side='left', fill='both', expand=True);
    frame5 = Listbox(book_list, relief='ridge', bd=1);
    frame5.pack(side='left', fill='both', expand=True);

    Button1 = Button(book_list, text="조회", command = select)
    Button1.place(x=15,y=175)
    Button2 = Button(book_list, text="사용자 정보 수정", command = update_user)
    Button2.place(x=65,y=175)
    Button3 = Button(book_list, text="사용자 정보 삭제", command = delete_user)
    Button3.place(x=180,y=175)

def delete_user():
    global d_U_name, delete_user_button_page
    delete_user_button_page = Toplevel()
    delete_user_button_page.geometry("500x100+800+350")
    delete_user_button_page.title("사용자 정보 삭제")
    d_U_name = StringVar()
    ttk.Label(delete_user_button_page, text = "삭제할 사용자 이름 : ").grid(row = 0, column = 0, padx = 5, pady = 10)
    ttk.Entry(delete_user_button_page, textvariable = d_U_name).grid(row = 0, column = 1, padx = 5, pady = 10)
    ttk.Button(delete_user_button_page, text = "삭제", command = delete_user_Button).grid(row = 1, column = 1, padx = 5, pady = 10)

def delete_user_Button():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='anyangu_db', charset='utf8')
    cur = conn.cursor()
    sql = "DELETE FROM User_table WHERE U_name = '" +  str(d_U_name.get()) + "';"
    cur.execute(sql)
    conn.commit()
    conn.close()
    messagebox.showinfo('삭제 완료', "사용자 '" + str(d_U_name.get()) + "' 가 제거 되었습니다!")
    select()
    delete_user_button_page.destroy()

def update_user():
    global u_U_name, u_birth, u_gender, u_address, u_phone, u_field, combo_box, update_after, update_user_button_page
    update_user_button_page = Toplevel()
    update_user_button_page.title("사용자 수정")
    
    u_U_name, update_after, u_field = StringVar(), StringVar(), StringVar()

    ttk.Label(update_user_button_page, text = "수정할 사용자 이름 : ").grid(row = 0, column = 0, padx = 5, pady = 10)
    ttk.Entry(update_user_button_page, textvariable = u_U_name).grid(row = 0, column = 1, padx = 5, pady = 10)

    ttk.Label(update_user_button_page, text = "수정할 대상 항목 : ").grid(row = 1, column = 0, padx = 5, pady = 10)
    options = ['성별', '주소', '전화번호']
    combo_box = ttk.Combobox(update_user_button_page, values=options)
    combo_box.grid(row=1, column=1, padx=5, pady=10)
    combo_box.config(width = 15)
    combo_box.config(state="readonly") 
    combo_box.set("대상 선택")  

    ttk.Label(update_user_button_page, text = "수정 후 항목 : ").grid(row = 3, column = 0, padx = 5, pady = 10)
    ttk.Entry(update_user_button_page, textvariable = update_after).grid(row = 3, column = 1, padx = 5, pady = 10)

    ttk.Button(update_user_button_page, text = "수정", command = update_user_Button).grid(row = 4, column = 1, padx = 5, pady = 10)

def update_user_Button():
    u_field = []
    u_field.append(combo_box.get())
    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='anyangu_db', charset='utf8')
    cur = conn.cursor()
    if u_field[0] == '성별':
        sql = "UPDATE User_table SET gender = '" + str(update_after.get()) + "'" + " WHERE U_name = " + "'" + str(u_U_name.get()) + "';"

    if u_field[0] == '주소':
        sql = "UPDATE User_table SET address = '" + str(update_after.get()) + "'" + " WHERE U_name = " + "'" + str(u_U_name.get()) + "';"

    if u_field[0] == '전화번호':
        sql = "UPDATE User_table SET phone = '" + str(update_after.get()) + "'" + " WHERE U_name = " + "'" + str(u_U_name.get()) + "';"
    
    cur.execute(sql)
    conn.commit()
    conn.close()
    messagebox.showinfo('수정 완료', "사용자 '" + str(u_U_name.get()) + "' 의 " + u_field[0] + "가 수정 되었습니다!")
    select()
    update_user_button_page.destroy()

def select():
    strData1, strData2, strData3, strData4, strData5,   = [], [], [], [], []
    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='anyangu_db', charset='utf8')
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM User_table;")

    strData1.append("사용자 이름")      
    strData2.append("생년월일")
    strData3.append("성별")   
    strData4.append("주소")
    strData5.append("전화번호")
    
    strData1.append("-----------")
    strData2.append("-----------")
    strData3.append("-----------")
    strData4.append("-----------")
    strData5.append("-----------")
    
    while (True) :
        row = cur.fetchone()
        if row== None :
            break;
        strData1.append(row[0]);        strData2.append(row[1])
        strData3.append(row[2]);        strData4.append(row[3])
        strData5.append(row[4]);        

    frame1.delete(0,frame1.size() - 1);    frame2.delete(0,frame2.size() - 1) #입력 후 Entry값 초기화
    frame3.delete(0,frame3.size() - 1);    frame4.delete(0,frame4.size() - 1)
    frame5.delete(0,frame5.size() - 1);    
    
    for item1, item2, item3, item4, item5,  in zip(strData1, strData2, strData3, strData4, strData5,  ):
        frame1.insert(END, item1);        frame2.insert(END, item2)
        frame3.insert(END, item3);        frame4.insert(END, item4)
        frame5.insert(END, item5);        
    conn.close()