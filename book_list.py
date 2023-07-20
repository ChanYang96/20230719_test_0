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

    frame1.delete(0,frame1.size() - 1);    frame2.delete(0,frame2.size() - 1) #입력 후 Entry값 초기화
    frame3.delete(0,frame3.size() - 1);    frame4.delete(0,frame4.size() - 1)
    frame5.delete(0,frame5.size() - 1);    frame6.delete(0,frame6.size() - 1)
    
    for item1, item2, item3, item4, item5, item6 in zip(strData1, strData2, strData3, strData4, strData5, strData6 ):
        frame1.insert(END, item1);        frame2.insert(END, item2)
        frame3.insert(END, item3);        frame4.insert(END, item4)
        frame5.insert(END, item5);        frame6.insert(END, item6)
    conn.close()

def borrow_book_button(Uname, Cname):
    global borrow_book_button_page, Bname, Bcount, Int_Bcount, B_name, B_count
    borrow_book_button_page = Toplevel()
    borrow_book_button_page.geometry("600x150+800+350")       # 창 크기설정
    borrow_book_button_page.title("대여 서비스")
        
    B_name, B_count = StringVar(), StringVar()

    ttk.Label(borrow_book_button_page, text = Uname + "님이 대여할 책 이름 : ").grid(row = 0, column = 0, padx = 5, pady = 10)
    ttk.Label(borrow_book_button_page, text = "대여 수(권) : ").grid(row = 1, column = 0, padx = 5, pady = 10)
    ttk.Entry(borrow_book_button_page, textvariable = B_name).grid(row = 0, column = 1, padx = 5, pady = 10)
    ttk.Entry(borrow_book_button_page, textvariable = B_count).grid(row = 1, column = 1, padx = 5, pady = 10)
    #Bname = str(B_name.get())
    #Bcount = str(B_count.get())
    ttk.Button(borrow_book_button_page, text = "대여 요청", command = lambda : borrow_book_check(Uname, Cname)).grid(row = 2, column = 1, padx = 5, pady = 10)

def borrow_book_check(Uname, Cname):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='anyangu_db', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT quantity FROM Book_table WHERE B_name = " + "'" + str(B_name.get()) + "';"
    cur.execute(sql)
    row = cur.fetchone()
    Bname = str(B_name.get())
    Bcount = str(row[0])
    Int_Bcount = row[0]
    
    if Int_Bcount >= int(B_count.get()):
        sql = "UPDATE Book_table SET quantity = " + str(Int_Bcount - int(B_count.get())) + " WHERE B_name = " + "'" + Bname + "';"
        cur.execute(sql)
        conn.commit()

        sql = "INSERT INTO Borrow_table VALUES('" + Bname + "', '" + str(B_count.get()) + "', '" + Cname + "', '" + Uname + "', DATE_FORMAT(now(), '%Y-%m-%d'), DATE_ADD(NOW(), INTERVAL 14 DAY), '미반납');"
        cur.execute(sql)
        conn.commit()
        messagebox.showinfo('도서 대여', "대여 완료 감사합니다!")
        selsct(Bname)
        borrow_book_button_page.destroy()
    else:
        messagebox.showinfo('도서 대여', "수량이 부족하거나 잘못된 입력입니다!")
        
    conn.close()

def book_list_main(Uname, Cname):
    #name = U_name
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

    Button2 = Button(book_list, text="대여", command = lambda : borrow_book_button(Uname, Cname))
    Button2.place(x=80,y=175,width=50,height=30,)

    