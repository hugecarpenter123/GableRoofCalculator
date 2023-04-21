import turtle
import math

def dotted(item, length: int):
    for i in range(length // 4):
        if i % 2 == 0:
            item.penup()
            item.forward(4)
        else:
            item.pendown()
            item.forward(4)
    item.penup()


def rysuj(dach1, drugaDepka):
    canvas = turtle.Screen()
    turtle.TurtleScreen._RUNNING = True

    krokwa = turtle.Turtle()
    krokwa.speed(12)
    # Narysowanie krokwy-----------
    krokwa.penup()
    krokwa.hideturtle()
    krokwa.goto(-300, -30)
    krokwa.showturtle()
    krokwa.pendown()
    krokwa.forward(600)
    krokwa.left(90)
    krokwa.forward(60)
    krokwa.left(90)
    krokwa.forward(600)
    krokwa.left(90)
    krokwa.forward(60)

    krokwa.penup()
    krokwa.left(180)
    krokwa.forward(60)
    krokwa.right(90)

    # 1 zaciecie-----------
    if dach1.kat_dachu <= 90:
        krokwa.right(dach1.kat_dachu)
        c = math.tan(math.radians(90 - dach1.kat_dachu)) * 60
        distance = math.sqrt(60 ** 2 + c ** 2)
        krokwa.showturtle()
        krokwa.pendown()
        krokwa.forward(distance)
        # drugie zaciecie
        krokwa.left(180)  # powrót
        krokwa.forward(distance)
        krokwa.right(180 - dach1.kat_dachu)
        x = 60 / math.tan(math.radians(0.5 * dach1.kat_dachu))
        krokwa.forward(x)
        krokwa.right(dach1.kat_dachu)
        krokwa.forward(distance)
        # narysowanie kąta
        krokwa.left(dach1.kat_dachu)
        krokwa.forward(50)
        krokwa.left(90)
        krokwa.circle(50, dach1.kat_zaciecia)
        krokwa.penup()
        krokwa.setx(-300)
        krokwa.sety(-30)
        krokwa.right(krokwa.heading())
        krokwa.forward(x + c + 2)
        krokwa.left(90)
        krokwa.forward(10)
        krokwa.pendown()
        krokwa.color('orange')
        krokwa.write(f"{round(dach1.kat_zaciecia, 2)}\N{DEGREE SIGN}", font=('arial', 10, 'bold'))
    else:
        c = math.tan(math.radians(90-dach1.kat_zaciecia)) * 60
        x = 60 / math.sin(math.radians(180-dach1.kat_dachu))
        distance = math.sqrt(c**2 + 60**2)
        krokwa.pendown()
        krokwa.forward(c)
        krokwa.right(180 - dach1.kat_zaciecia)
        krokwa.forward(distance)
        krokwa.left(180-dach1.kat_zaciecia)
        krokwa.forward(x)
        krokwa.left(dach1.kat_zaciecia)
        krokwa.forward(distance)
        krokwa.penup()
        krokwa.goto(-300+x+60,-30)
        krokwa.right(krokwa.heading())
        krokwa.left(90)
        krokwa.pendown()
        krokwa.circle(60, dach1.kat_zaciecia)
        #podpisanie kąta
        krokwa.penup()
        krokwa.goto(-300+x+20,-20)
        krokwa.color('orange')
        krokwa.write(f"{round(dach1.kat_zaciecia, 2)}\N{DEGREE SIGN}", font=('arial', 10, 'bold'))

    # reset to (0,0) --------------
    krokwa.color('black')
    krokwa.penup()
    krokwa.goto(0, 0)

    # rysuj zamek
    krokwa.penup()
    depka1 = (dach1.depka['odległość'] * 600) / dach1.d_krokwi_calkowita
    krokwa.setx(-300 + depka1)
    krokwa.sety(-30)

    if dach1.kat_dachu <= 90:
        krokwa.right(90)
    else:
        krokwa.right(krokwa.heading())

    krokwa.pendown()
    krokwa.left(dach1.depka['kąt'])
    krokwa.forward(30)
    krokwa.color('grey')
    dotted(krokwa, 80)
    krokwa.color('black')

    z = 30 / math.sin(math.radians(dach1.depka['kąt2']))
    krokwa.penup()
    krokwa.goto(-300 + depka1 - z, -30)
    krokwa.right(krokwa.heading())
    krokwa.left(dach1.depka['kąt2'])
    krokwa.pendown()
    zx = 30 / math.tan(math.radians(dach1.depka['kąt2']))
    krokwa.forward(zx)
    krokwa.color('grey')
    dotted(krokwa, 80)
    krokwa.color('black')

    # rysowanie łuków do kątów
    krokwa.penup()
    krokwa.goto(-300 + depka1, -30)
    krokwa.right(krokwa.heading())
    krokwa.forward(40)
    krokwa.left(90)
    krokwa.pendown()
    krokwa.circle(40, dach1.depka['kąt'])
    krokwa.penup()
    krokwa.setx(-300 + depka1 - 5)
    krokwa.sety(-20)
    krokwa.color('orange')
    krokwa.write(f"{round(dach1.depka['kąt'], 2)}\N{DEGREE SIGN}", font=('arial', 10, 'bold'))
    krokwa.color('black')

    # drugi łuk
    krokwa.penup()
    krokwa.setx(-300 + depka1 - z)
    krokwa.sety(-30)
    krokwa.right(180)
    krokwa.forward(40)
    krokwa.left(90)
    krokwa.pendown()
    krokwa.circle(40, 180 - dach1.depka['kąt2'])
    krokwa.penup()
    krokwa.setx(-300 + depka1 - z - 25)
    krokwa.sety(-20)
    krokwa.color('orange')
    krokwa.pendown()
    krokwa.write(f"{180 - round(dach1.depka['kąt2'], 2)}\N{DEGREE SIGN}", font=('arial', 10, 'bold'))

    # zaznaczanie długości
    krokwa.penup()
    krokwa.goto(-300, -30)
    krokwa.right(krokwa.heading() + 90)
    krokwa.color('grey')
    krokwa.pendown()
    krokwa.forward(150)
    krokwa.backward(10)
    krokwa.left(90)
    krokwa.color('darkgrey')
    krokwa.forward(600)
    krokwa.right(90)
    krokwa.color('grey')
    krokwa.forward(10)
    krokwa.backward(150)
    krokwa.penup()
    krokwa.setx(-10)
    krokwa.sety(-190)
    krokwa.color('orange')
    krokwa.pendown()
    krokwa.write(str(dach1.d_krokwi_calkowita) + 'cm', font=('arial', 10, 'bold'))

    # od zacięcia do zamka
    krokwa.penup()
    if dach1.kat_dachu <= 90:
        krokwa.goto(-300 + x + c, -30)
    else:
        krokwa.goto(-300 + x, -30)
    krokwa.color('grey')
    krokwa.pendown()
    krokwa.forward(100)
    krokwa.backward(10)
    krokwa.left(90)
    krokwa.color('darkgrey')
    if dach1.kat_dachu <= 90:
        krokwa.setx(-300 + depka1)

    else:
        krokwa.setx(-300 + depka1)
    krokwa.color('grey')
    krokwa.right(90)
    krokwa.forward(10)
    krokwa.backward(100)

    krokwa.penup()
    krokwa.goto(-10, -140)
    krokwa.pendown()
    krokwa.color('orange')
    krokwa.write(str(round(dach1.d_k_w, 2)) + 'cm', font=('arial', 10, 'bold'))

    if drugaDepka:
        krokwa.penup()
        krokwa.color('black')
        depka2 = (600 * dach1.d_k_gp) / dach1.d_krokwi_calkowita
        krokwa.setx(-300 + depka2)
        krokwa.sety(-30)
        krokwa.right(krokwa.heading())
        krokwa.left(dach1.depka['kąt'])
        krokwa.pendown()
        krokwa.forward(30)
        krokwa.left(90)
        krokwa.forward(zx)
        # siatka
        krokwa.penup()
        krokwa.color('lightgrey')
        krokwa.setx(-300 + depka2)
        krokwa.sety(-30)
        krokwa.right(krokwa.heading())
        krokwa.right(90)
        krokwa.pendown()
        krokwa.forward(50)
        krokwa.backward(5)
        krokwa.right(90)
        krokwa.goto(-300, -75)
        krokwa.penup()
        krokwa.setx(-300 + (depka2 / 2) - 10)
        krokwa.sety(-95)
        krokwa.color('orange')
        krokwa.write(str(dach1.d_k_gp) + 'cm', font=('arial', 10, 'bold'))

    krokwa.hideturtle()
    canvas.exitonclick()