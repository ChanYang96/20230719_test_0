import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter import ttk

def selsct(Cname):
    strData1, strData2, strData3, strData4, strData5, strData6, strData7  = [], [], [], [], [], [], []
    #messagebox.showinfo('테스트', User_name)
    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='anyangu_db', charset='utf8')
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM Borrow_table WHERE C_name = " + "'" + Cname + "';")

    strData1.append("책 이름")
    strData2.append("대여 수량(권)")      
    strData3.append("카드번호")
    strData4.append("이름")   
    strData5.append("대여 일자")
    strData6.append("반납 일자")
    strData7.append("상태")
    
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

def borrow_list_main(Cname):
    #name = U_name
    book_list = Tk()  
    book_list.geometry("1100x220")
    book_list.title("대여 목록")

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

    Button1 = Button(book_list, text="조회", command = lambda : selsct(Cname))
    Button1.place(x=15,y=175,width=50,height=30,)


    