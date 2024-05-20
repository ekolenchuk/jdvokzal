from tkinter import*

W1=Tk()
W1.config(width=1200, height=900)
p1 = PhotoImage(file="фон.png")
L = Label(W1, image=p1)
L.place(x=-1,y=-1,width=1200,height=900)

#картинки(стремные, но мне так проще делать, Леша потом сам задизайнит, старалась использовать говорящие переменные,
#чтобы проще было заменять потом только файлы картинок, ну и останется подогнать масштаб в коде)
p2=PhotoImage(file="купить.png")
p3=PhotoImage(file="купитьнаведение.png")
p4=PhotoImage(file="заказы.png")
p5=PhotoImage(file="заказынаведение.png")
p6=PhotoImage(file="отзыв.png")
p7=PhotoImage(file="отзывнаведение.png")
#окошко купить билеты
def buy():
    W2 = Toplevel(W1)
    W2.config(width=1200, height=900)
    L2 = Label(W2, image=p2, borderwidth=0)

    W2.grab_set()
    W2.mainloop()
def buy1(e):
   Buy['image'] = p3
def buy2(e):
    Buy['image'] = p2
Buy = Button(W1, image=p2, borderwidth=0, command= buy)
Buy.place(x=450, y=400, width = 300, height= 52)
Buy.bind('<Enter>', buy1)
Buy.bind('<Leave>', buy2)

#окошко мои заказы
def orders():
    W3 = Toplevel(W1)
    W3.config(width=1200, height=900)
    L3=Label(W3, image = p4, borderwidth=0)

    W3.grab_set()
    W3.mainloop()
def orders1(e):
    Orders['image'] = p5
def orders2(e):
    Orders['image'] = p4

Orders = Button(W1, image=p4, borderwidth=0, command= orders)
Orders.place(x=450, y=550, width=300, height=52)
Orders.bind('<Enter>', orders1)
Orders.bind('<Leave>', orders2)

def feedback():
    W4 = Toplevel(W1)
    W4.config(width=1200, height=900)
    L4=Label(W4, image=p6, borderwidth=0)

    W4.grab_set()
    W4.mainloop()

def feedback1(e):
    Feedback['image'] = p7
def feedback2(e):
    Feedback['image'] = p6

Feedback = Button(W1, image=p6, borderwidth=0, command= feedback)
Feedback.place(x=450, y=700, width=300, height=52)
Feedback.bind('<Enter>', feedback1)
Feedback.bind('<Leave>', feedback2)


W1.mainloop()