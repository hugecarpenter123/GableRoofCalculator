import tkinter
from PIL import ImageTk, Image
from CieciaKrokwi import CieciaNaKrokwach
from rysuj_krokiew import rysuj
from symuluj_dach import symuluj


dach = None

root = tkinter.Tk()
root.geometry('900x600')
root.title('Wymiary i kąty krokwi')

img = Image.open("assets/dach_baza3.bmp")
img_resized = img.resize((900, 600))

bg = ImageTk.PhotoImage(img_resized)
bgLabel = tkinter.Label(root, image=bg)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
side_frame = tkinter.Frame(root, width=200, bg='white')
side_frame.place(x=20, y=20)

info_frame = tkinter.Frame(side_frame, width=200, padx=10, pady=10)
info_frame.grid(row=0, column=0)

def change_to_h():
    h_label['text'] = 'h = '
    cm_or_deg['text'] = 'cm'

def change_to_k():
    h_label['text'] = 'kąt = '
    cm_or_deg['text'] = '\N{DEGREE SIGN}'

def oblicz():
    global dach
    data = dict()
    if h_or_k.get() == 'h':
        data['h'] = float(h_entry.get())
    else:
        data['kat_dachu'] = 180 - (2 * float(h_entry.get()))

    if platwa_intVar.get():
        data['op'] = float(platwa_entry.get())
    if jetka_intVar.get():
        data['hj'] = float(jetka_entry.get())

    data['d'] = float(d_entry.get())
    data['h_krokwi'] = float(g_entry.get())
    data['p'] = float(p_entry.get())
    dach = CieciaNaKrokwach(data)

    uzupelnij_dane(dach)

def uzupelnij_dane(dach_obj):
    #frame 1
    k_c_wynik['text'] = str(dach_obj.d_krokwi_calkowita) + 'cm'
    k_w_wynik['text'] = str(dach_obj.d_k_w) + 'cm'
    k_z_wynik['text'] = str(dach_obj.kat_zaciecia) + '\N{DEGREE SIGN}'
    s_z_wynik['text'] = str(dach_obj.s_zaciecia) + 'cm'
    # frame 2
    d_r_wynik['text'] = str(dach_obj.depka['odległość']) + 'cm'
    d_zp_wynik['text'] = str(dach_obj.depka['kąt']) + '\N{DEGREE SIGN}'
    d_zr_wynik['text'] = str(dach_obj.depka['kąt2']) + '\N{DEGREE SIGN}'
    # frame 3
    k_roz_wynik['text'] = str(round(dach_obj.kat_dachu, 2)) + '\N{DEGREE SIGN}'
    kat_wynik['text'] = str(round((180 - dach_obj.kat_dachu) / 2, 2)) + '\N{DEGREE SIGN}'
    h_dach_wynik['text'] = str(dach_obj.h) + 'cm'
    # frame 4
    if platwa_intVar.get():
        p_c_wynik['text'] = str(dach_obj.hp) + 'cm'
        p_d_wynik['text'] = str(dach_obj.d_k_gp) + 'cm'
        p_opp_wynik['text'] = str(dach_obj.opp) + 'cm'
    # frame 5
    if jetka_intVar.get():
        j_c_wynik['text'] = str(dach_obj.d_j_c) + 'cm'
        j_o_wynik['text'] = str(dach_obj.d_j_kk) + 'cm'

def symulujFun():
    try:
        platwa = False
        jetka = False
        if platwa_intVar.get():
            platwa = True
        if jetka_intVar.get():
            jetka = True
        symuluj(dach, platwa, jetka)
    except:
        pass

def rysujFun():
    try:
        platwa = False
        if platwa_intVar.get():
            platwa = True
        rysuj(dach, platwa)
    except:
        pass

def hide_platwaInfo(arg: str):
    if arg == 'hide':
        outputFrame4.place_forget()
        platwa_label.grid_forget()
        platwa_entry.grid_forget()
        cm_platwa.grid_forget()

        platwa_entry.delete(0, 'end')
        p_c_wynik['text'] = 'cm'
        p_d_wynik['text'] = 'cm'
        p_opp_wynik['text'] = 'cm'
    else:
        outputFrame4.place(x=220, y=125)
        platwa_label.grid(row=6, column=0)
        platwa_entry.grid(row=6, column=1)
        cm_platwa.grid(row=6, column=2)

def hide_jetkaInfo(arg: str):
    if arg == 'hide':
        outputFrame5.place_forget()
        jetka_label.grid_forget()
        jetka_entry.grid_forget()
        cm_jetka.grid_forget()

        jetka_entry.delete(0, 'end')
        j_c_wynik['text'] = 'cm'
        j_o_wynik['text'] = 'cm'
    else:
        outputFrame5.place(x=590, y=125)
        jetka_label.grid(row=8, column=0)
        jetka_entry.grid(row=8, column=1)
        cm_jetka.grid(row=8, column=2)

