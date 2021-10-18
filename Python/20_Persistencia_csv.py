import csv


def procesamientoDato(nom_archivo):
    try:
        archivo_csv = open(nom_archivo, "r")

    except:
        print("Archivo inexistente")
        return

    lineas = csv.reader(archivo_csv)
    cotizacion = []
    for fila in lineas:  # recorre por pila, primero los titulos y luego sus valores (fila por fila)
        cotizacion.append(fila)
        # print (fila)

    archivo_csv.close()
    # print(cotizacion)
    claves = cotizacion[0]
    # print(claves)

    # el  cvs toma los datos como String.
    diccionario_cotiza = {}

    for i in claves:
        diccionario_cotiza[i] = []
    print(diccionario_cotiza)

    for i in cotizacion[1:]:
        for j in range(len(i)):
            # guardarlo como float los que no sean nombre
            if j > 0:
                diccionario_cotiza[claves[j]].append(float(i[j]))
            else:
                diccionario_cotiza[claves[j]].append(i[j])

    print(diccionario_cotiza)
    return diccionario_cotiza


def estadisticas(dicci_coti, nombre_archiv):
    # almacenaremos el nombre de cada columna y sus datos estadisticos ejem: Final minimo, etc
    resumen = [["Nombre", "Mínimo", "Máximo", "Promedio"]]
    # eliminamos el campo de clave nombre, ya que no haremos calculos numericos en base a el
    del dicci_coti["Nombre"]

    print(dicci_coti)


dicc_cotización = procesamientoDato("cotizacion.csv")

estadisticas(dicc_cotización, "estadisticas_cotizacion.csv")