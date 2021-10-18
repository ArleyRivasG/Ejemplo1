#NO MODIFICAR, NI AGREGAR CÓDIGO EN ESTE ARCHIVO
class cliente:
  def __init__(self, nombre, edad, dinero_cuenta_bancaria, fila_interes, transaccion, cantidad_retirar, cantidad_consignar):
    self.nombre = nombre
    self.edad = edad
    self.dinero_cuenta_bancaria = dinero_cuenta_bancaria
    self.fila_interes = fila_interes
    self.transaccion = transaccion
    self.cantidad_retirar = cantidad_retirar
    self.cantidad_consignar = cantidad_consignar


cola_general = [
                cliente("Matt",21,235000,"caja","retirar",100000,0),
                cliente("Dan",32,658000,"caja","retirar",98000,0),
                cliente("Diana",29,87000,"info","ninguna",0,0),
                 cliente("kelly", 28, 87000, "info", "ninguna", 0, 0),
                cliente("Arley", 25, 6058000, "caja", "consignar", 0, 50000)
]


def sede_bancaria(cola_general):
    cola_caja = []
    cola_info = []
    suma_retiros = 0
    suma_consignaciones = 0
    edad_minima_retiro = -1
    edad_minima_info = -1
    edad_minima_consignacion = -1


    for instancia in cola_general:
        objeto= instancia
        if(objeto.fila_interes == "caja"):
            cola_caja.append(objeto.nombre)
            if(objeto.transaccion == "retirar"):
                if(edad_minima_retiro == -1):
                    edad_minima_retiro = objeto.edad
                elif(edad_minima_retiro> objeto.edad):
                    edad_minima_retiro=objeto.edad

                if(objeto.cantidad_retirar <= objeto.dinero_cuenta_bancaria):#si no tiene el dinero suficiente no se realiza el retiro
                        suma_retiros = suma_retiros + objeto.cantidad_retirar

            if(objeto.transaccion == "consignar"):
                if(edad_minima_consignacion == -1):
                    edad_minima_consignacion = objeto.edad
                elif(edad_minima_consignacion > objeto.edad):
                    edad_minima_consignacion = objeto.edad
                if (objeto.cantidad_consignar > 0):
                    suma_consignaciones = suma_consignaciones + objeto.cantidad_consignar


        if(objeto.fila_interes == "info"):
            cola_info.append(objeto.nombre)
            if (edad_minima_info == -1):
                edad_minima_info = objeto.edad
            elif (edad_minima_info > objeto.edad):
                edad_minima_info = objeto.edad

    print(cola_caja ,cola_info ,suma_retiros, suma_consignaciones, edad_minima_retiro, edad_minima_info,
          edad_minima_consignacion)


sede_bancaria(cola_general)
