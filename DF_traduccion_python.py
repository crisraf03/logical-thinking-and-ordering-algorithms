##TRADUCCION ALGORITMOS A CODIGO python

#encender una vela
def estado_vela(vela, caja):
    estado = vela.estado
    print("la vela esta:" + estado)
    if estado == off:
        encender_vela(vela)
    print("La vela esta encendida")
    else:
        print("La vela ya esta encendida")

#cuenta regresiva
def cuenta_regresiva(tiempo):
    for i in range(tiempo):
        print(tiempo - i + "segundos")
        tiempo += -1
        if tiempo = 0:
            return(None)


#entrar en una tienda
def entrarTienda(peso, pesoOn):
    if peso >= pesoOn:
        abrirPuerta()
    else
        False

#Realizar una compra de zapatos
def CompraZapatos( ): 
    print("Bienvenid@ a su compra online")
    print()
    mostrarZapatos()
    print('seleccione sus zapatos preferidos')
    zapatos = seleccionarZapatos()
    nZapatos = np.zeros(len(zapatos))
    for i in range(len(zapatos)):
        nZapatos += int(input("Indique el número de zapatos"))
    compra = zapatos.precio @ nZapatos
    return(compra)

#validar si una persona es mayor de edad

def MayoriaDeEdad(edad):
    if edad > 18:
        print('es mayor de edad')
        return True
    if edad <= 18:
        print('No es mayor de edad')
        return False
    else
        edad = int(input('Introduce tu edad en un número porfavor, es para ver si eres mayor de edad:'))
        MayoriaDeEdad(edad)