import turtle as t
from datetime import datetime
from time import sleep

t.bgcolor("black")

def marcas(t, raio):
    marca_seg = raio * 0.1
    marca_hora = raio * 0.2
    
    for i in range(0,360,6):
        if i % 30 == 0:
            marca = marca_hora
        else:
            marca = marca_seg
        t.color("white")
        t.seth(i)
        t.pu()
        t.fd(raio - marca)
        t.pd()
        t.fd(marca)
        t.pu()
        t.bk(raio)

def horas(t, raio, hora):
    t.color("white")
    t.width(8)
    t.seth((hora.hour * 30) + (hora.minute * 0.5))
    t.pd()
    t.fd(raio * 0.6)
    t.pu()
    t.bk(raio * 0.6)

def minutos(t, raio, hora):
    t.width(4)
    t.seth((hora.minute * 6) + (hora.second * 0.1))
    t.pd()
    t.fd(raio * 0.8)
    t.pu()
    t.bk(raio * 0.8)

def segundos(t, raio, hora):
    t.width(2)
    t.color("white")
    t.seth(hora.second * 6)
    t.pd()
    t.fd(raio)
    t.pu()
    t.bk(raio)

#Config da Tartaruga
t.mode("logo")
t.shape("circle")
t.tracer(0)

while True:
    #apagar
    t.reset()
    
    #desenhar
    agora = datetime.now()
    marcas(t, 300)
    horas(t, 300, agora)
    minutos(t, 300, agora)
    segundos(t, 300, agora)
    t.update()
    
    #pausa
    sleep(1)