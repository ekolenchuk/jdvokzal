from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

W1 = Tk()
W1.config(width=1200, height=900)
p1 = PhotoImage(file="фон.png")
L = Label(W1, image=p1)
L.place(x=-1, y=-1, width=1200, height=900)

# картинки(стремные, но мне так проще делать, Леша потом сам задизайнит, старалась использовать говорящие названия,
# чтобы проще было заменять потом только файлы картинок, ну и останется подогнать масштаб в коде)
p2 = PhotoImage(file="купить.png")
p3 = PhotoImage(file="купитьнаведение.png")
p4 = PhotoImage(file="заказы.png")
p5 = PhotoImage(file="заказынаведение.png")
p6 = PhotoImage(file="отзыв.png")
p7 = PhotoImage(file="отзывнаведение.png")
p8 = PhotoImage(file="билет.png")
p9 = PhotoImage(file="билетнаведение.png")
p10 = PhotoImage(file="отправить.png")
p11 = PhotoImage(file="отправитьнаведение.png")
p12 = PhotoImage(file="Спасибо.png")
p13 = PhotoImage(file="спасибозаотзыв.png")
p14 = PhotoImage(file="неввели.png")
# Картинка для логотипа (на сайте подсмотрела)
p3_1 = PhotoImage(file="логотипзаказы.png")

Tickets = []