def platwaFun():
    if platwa_intVar.get() == 1:
        hide_platwaInfo('show')

        if jetka_intVar.get() == 0:
            img = Image.open("assets/dach_baza3p.bmp")
            img_resized = img.resize((900, 600))
            bg = ImageTk.PhotoImage(img_resized)
            bgLabel['image'] = bg
            bgLabel.image = bg
        else:
            img = Image.open("assets/dach_baza3pj.bmp")
            img_resized = img.resize((900, 600))
            bg = ImageTk.PhotoImage(img_resized)
            bgLabel['image'] = bg
            bgLabel.image = bg
    else:
        hide_platwaInfo('hide')
        if jetka_intVar.get() == 0:
            img = Image.open("assets/dach_baza3.bmp")
            img_resized = img.resize((900, 600))
            bg = ImageTk.PhotoImage(img_resized)
            bgLabel['image'] = bg
            bgLabel.image = bg
        else:
            img = Image.open("assets/dach_baza3j.bmp")
            img_resized = img.resize((900, 600))
            bg = ImageTk.PhotoImage(img_resized)
            bgLabel['image'] = bg
            bgLabel.image = bg

def jetkaFun():
    if jetka_intVar.get() == 1:
        hide_jetkaInfo('show')

        if platwa_intVar.get() == 0:
            img = Image.open("assets/dach_baza3j.bmp")
            img_resized = img.resize((900, 600))
            bg = ImageTk.PhotoImage(img_resized)
            bgLabel['image'] = bg
            bgLabel.image = bg
        else:
            img = Image.open("assets/dach_baza3pj.bmp")
            img_resized = img.resize((900, 600))
            bg = ImageTk.PhotoImage(img_resized)
            bgLabel['image'] = bg
            bgLabel.image = bg
    else:
        hide_jetkaInfo('hide')

        if platwa_intVar.get() == 0:
            img = Image.open("assets/dach_baza3.bmp")
            img_resized = img.resize((900, 600))
            bg = ImageTk.PhotoImage(img_resized)
            bgLabel['image'] = bg
            bgLabel.image = bg
        else:
            img = Image.open("assets/dach_baza3p.bmp")
            img_resized = img.resize((900, 600))
            bg = ImageTk.PhotoImage(img_resized)
            bgLabel['image'] = bg
            bgLabel.image = bg


def on_closing():
    global run
    run = False
    root.destroy()

# info frame ================================================================
# radiobutton kąt/h ---------------------------------------------
inner_frame = tkinter.Frame(info_frame)
inner_frame.grid(row=0, column=0, columnspan=3)
h_or_k = tkinter.StringVar()
h_or_k.set('h')
h_radio = tkinter.Radiobutton(inner_frame, text="h", value='h', variable=h_or_k, command=change_to_h, font=('arial',10))
k_radio = tkinter.Radiobutton(inner_frame, text="kąt", value='k', variable=h_or_k, command=change_to_k, font=('arial',10))
h_radio.grid(row=0, column=0)
k_radio.grid(row=0, column=1)
# h row ---------------------------------------------
h_label = tkinter.Label(info_frame, text="h = ", font=('Arial', 12), width=4)
h_label.grid(row=1, column=0, padx=(0,20))
h_entry = tkinter.Entry(info_frame, width=8, font=('Arial', 10))
h_entry.grid(row=1, column=1)
cm_or_deg = tkinter.Label(info_frame, text="cm", font=('Arial', 11))
cm_or_deg.grid(row=1, column=2)
# d row ---------------------------------------------
d_label = tkinter.Label(info_frame, text="d = ", font=('Arial', 12))
d_label.grid(row=2, column=0, padx=(0,20))
d_entry = tkinter.Entry(info_frame, width=8, font=('Arial', 10))
d_entry.grid(row=2, column=1)
cm = tkinter.Label(info_frame, text="cm", font=('Arial', 11))
cm.grid(row=2, column=2)

