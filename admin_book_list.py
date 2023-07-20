import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter import ttk
def selsct(Uname):
    strData1, strData2, strData3, strData4, strData5, strData6, strData7  = [], [], [], [], [], [], []
    #messagebox.showinfo('테스트', User_name)
    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='anyangu_db', charset='utf8')
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM Book_table;")

    strData1.append("책 이름")      
    strData2.append("저자")
    strData3.append("출판사")   
    strData4.append("분야")
    strData5.append("재고")
    strData6.append("위치")
    strData7.append("특이사항")
    
    strData1.append("-----------")
    strData2.append("-----------")
    strData3.append("-----------")
    strData4.append("-----------")
    strData5.append("-----------")
    strData6.append("-----------")
    strData7.append("-----------")
    
    while (True) :
        row = cur.fetchone()
        if row== None :
            break;
        strData1.append(row[0]);        strData2.append(row[1])
        strData3.append(row[2]);        strData4.append(row[3])
        strData5.append(row[4]);        strData6.append(row[5])
        strData7.append(row[6])

    frame1.delete(0,frame1.size() - 1);    frame2.delete(0,frame2.size() - 1) #입력 후 Entry값 초기화
    frame3.delete(0,frame3.size() - 1);    frame4.delete(0,frame4.size() - 1)
    frame5.delete(0,frame5.size() - 1);    frame6.delete(0,frame6.size() - 1)
    frame7.delete(0,frame7.size() - 1)
    
    for item1, item2, item3, item4, item5, item6, item7 in zip(strData1, strData2, strData3, strData4, strData5, strData6, strData7 ):
        frame1.insert(END, item1);        frame2.insert(END, item2)
        frame3.insert(END, item3);        frame4.insert(END, item4)
        frame5.insert(END, item5);        frame6.insert(END, item6)
        frame7.insert(END, item7)
    conn.close()

def delete_book():
    global d_B_name, delete_book_button_page
    delete_book_button_page = Toplevel()
    delete_book_button_page.geometry("500x100+800+350")
    delete_book_button_page.title("도서 제거")
    d_B_name = StringVar()
    ttk.Label(delete_book_button_page, text = "제거할 서적 이름 : ").grid(row = 0, column = 0, padx = 5, pady = 10)
    ttk.Entry(delete_book_button_page, textvariable = d_B_name).grid(row = 0, column = 1, padx = 5, pady = 10)
    ttk.Button(delete_book_button_page, text = "제거", command = delete_book_Button).grid(row = 2, column = 1, padx = 5, pady = 10)

def delete_book_Button():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='anyangu_db', charset='utf8')
    cur = conn.cursor()
    sql = "DELETE FROM book_table WHERE B_name = '" +  str(d_B_name.get()) + "';"
    cur.execute(sql)
    conn.commit()
    conn.close()
    messagebox.showinfo('제거 완료', "서적 '" + str(d_B_name.get()) + "' 제거 완료!")
    selsct(d_B_name)
    delete_book_button_page.destroy()

def insert_book():
    global i_B_name, i_author, i_publisher, i_theme, i_quantity, i_floor, i_maintenance, insert_book_button_page
    insert_book_button_page = Toplevel()
    #insert_book_button_page.geometry("500x100+800+350")
    insert_book_button_page.title("도서 제거")
    i_B_name, i_author, i_publisher, i_theme, i_quantity, i_floor, i_maintenance = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
    ttk.Label(insert_book_button_page, text = "추가할 서적 이름 : ").grid(row = 0, column = 0, padx = 5, pady = 10)
    ttk.Entry(insert_book_button_page, textvariable = i_B_name).grid(row = 0, column = 1, padx = 5, pady = 10)

    ttk.Label(insert_book_button_page, text = "추가할 서적의 저자 : ").grid(row = 1, column = 0, padx = 5, pady = 10)
    ttk.Entry(insert_book_button_page, textvariable = i_author).grid(row = 1, column = 1, padx = 5, pady = 10)

    ttk.Label(insert_book_button_page, text = "추가할 서적의 출판사 : ").grid(row = 2, column = 0, padx = 5, pady = 10)
    ttk.Entry(insert_book_button_page, textvariable = i_publisher).grid(row = 2, column = 1, padx = 5, pady = 10)

    ttk.Label(insert_book_button_page, text = "추가할 서적의 분야 : ").grid(row = 3, column = 0, padx = 5, pady = 10)
    ttk.Entry(insert_book_button_page, textvariable = i_theme).grid(row = 3, column = 1, padx = 5, pady = 10)

    ttk.Label(insert_book_button_page, text = "추가할 서적의 재고 : ").grid(row = 4, column = 0, padx = 5, pady = 10)
    ttk.Entry(insert_book_button_page, textvariable = i_quantity).grid(row = 4, column = 1, padx = 5, pady = 10)

    ttk.Label(insert_book_button_page, text = "추가할 서적의 층(위치) : ").grid(row = 5, column = 0, padx = 5, pady = 10)
    ttk.Entry(insert_book_button_page, textvariable = i_floor).grid(row = 5, column = 1, padx = 5, pady = 10)

    ttk.Label(insert_book_button_page, text = "추가할 서적의 특이사항 : ").grid(row = 6, column = 0, padx = 5, pady = 10)
    ttk.Entry(insert_book_button_page, textvariable = i_maintenance).grid(row = 6, column = 1, padx = 5, pady = 10)


    ttk.Button(insert_book_button_page, text = "추가", command = insert_book_Button).grid(row = 7, column = 1, padx = 5, pady = 10)