# окошко купить билеты
def buy():
    W2 = Toplevel(W1)
    W2.config(width=1200, height=900)
    L2 = Label(W2, image=p2, borderwidth=0)
    L2.place(x=-1, y=-1, width=1200, height=900)

    def buy3():
        W5 = Toplevel(W2)
        W5.config(width=1200, height=900)
        L5 = Label(W5, image=p8, borderwidth=0)
        L5.place(x=-1, y=-1, width=1200, height=900)

        def check():
            name = entry.get()
            entry.delete(0, 'end')
            num_order = str(random.randint(100000, 999999))
            surname = entry2.get()
            entry2.delete(0, 'end')
            Tickets.append((num_order, surname, name, "", "", "", "", "", ""))

            W8 = Toplevel(W5)
            W8.config(width=1200, height=900)
            L8 = Label(W8, image=p12, borderwidth=0)
            L8.place(x=-1, y=-1, width=1200, height=900)

            W8.grab_set()
            W8.mainloop()

        def check1(e):
            Check['image'] = p11

        def check2(e):
            Check['image'] = p10

        Check = Button(W5, image=p10, borderwidth=0, command=check)
        Check.place(x=500, y=500, width=300, height=50)
        Check.bind('<Enter>', check1)
        Check.bind('<Leave>', check2)

        def on_validate_input(char):
            if char.isalpha() or char == "":
                return True
            else:
                return False



        vcmd = W5.register(on_validate_input)
        entry = ttk.Entry(W5, validate="key", validatecommand=(vcmd, '%P'))
        entry.pack()

        entry.config(width=50)  # Ширина окна ввода
        entry.place(x=400, y=300)  # Положение окна ввода в окне

        entry2 = ttk.Entry(W5, validate="key", validatecommand=(vcmd, '%P'))
        entry2.pack()

        entry2.config(width=50)  # Ширина окна ввода
        entry2.place(x=400, y=400)  # Положение окна ввода в окне

        LABEL_1 = ttk.Label(W5, anchor=ttk.CENTER, font=('Calibri light', '14', 'bold'), text="Введите свои данные").place(x=400, y=200)
        LABEL_2 = ttk.Label(W5, anchor=ttk.CENTER, font=('Calibri light', '14', 'bold'), text="Фамилия:").place(x=300, y=300)
        LABEL_3 = ttk.Label(W5, anchor=ttk.CENTER, font=('Calibri light', '14', 'bold'), text="Имя:").place(x=300, y=400)

        W5.grab_set()
        W5.mainloop()

    def buy4(e):
        Buy1['image'] = p9

    def buy5(e):
        Buy1['image'] = p8

    Buy1 = Button(W2, image=p8, borderwidth=0, command=buy3)
    Buy1.place(x=200, y=100, width=800, height=200)
    Buy1.bind('<Enter>', buy4)
    Buy1.bind('<Leave>', buy5)

    def buy6():
        W6 = Toplevel(W2)
        W6.config(width=1200, height=900)
        L6 = Label(W6, image=p8, borderwidth=0)
        L6.place(x=-1, y=-1, width=1200, height=900)

        def check():
            name = entry.get()
            entry.delete(0, 'end')
            num_order = str(random.randint(100000, 999999))
            surname = entry2.get()
            entry2.delete(0, 'end')
            Tickets.append((num_order, surname, name, "", "", "", "", "", ""))

            W8 = Toplevel(W6)
            W8.config(width=1200, height=900)
            L8 = Label(W8, image=p12, borderwidth=0)
            L8.place(x=-1, y=-1, width=1200, height=900)

            W8.grab_set()
            W8.mainloop()

        def check1(e):
            Check['image'] = p11

        def check2(e):
            Check['image'] = p10

        Check = Button(W6, image=p10, borderwidth=0, command=check)
        Check.place(x=500, y=500, width=300, height=50)
        Check.bind('<Enter>', check1)
        Check.bind('<Leave>', check2)

        def on_validate_input(char):
            if char.isalpha() or char == "":
                return True
            else:
                return False

        vcmd = W6.register(on_validate_input)
        entry = ttk.Entry(W6, validate="key", validatecommand=(vcmd, '%P'))
        entry.pack()

        entry.config(width=50)  # Ширина окна ввода
        entry.place(x=400, y=300)  # Положение окна ввода в окне

        entry2 = ttk.Entry(W6, validate="key", validatecommand=(vcmd, '%P'))
        entry2.pack()

        entry2.config(width=50)  # Ширина окна ввода
        entry2.place(x=400, y=400)  # Положение окна ввода в окне

        LABEL_1 = ttk.Label(W6, anchor=ttk.CENTER, font=('Calibri light', '14', 'bold'), text="Введите свои данные").place(x=400, y=200)
        LABEL_2 = ttk.Label(W6, anchor=ttk.CENTER, font=('Calibri light', '14', 'bold'), text="Фамилия:").place(x=300, y=300)
        LABEL_3 = ttk.Label(W6, anchor=ttk.CENTER, font=('Calibri light', '14', 'bold'), text="Имя:").place(x=300, y=400)

        W6.grab_set()
        W6.mainloop()

    def buy7(e):
        Buy2['image'] = p9

    def buy8(e):
        Buy2['image'] = p8

    Buy2 = Button(W2, image=p8, borderwidth=0, command=buy6)
    Buy2.place(x=200, y=320, width=800, height=200)
    Buy2.bind('<Enter>', buy7)
    Buy2.bind('<Leave>', buy8)

    def buy9():
        W7 = Toplevel(W2)
        W7.config(width=1200, height=900)
        L7 = Label(W7, image=p8, borderwidth=0)
        L7.place(x=-1, y=-1, width=1200, height=900)

        def check():
            name = entry.get()
            entry.delete(0, 'end')
            num_order = str(random.randint(100000, 999999))
            surname = entry2.get()
            entry2.delete(0, 'end')
            Tickets.append((num_order, surname, name, "", "", "", "", "", ""))

            W8 = Toplevel(W7)
            W8.config(width=1200, height=900)
            L8 = Label(W8, image=p12, borderwidth=0)
            L8.place(x=-1, y=-1, width=1200, height=900)

            W8.grab_set()
            W8.mainloop()

        def check1(e):
            Check['image'] = p11

        def check2(e):
            Check['image'] = p10

        Check = Button(W7, image=p10, borderwidth=0, command=check)
        Check.place(x=500, y=500, width=300, height=50)
        Check.bind('<Enter>', check1)
        Check.bind('<Leave>', check2)

        def on_validate_input(char):
            if char.isalpha() or char == "":
                return True
            else:
                return False

        vcmd = W7.register(on_validate_input)
        entry = ttk.Entry(W7, validate="key", validatecommand=(vcmd, '%P'))
        entry.pack()

        entry.config(width=50)  # Ширина окна ввода
        entry.place(x=400, y=300)  # Положение окна ввода в окне

        entry2 = ttk.Entry(W7, validate="key", validatecommand=(vcmd, '%P'))
        entry2.pack()

        entry2.config(width=50)  # Ширина окна ввода
        entry2.place(x=400, y=400)  # Положение окна ввода в окне

        LABEL_1 = ttk.Label(W7, anchor=ttk.CENTER, font=('Calibri light', '14', 'bold'), text="Введите свои данные").place(x=400, y=200)
        LABEL_2 = ttk.Label(W7, anchor=ttk.CENTER, font=('Calibri light', '14', 'bold'), text="Фамилия:").place(x=300, y=300)
        LABEL_3 = ttk.Label(W7, anchor=ttk.CENTER, font=('Calibri light', '14', 'bold'), text="Имя:").place(x=300, y=400)

        W7.grab_set()
        W7.mainloop()

    def buy10(e):
        Buy3['image'] = p9

    def buy11(e):
        Buy3['image'] = p8

    Buy3 = Button(W2, image=p8, borderwidth=0, command=buy9)
    Buy3.place(x=200, y=540, width=800, height=200)
    Buy3.bind('<Enter>', buy10)
    Buy3.bind('<Leave>', buy11)

    W2.grab_set()
    W2.mainloop()