# p row ---------------------------------------------
p_label = tkinter.Label(info_frame, text="p = ", font=('Arial', 12))
p_label.grid(row=3, column=0, padx=(0,20))
p_entry = tkinter.Entry(info_frame, width=8, font=('Arial', 10))
p_entry.grid(row=3, column=1)
cm = tkinter.Label(info_frame, text="cm", font=('Arial', 11))
cm.grid(row=3, column=2)
# g row ---------------------------------------------
g_label = tkinter.Label(info_frame, text="g = ", font=('Arial', 12))
g_label.grid(row=4, column=0, padx=(0,20))
g_entry = tkinter.Entry(info_frame, width=8, font=('Arial', 10))
g_entry.grid(row=4, column=1)
cm = tkinter.Label(info_frame, text="cm", font=('Arial', 11))
cm.grid(row=4, column=2)
# platwa checkbutton row ---------------------------------------------
platwa_intVar = tkinter.IntVar()
platwa_checkbox = tkinter.Checkbutton(info_frame, text="z płatwami", onvalue=1, offvalue=0, command=platwaFun
                                      , font=('arial', 10), variable=platwa_intVar)
platwa_checkbox.grid(row=5, column=0, columnspan=3, sticky='w')
# platwa row ---------------------------------------------
# platwa label:
platwa_label = tkinter.Label(info_frame, text="mp = ", font=('Arial', 12))
# platwa entry:
platwa_entry = tkinter.Entry(info_frame, width=8, font=('Arial', 10))
# platwa cm:
cm_platwa = tkinter.Label(info_frame, text="cm", font=('Arial', 11))

# jętka checkbutton row ---------------------------------------------
jetka_intVar = tkinter.IntVar()
jetka_checkbox = tkinter.Checkbutton(info_frame, text="z jętkami", onvalue=1, offvalue=0, command=jetkaFun
                                      , font=('arial', 10), variable=jetka_intVar)
jetka_checkbox.grid(row=7, column=0, columnspan=3, sticky='w')
# jętka row ---------------------------------------------
jetka_label = tkinter.Label(info_frame, text="hj = ", font=('Arial', 12))
jetka_entry = tkinter.Entry(info_frame, width=8, font=('Arial', 10))
cm_jetka = tkinter.Label(info_frame, text="cm", font=('Arial', 11))

# submit button
submitBtn = tkinter.Button(info_frame ,text="Oblicz", font=("Arial", 12), width=8, command=oblicz
                           , cursor='hand2')
submitBtn.grid(row=9, column=0, columnspan=3, pady=(10,0))
# end infoframe================================================================

# symuluj-dach button ---------------------------------------------
symulujBtn = tkinter.Button(side_frame, text='Symuluj dach', font=("Arial", 12), width=15, bg='lightgreen'
                            , cursor='hand2', command=symulujFun)
symulujBtn.grid(row=1, column=0, sticky='w', pady=(10,0))

# rysuj-krokiwe button ---------------------------------------------
rysujBtn = tkinter.Button(side_frame, text='Zarysuj krokiew', font=("Arial", 12), width=15, bg='lightblue'
                          , cursor='hand2', command=rysujFun)
rysujBtn.grid(row=2, column=0, sticky='w', pady=(5,0))


# output frame 1 ---------------------------------------------
outputFrame1 = tkinter.Frame(width=260, height=100, bd='4')
outputFrame1.place(x=220, y=20)

k_c = tkinter.Label(outputFrame1, text=f'{"Całkowita długość krokwi: "}', anchor='w')
k_w = tkinter.Label(outputFrame1, text=f'{"Długość krokwi (od zacięcia do zamka): "}' , anchor='w', bg='lightgrey')
k_z = tkinter.Label(outputFrame1, text=f'{"Kąt zacięcia krokwi: "}', anchor='w')
s_z = tkinter.Label(outputFrame1, text=f'{"Szerokość zacięcia: "}', anchor='w', bg='lightgrey')
k_c.grid(row=0, column=0, sticky='ew', ipadx=(20))
k_w.grid(row=1, column=0, sticky='ew')
k_z.grid(row=2, column=0, sticky='ew')
s_z.grid(row=3, column=0, sticky='ew')

k_c_wynik = tkinter.Label(outputFrame1, text='cm', anchor='w', bg='lightgrey')
k_w_wynik = tkinter.Label(outputFrame1, text='\N{DEGREE SIGN}', anchor='w')
k_z_wynik = tkinter.Label(outputFrame1, text='cm', anchor='w', bg='lightgrey')
s_z_wynik = tkinter.Label(outputFrame1, text='cm', anchor='w')
k_c_wynik.grid(row=0, column=1, sticky='ew')
k_w_wynik.grid(row=1, column=1, sticky='ew')
k_z_wynik.grid(row=2, column=1, sticky='ew')
s_z_wynik.grid(row=3, column=1, sticky='ew')


# output frame 2 ---------------------------------------------
outputFrame2 = tkinter.Frame(width=260, height=100, bd='4')
outputFrame2.place(x=220+260+20, y=20)

