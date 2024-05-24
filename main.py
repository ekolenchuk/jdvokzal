from tkinter import*

W1=Tk()
W1.config(width=1200, height=900)
p1 = PhotoImage(file="фон.png")
L = Label(W1, image=p1)
L.place(x=-1,y=-1,width=1200,height=900)

#картинки(стремные, но мне так проще делать, Леша потом сам задизайнит, старалась использовать говорящие названия,
#чтобы проще было заменять потом только файлы картинок, ну и останется подогнать масштаб в коде)
p2=PhotoImage(file="купить.png")
p3=PhotoImage(file="купитьнаведение.png")
p4=PhotoImage(file="заказы.png")
p5=PhotoImage(file="заказынаведение.png")
p6=PhotoImage(file="отзыв.png")
p7=PhotoImage(file="отзывнаведение.png")

# Картинка для логотипа (на сайте подсмотрела)
p3_1 = PhotoImage(file="логотипзаказы.png")

# Список купленных билетов. Данные после внесения на втором окне записываются сюда
# Я пока сама данные придумала для наглядности
Tickets = [("126548", "Иванов", "Иван", "Семенович", "6217080645", "Екатеринбург - Санкт-Петербург", "12.03.24",
                "18:46 мск", "12568"),
               ("135764", "Иванова", "Алевтина", "Михайловна", "6217157956", "Екатеринбург - Перьм", "12.03.24",
                "18:46 мск", "12568"),
               ("135764", "Белова", "Лиза", "Антоновна", "6217468756", "Екатеринбург - Перьм", "12.03.24", "18:46 мск",
                "12568")]

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
    W3.title("МОИ ЗАКАЗЫ")
    L3 = (Label(W3, image=p3_1, borderwidth=0)).place(x=10, y=14)
    l_phone = Label(W3,
                       anchor='center',
                       text="8 (800) 707-36-39\n8 (499) 116 36 36",
                       font=("Bahnschrift Condensed", 20, "italic"))
    l_phone.place(x=760, y=14, width=200, height=100)
    
    title = ((Label(W3, text="Заказы", font=("Bahnschrift Condensed", 34, "italic"), anchor='center'))
             .place(x=350, y=50, width=340, height=60))

    num_order = ((Label(W3, text="Номер заказа", bg="red", fg="white", font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
                 .place(x=30, y=130, width=120, height=20))
    name = ((Label(W3, text="ФИО", bg="red", fg="white", font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
            .place(x=170, y=130, width=160, height=20))
    document = ((Label(W3, text="Документ", bg="red", fg="white", font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
                .place(x=350, y=130, width=120, height=20))
    train = ((Label(W3, text="Поезд", bg="red", fg="white", font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
             .place(x=490, y=130, width=220, height=20))
    time = ((Label(W3, text="Отправление", bg="red", fg="white", font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
            .place(x=730, y=130, width=120, height=20))
    price = ((Label(W3, text="Цена", bg="red", fg="white", font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
             .place(x=870, y=130, width=120, height=20))

    num_ticket = 0
    for ticket in Tickets:
        pas_num_order1 = ((Label(W3, text=ticket[0], font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
                          .place(x=30, y=190 + num_ticket * 110, width=120, height=40))
        pas_name = ((Label(W3, text=ticket[1] + "\n" + ticket[2] + "\n" + ticket[3], font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
                    .place(x=170, y=190 + num_ticket * 110, width=160, height=80))
        pas_document = ((Label(W3, text=ticket[4], font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
                        .place(x=350, y=190 + num_ticket * 110, width=120, height=40))
        pas_train = ((Label(W3, text=ticket[5], font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
                     .place(x=490, y=190 + num_ticket * 110, width=220, height=40))
        pas_time = ((Label(W3, text=ticket[6] + "\n" + ticket[7], font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
                    .place(x=730, y=190 + num_ticket * 110, width=120, height=60))
        pas_price = ((Label(W3, text=ticket[8] + "руб.", font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
                     .place(x=870, y=190 + num_ticket * 110, width=120, height=40))
        line = ((Label(W3, text="-" * 500, fg="red"))
                .place(x=30, y=280 + num_ticket * 110, width=960, height=10))
        num_ticket = num_ticket + 1

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
