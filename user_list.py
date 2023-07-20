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

    strData1, strData2, strData3, strData4, strData5,   = [], [], [], [], []
    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='anyangu_db', charset='utf8')
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM User_table WHERE U_name = " + "'" + Uname + "';")

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