d = tkinter.Label(outputFrame2, text=f'{"Zamek"}', anchor='w', font=('arial', 9, 'bold'))
d_r = tkinter.Label(outputFrame2, text=f'{"Odległość od góry do zamka: "}' , anchor='w', bg='lightgrey')
d_zp = tkinter.Label(outputFrame2, text=f'{"Kąt prostopadły (do ziemi): "}', anchor='w')
d_zr = tkinter.Label(outputFrame2, text=f'{"Kąt równoległy (do ziemi): "}', anchor='w', bg='lightgrey')

d.grid(row=0, column=0, sticky='ew')
d_r.grid(row=1, column=0, sticky='ew', ipadx=(20))
d_zp.grid(row=2, column=0, sticky='ew')
d_zr.grid(row=3, column=0, sticky='ew')

d_wynik = tkinter.Label(outputFrame2, bg='lightgrey')
d_r_wynik = tkinter.Label(outputFrame2, text='cm', anchor='w')
d_zp_wynik = tkinter.Label(outputFrame2, text='\N{DEGREE SIGN}', anchor='w', bg='lightgrey')
d_zr_wynik = tkinter.Label(outputFrame2, text='cm', anchor='w')

d_wynik.grid(row=0, column=1, sticky='ew')
d_r_wynik.grid(row=1, column=1, sticky='ew')
d_zp_wynik.grid(row=2, column=1, sticky='ew')
d_zr_wynik.grid(row=3, column=1, sticky='ew')

# output frame 3 ---------------------------------------------
outputFrame3 = tkinter.Frame(root, height=100, width=80)
outputFrame3.place(x=765, y=20)

k_roz = tkinter.Label(outputFrame3, text=f'{"Kąt rozwarcia: "}', anchor='w')
kat = tkinter.Label(outputFrame3, text=f'{"Kąt: "}' , anchor='w', bg='lightgrey')
h_dach = tkinter.Label(outputFrame3, text=f'{"h: "}', anchor='w')

k_roz.grid(row=0, column=0, sticky='ew')
kat.grid(row=1, column=0, sticky='ew', ipadx=(20))
h_dach.grid(row=2, column=0, sticky='ew')

k_roz_wynik = tkinter.Label(outputFrame3, bg='lightgrey')
kat_wynik = tkinter.Label(outputFrame3, anchor='w')
h_dach_wynik = tkinter.Label(outputFrame3, anchor='w', bg='lightgrey')

k_roz_wynik.grid(row=0, column=1, sticky='ew')
kat_wynik.grid(row=1, column=1, sticky='ew')
h_dach_wynik.grid(row=2, column=1, sticky='ew')

# output frame 4 ------------------------------------------------------------------------------------------
outputFrame4 = tkinter.Frame(width=260, height=100, bd='4')
# outputFrame4.place(x=220, y=125)

p_c = tkinter.Label(outputFrame4, text=f'{"Długość słupka (+płatwa) od murłaty do krokwi: "}', anchor='w')
p_d = tkinter.Label(outputFrame4, text=f'{"Długość krokwi (od czubka do zamka na płatwę): "}' , anchor='w', bg='lightgrey')
p_opp = tkinter.Label(outputFrame4, text=f'{"Odległość między płatwami po zewnetrznej: "}', anchor='w')

p_c.grid(row=0, column=0, sticky='ew', ipadx=(20))
p_d.grid(row=1, column=0, sticky='ew')
p_opp.grid(row=2, column=0, sticky='ew')

p_c_wynik = tkinter.Label(outputFrame4, text='cm', anchor='w', bg='lightgrey')
p_d_wynik = tkinter.Label(outputFrame4, text='cm', anchor='w')
p_opp_wynik = tkinter.Label(outputFrame4, text='cm', anchor='w', bg='lightgrey')

p_c_wynik.grid(row=0, column=1, sticky='ew')
p_d_wynik.grid(row=1, column=1, sticky='ew')
p_opp_wynik.grid(row=2, column=1, sticky='ew')

# output frame 5 ------------------------------------------------------------------------------------------
outputFrame5 = tkinter.Frame(width=260, height=100, bd='4')

j_c = tkinter.Label(outputFrame5, text=f'{"Długość jętki: "}', anchor='w')
j_o = tkinter.Label(outputFrame5, text=f'{"Odległość od końca krokwi do spodu jętki: "}', anchor='w', bg='lightgrey')

j_c.grid(row=0, column=0, sticky='ew', ipadx=(20))
j_o.grid(row=1, column=0, sticky='ew')

j_c_wynik = tkinter.Label(outputFrame5, text='cm', anchor='w', bg='lightgrey')
j_o_wynik = tkinter.Label(outputFrame5, text='cm', anchor='w')

j_c_wynik.grid(row=0, column=1, sticky='ew')
j_o_wynik.grid(row=1, column=1, sticky='ew')

root.mainloop()
