from tkinter import*
from tkinter import ttk #theme of tk
from tkinter import messagebox
import webbrowser as web

GUI = Tk ()
GUI.title('โปรแกรมบันทึกข้อมูล') #ขื่อโปรแกรม
GUI.geometry ('800x600') #ขนาดโปรแกรม

L1=Label (GUI,text='โปรแกรมเรียน python พื้นฐาน',font= ('Angsana New',30),fg='blue')
L1.place(x=180,y=20)
L2=Label (GUI,text='ขอขอบคุณ "Uncle Engineer"',font= ('Angsana New',30),fg='blue')
L2.place(x=380,y=400)

#B1=ttk.Button(GUI,text="Knowledge today")
#B1.pack(ipadx=20,ipady=20) #ขนาดปุ่ม
#####
def Button1() :
    #text = 'ยอดเยี่ยมเราทำได้'
    url='https://youtube.com/live/j1GCwOiACqw?feature=share'
    web.open(url)
    #messagebox.showinfo('มีความรู้เท่าไรแล้วจ๊ะ',text)
FB1 = Frame(GUI)
FB1.place(x=80,y=80)
B2=ttk.Button(FB1,text='เรียน python ep1',command=Button1)
B2.pack(ipadx=20,ipady=20)
#########
def Button2() :
    #text = 'ยอดเยี่ยมเราทำได้'
    url='https://youtube.com/live/4sj5bS2LVGQ?feature=share'
    web.open(url)
    #messagebox.showinfo('มีความรู้เท่าไรแล้วจ๊ะ',text)
FB1 = Frame(GUI)
FB1.place(x=80,y=160)
B2=ttk.Button(FB1,text='เรียน python ep2',command=Button2)
B2.pack(ipadx=20,ipady=20)
##########
def Button3() :
    url='https://youtube.com/live/x-XKkeGWnaQ?feature=share'
    web.open(url)
FB1 = Frame(GUI)
FB1.place(x=80,y=240)
B2=ttk.Button(FB1,text='เรียน python ep3',command=Button3)
B2.pack(ipadx=20,ipady=20)
##########
def Button4() :
    url='https://youtube.com/live/1ISiyDS6JOo?feature=share'
    web.open(url)
FB1 = Frame(GUI)
FB1.place(x=80,y=320)
B2=ttk.Button(FB1,text='เรียน python ep4',command=Button4)
B2.pack(ipadx=20,ipady=20)
##########
def Button5() :
    url='https://youtube.com/live/w_LIoaRlZlk?feature=share'
    web.open(url)
FB1 = Frame(GUI)
FB1.place(x=80,y=400)
B2=ttk.Button(FB1,text='เรียน python ep5',command=Button5)
B2.pack(ipadx=20,ipady=20)
##########
def Button6() :
    #text = 'ยอดเยี่ยมเราทำได้'
    url='https://youtube.com/live/Y18cPLLyw3Y?feature=share'
    web.open(url)
    #messagebox.showinfo('มีความรู้เท่าไรแล้วจ๊ะ',text)
FB1 = Frame(GUI)
FB1.place(x=380,y=80)
B2=ttk.Button(FB1,text='เรียน python ep6',command=Button6)
B2.pack(ipadx=20,ipady=20)
##########
def Button7() :
    #text = 'ยอดเยี่ยมเราทำได้'
    url='https://youtube.com/live/oMFElGGAT5Y?feature=share'
    web.open(url)
    #messagebox.showinfo('มีความรู้เท่าไรแล้วจ๊ะ',text)
FB1 = Frame(GUI)
FB1.place(x=380,y=160)
B2=ttk.Button(FB1,text='เรียน python ep7',command=Button7)
B2.pack(ipadx=20,ipady=20)
##########
def Button8() :
    #text = 'ยอดเยี่ยมเราทำได้'
    url='https://www.youtube.com/playlist?list=PL303UszemaD1JWJYZkz53tpeSmNsaN1EQ'
    web.open(url)
    #messagebox.showinfo('มีความรู้เท่าไรแล้วจ๊ะ',text)
FB1 = Frame(GUI)
FB1.place(x=380,y=240)
B2=ttk.Button(FB1,text='เรียน python all clip',command=Button8)
B2.pack(ipadx=20,ipady=20)
##########

GUI.mainloop ()