def insert_book_Button():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='anyangu_db', charset='utf8')
    cur = conn.cursor()
    sql = "INSERT INTO book_table VALUES('" + str(i_B_name.get()) + "', '" + str(i_author.get()) + "', '" + str(i_publisher.get()) + "', '" + str(i_theme.get()) + "', '" + str(i_quantity.get()) + "', '" + str(i_floor.get()) + "', '" + str(i_maintenance.get()) + "');"
    cur.execute(sql)
    conn.commit()
    conn.close()
    messagebox.showinfo('추가 완료', "서적 '" + str(i_B_name.get()) + "' 추가 완료!")
    selsct(i_B_name)
    insert_book_button_page.destroy()

def update_book():
    global u_B_name, u_author, u_publisher, u_theme, u_quantity, u_floor, u_maintenance, u_field, combo_box, update_before, update_after, update_book_button_page
    update_book_button_page = Toplevel()
    #insert_book_button_page.geometry("500x100+800+350")
    update_book_button_page.title("도서 수정")
    
    u_B_name, update_before, update_after, u_field = StringVar(), StringVar(), StringVar(), StringVar()

    ttk.Label(update_book_button_page, text = "수정할 서적 이름 : ").grid(row = 0, column = 0, padx = 5, pady = 10)
    ttk.Entry(update_book_button_page, textvariable = u_B_name).grid(row = 0, column = 1, padx = 5, pady = 10)

    ttk.Label(update_book_button_page, text = "수정할 대상 항목 : ").grid(row = 1, column = 0, padx = 5, pady = 10)
    options = ['분야', '재고', '위치', '특이사항']
    combo_box = ttk.Combobox(update_book_button_page, values=options)
    combo_box.grid(row=1, column=1, padx=5, pady=10)
    combo_box.config(width = 15)
    combo_box.config(state="readonly") 
    combo_box.set("대상 선택")  

    #ttk.Label(update_book_button_page, text = "수정할 대상 항목 : ").grid(row = 1, column = 0, padx = 5, pady = 10)
    #ttk.Entry(update_book_button_page, textvariable = u_field).grid(row = 1, column = 1, padx = 5, pady = 10)

    #ttk.Label(update_book_button_page, text = "수정 전 항목 : ").grid(row = 2, column = 0, padx = 5, pady = 10)
    #ttk.Entry(update_book_button_page, textvariable = update_before).grid(row = 2, column = 1, padx = 5, pady = 10)

    ttk.Label(update_book_button_page, text = "수정 후 항목 : ").grid(row = 3, column = 0, padx = 5, pady = 10)
    ttk.Entry(update_book_button_page, textvariable = update_after).grid(row = 3, column = 1, padx = 5, pady = 10)

    ttk.Button(update_book_button_page, text = "수정", command = update_book_Button).grid(row = 4, column = 1, padx = 5, pady = 10)

def update_book_Button():
    u_field = []
    u_field.append(combo_box.get())
    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='anyangu_db', charset='utf8')
    cur = conn.cursor()
    if u_field[0] == '분야':
        sql = "UPDATE Book_table SET theme = '" + str(update_after.get()) + "'" + " WHERE B_name = " + "'" + str(u_B_name.get()) + "';"

    if u_field[0] == '재고':
        sql = "UPDATE Book_table SET quantity = " + str(update_after.get()) + " WHERE B_name = " + "'" + str(u_B_name.get()) + "';"

    if u_field[0] == '위치':
        sql = "UPDATE Book_table SET floor = '" + str(update_after.get()) + "'" + " WHERE B_name = " + "'" + str(u_B_name.get()) + "';"

    if u_field[0] == '특이사항':
        sql = "UPDATE Book_table SET maintenance = '" + str(update_after.get()) + "'" + " WHERE B_name = " + "'" + str(u_B_name.get()) + "';"
    
    cur.execute(sql)
    conn.commit()
    conn.close()
    messagebox.showinfo('수정 완료', "서적 '" + str(u_B_name.get()) + "' 의 " + u_field[0] + "가 수정 되었습니다!")
    selsct(u_B_name)
    update_book_button_page.destroy()

def book_list_main(Uname, Cname):
    book_list = Tk()  
    book_list.geometry("1100x220")
    book_list.title("서적 목록")

    global frame1, frame2, frame3, frame4, frame5, frame6, frame7, combobox
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
    frame6 = Listbox(book_list, relief='ridge', bd=1);
    frame6.pack(side='left', fill='both', expand=True);
    frame7 = Listbox(book_list, relief='ridge', bd=1);
    frame7.pack(side='left', fill='both', expand=True);

    Button1 = Button(book_list, text="조회", command = lambda : selsct(Uname))
    Button1.place(x=15,y=175,width=50,height=30,)

    Button2 = Button(book_list, text="서적 정보 수정", command = update_book)
    Button2.place(x=80,y=175,width=180,height=30,)

    Button3 = Button(book_list, text="서적 추가", command = insert_book)
    Button3.place(x=280,y=175,width=130,height=30,)

    Button4 = Button(book_list, text="서적 제거", command = delete_book)
    Button4.place(x=425,y=175,width=130,height=30,)