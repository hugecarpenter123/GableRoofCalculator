import math
import turtle
#to delete----------
# from dekarz.class_CieciaNaKrokwach import CieciaNaKrokwach
#
# data = {'h': 260, 'd': 697, 'p': 35, 'h_krokwi': 8, 'op': 200, 'hj': 149.18}
# dach1 = CieciaNaKrokwach(data)
#to delete----------

def symuluj(dach1, rysujPlatwe, rysujJetke):

    canvas = turtle.Screen()
    turtle.TurtleScreen._RUNNING = True

    #dane
    kat = (180 - dach1.kat_dachu) / 2
    #-------------------------------

    # 1 pal
    s = turtle.Turtle()
    s.speed(11)
    s.penup()
    s.goto(-250,-150)
    s.left(90)
    s.pendown()
    s.forward(200)
    s.right(90)
    s.forward(20)
    s.right(90)
    s.forward(200)
    s.penup()
    s.goto(250, -150)
    #2 pal
    s.right(180)
    s.pendown()
    s.forward(200)
    s.left(90)
    s.forward(20)
    s.left(90)
    s.forward(200)

    s.penup()
    s.goto(250, 50)
    s.left(90)

    #obrócony w prawo, robienie dachu
    alfa = dach1.kat_dachu
    # alfa = 120
    distance = 250 / math.cos(math.radians(90 - 0.5 * alfa))
    kpd = (distance * dach1.krokiew_poza_dachem) / dach1.d_k_w # krokwa poza dachem
    dkx = (20 * dach1.d_k_x) / dach1.h_krokwi # długość krokwi x (od przecięcie krokwi spodem do końca)
    dkc = (dach1.dkc * dkx) / dach1.d_k_x
    kat_n = 90 - (90 - kat)
    d_o = math.tan(math.radians(kat_n)) * dach1.h_krokwi
    o = (d_o * dach1.h_krokwi) / dach1.h_krokwi
    dkxh = None
    if dach1.kat_dachu <= 90:
        dkxh = math.sqrt(20*20 + dkx*dkx)
    else:
        dkxh = round(math.sqrt((dkx-dkc)*(dkx-dkc) + 20*20), 2)
    print(s.heading())
    s.left(180-kat)
    s.pendown()
    s.backward(kpd)
    s.forward(kpd + distance)
    s.right(alfa/2)
    s.forward(dkxh)
    s.right(90 + kat)
    s.forward(distance + kpd)
    s.right(180 - dach1.depka['kąt'])
    s.forward(dkxh)

    s.penup()
    s.setx(-250)
    s.sety(50)
    s.left(90)
    s.left(kat)
    s.pendown()
    s.backward(kpd)
    s.forward(kpd + distance)
    s.left(alfa/2)
    s.forward(dkxh)
    s.left(90+kat)
    s.forward(distance+kpd)
    s.left(180-dach1.depka['kąt'])
    s.forward(dkxh)
    # print(s.heading())

    # rysowanie siatki
    s.penup()
    s.goto(-250, 50)
    # print(s.heading())
    s.right(s.heading())
    s.pendown()
    s.color('grey')
    s.forward(500)
    s.penup()
    s.setx(0)
    s.left(90)

    s.pendown()
    h = 250 / math.tan(math.radians(0.5 * alfa))
    s.color('lightgrey')
    s.forward(h)
    s.penup()
    s.goto(10, 40 + 0.5 * h)
    s.color('orange')
    s.write(f"h = {dach1.h}cm", font=('arial', 11, 'bold'))

    # if 'op' in dir(dach1):
    if rysujPlatwe:
        hp = (h * dach1.hp) / dach1.h
        xp = hp / math.tan(math.radians(kat))
        s.color('black')
        s.setx(-250)
        s.sety(50)

        s.right(90)
        s.forward(xp)
        s.pendown()
        s.left(90)
        s.forward(hp)
        s.right(90)
        s.forward(20)
        s.right(90)
        s.forward(hp)

        s.penup()
        s.goto(250-xp, 50)
        s.right(180)
        s.pendown()
        s.forward(hp)
        s.left(90)
        s.forward(20)
        s.left(90)
        s.forward(hp)
        # siatka
        s.penup()
        s.goto(-250+xp+20, 50+hp)
        s.left(90)
        s.color('lightgrey')
        s.pendown()
        s.forward(25)
        s.backward(5)
        s.right(90)
        s.forward(hp)
        s.penup()
        s.backward(hp/2 - 5)
        s.left(90)
        s.forward(5)
        s.pendown()
        s.color('orange')
        s.write(f"{dach1.hp}cm", font=('arial', 11, 'bold'))
        s.color('lightgrey')

        #siatka dół
        s.penup()
        s.setx(-250+xp)
        s.sety(50)
        s.right(90)
        s.pendown()
        s.forward(50)
        s.backward(5)
        s.left(90)
        s.setx(250-xp)
        s.left(90)
        s.backward(5)
        s.forward(50)
        s.penup()
        s.setx(-15)
        s.sety(-15)
        s.pendown()
        s.color('orange')
        s.write(f"{dach1.opp}cm", font=('arial', 11, 'bold'))

    # if 'hj' in dir(dach1):
    if rysujJetke:
        s.color('black')
        s.penup()
        djw_half = (250 * (dach1.d_j_w / 2)) / (dach1.d / 2)
        djw_s = djw_half / math.cos(math.radians(kat)) #djw_s: długość jętki wewnętrznej 'przeciwprostokątnej'
        djx = (dach1.d_j_x * 20) / dach1.h_krokwi

        #ustawienie kursora na górze krokwy wewnętrznej
        s.setx(0)
        s.sety(50+h)
        #heading: do góry
        #przejście na wysokość rysowania spodu jętki
        s.right(90 + kat)
        s.forward(djw_s)
        #obrót równolegle do ziemi
        s.right(180 - kat)
        # rysowanie jętki
        s.pendown()
        s.backward(djx)
        s.forward(djx * 2 + djw_half * 2)
        s.right(180-kat)
        # 'grubość' jętki wzdłóż krokwy: b
        b = 20 / math.sin(math.radians(kat))
        diff_djw_djz = b * math.cos(math.radians(kat))
        s.forward(b)
        s.right(kat)
        s.forward((djw_half - diff_djw_djz + djx) * 2)
        s.penup()
        s.backward(djx)
        s.right(kat)
        s.pendown()
        s.color('white')
        s.width(2)
        s.forward(b)
        s.penup()
        s.right(180-kat)
        s.forward(djw_half*2)
        s.right(180 - kat)
        s.pendown()
        s.forward(b)
        s.hideturtle()

        print(s.heading())

    # koniec
    canvas.exitonclick()

#to delete----------
# symuluj(dach1, True, True)
#to delete----------