def buy1(e):
    Buy['image'] = p3


def buy2(e):
    Buy['image'] = p2


Buy = Button(W1, image=p2, borderwidth=0, command=buy)
Buy.place(x=450, y=400, width=300, height=52)
Buy.bind('<Enter>', buy1)
Buy.bind('<Leave>', buy2)


# окошко мои заказы
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

    num_order = ((Label(W3, text="Номер заказа", bg="red", fg="white", font=("Bahnschrift Condensed", 14, "italic"),
                        anchor='center'))
                 .place(x=30, y=130, width=120, height=20))
    name = ((Label(W3, text="ФИО", bg="red", fg="white", font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
            .place(x=170, y=130, width=160, height=20))
    document = ((Label(W3, text="Документ", bg="red", fg="white", font=("Bahnschrift Condensed", 14, "italic"),
                       anchor='center'))
                .place(x=350, y=130, width=120, height=20))
    train = (
        (Label(W3, text="Поезд", bg="red", fg="white", font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
        .place(x=490, y=130, width=220, height=20))
    time = ((Label(W3, text="Отправление", bg="red", fg="white", font=("Bahnschrift Condensed", 14, "italic"),
                   anchor='center'))
            .place(x=730, y=130, width=120, height=20))
    price = (
        (Label(W3, text="Цена", bg="red", fg="white", font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
        .place(x=870, y=130, width=120, height=20))

    num_ticket = 0
    for ticket in Tickets:
        pas_num_order1 = ((Label(W3, text=ticket[0], font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
                          .place(x=30, y=190 + num_ticket * 110, width=120, height=40))
        pas_name = ((Label(W3, text=ticket[1] + "\n" + ticket[2] + "\n" + ticket[3],
                           font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
                    .place(x=170, y=190 + num_ticket * 110, width=160, height=80))
        pas_document = ((Label(W3, text=ticket[4], font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
                        .place(x=350, y=190 + num_ticket * 110, width=120, height=40))
        pas_train = ((Label(W3, text=ticket[5], font=("Bahnschrift Condensed", 14, "italic"), anchor='center'))
                     .place(x=490, y=190 + num_ticket * 110, width=220, height=40))
        pas_time = ((Label(W3, text=ticket[6] + "\n" + ticket[7], font=("Bahnschrift Condensed", 14, "italic"),
                           anchor='center'))
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


Orders = Button(W1, image=p4, borderwidth=0, command=orders)
Orders.place(x=450, y=550, width=300, height=52)
Orders.bind('<Enter>', orders1)
Orders.bind('<Leave>', orders2)


def feedback():
    W4 = Toplevel(W1)
    W4.config(width=1200, height=900)
    W4.title("ОТЗЫВ")
    main_text = Label(W4, text="Уважаемые пассажиры!\n"
                               "Если у вас есть претензии/пожелания по поводу нашей работы или слова благодарности,\n"
                               "оставьте, пожалуйста, отзыв!\n"
                               "Мы постараемся учесть ваши слова!", font=('Verdana', 16), bg="#ffffff", fg="#ff0000")
    main_text.place(x=130, y=70)
    L4 = Label(W4, image=p6, borderwidth=0)

    def otprav():
        answ = Vvod.get("1.0", "end-1c").strip()  # Получение многострочного текста
        Vvod.delete("1.0", END)

        if not answ:  # Проверка на пустой ввод
            Wo1 = Toplevel(W1)
            Wo1.config(width=486, height=236)
            Lo1 = Label(Wo1, image=p14, borderwidth=0)
            Lo1.place(x=0, y=0, width=486, height=236)
            Wo1.grab_set()
            Wo1.mainloop()
        else:
            Wo2 = Toplevel(W1)
            Wo2.config(width=486, height=236)
            Lo2 = Label(Wo2, image=p13, borderwidth=0)
            Lo2.place(x=0, y=0, width=486, height=236)
            Wo2.grab_set()
            Wo2.mainloop()

    Vvod = Text(W4, font=('Calibri light', 32), width=40, height=5)
    Vvod.place(x=150, y=270)

    Otprav = ttk.Style()
    Otprav.configure('primary.Outline.TButton', font=('Calibri light', 32))

    Botprav = ttk.Button(W4, text="ОТПРАВИТЬ", style='primary.Outline.TButton', width=20, command=otprav)
    Botprav.place(x=580, y=570)

    W4.grab_set()
    W4.mainloop()


def feedback1(e):
    Feedback['image'] = p7


def feedback2(e):
    Feedback['image'] = p6


Feedback = Button(W1, image=p6, borderwidth=0, command=feedback)
Feedback.place(x=450, y=700, width=300, height=52)
Feedback.bind('<Enter>', feedback1)
Feedback.bind('<Leave>', feedback2)

W1.mainloop()
