import os
import platform


def rango(a,b,c):
    while(c<a or c>b):
        print("El valor ingresado es inválido")
        print("Ingréselo de nuevo: ")
        c = int(input())
    return c

def limpiarPantalla():
    if(platform.system() == 'Windows'):
        os.system('cls')
    else:
        os.system('clear')

def menu(opcion):
    print("Menú")
    print("1. Registrar paciente.")
    print("2. Ver porcentajes de géneros.")
    print("3. Ver información de los pacientes.")
    print("4. Ver promedio de edades de pacientes con obesidad.")
    print("5. Ver estadísticas de los pacientes con enfermedades preexistentes.")
    print("6. Ver dinero recaudado.")
    print("\n0. Salir.")
    opcion = int(input("Ingrese opción: "))
    opcion = rango(0,6,opcion)
    return opcion

def imprimirCotizacion(datos,dia,mes,year):
    print("SALUD CARE Ltda.")
    print("Cotización de servicios de salud")
    print(f"\nFecha: {dia}/{mes}/{year}")
    print(f"\nNombre del cliente: {datos['nombre']} {datos['apellidos']}\n\n")
    print("Item    Descripción                           Valor/mes")
    print("01     Tarifa básica                          $100000")
    print(f"02     Costo mensual género/edad              ${datos['costoGeneroEdad']}")
    print(f"03     Costo mensual enf. preexistentes       ${datos['costoEnfermedades']}")
    print(f"04     Costo mensual x IMC                    ${datos['costoImc']}")
    print("                                       ------------------")
    print(f"                              Subtotal        ${datos['subtotal']}")
    print(f"                              IVA(19%)        ${datos['iva']:.0f}")
    print("                                       ------------------")
    print(f"                                 Total        ${datos['total']:.0f}")
    print("\n\n\nFirma asesor Comercial______________________")
    print("\n                   Estamos para servirle")
    print("___________________________________________________________")
    input("\n\nIngrese Enter para continuar")

def registro(i,contHombres,contObesidad,acumEdad,acumDinero,contDiabetes,contHipertension,contCardiovascular):
    datos = {}
    indice = ''
    dia = 0
    mes = 0
    year = 0
    print("Ingrese la fecha de hoy")
    dia = int(input("Día: "))
    dia = rango(1,31,dia)
    mes = int(input("Mes: "))
    mes = rango(1,12,mes)
    year = int(input("Año: "))
    year = rango(2022,9999,year)
    limpiarPantalla()
    print(f"Datos del paciente #{i+1}")
    datos["nombre"] = input("Nombre: ")
    datos["apellidos"] = input("Apellidos: ")
    datos["genero"] = input("Género [M/F]: ")
    datos["genero"] = datos["genero"].upper()
    while(datos["genero"]!='M' and datos["genero"]!='F'):
        print("Género ingresado inválido: ")
        datos["genero"] = input("Ingréselo de nuevo: ")
        datos["genero"] = datos["genero"].upper()
    datos["edad"] = int(input("Edad: "))
    datos["edad"] = rango(0,120,datos["edad"])
    print("¿Sufre de diabetes?")
    print("1. Sí.")
    print("0. No.")
    datos["diabetes"] = int(input("Ingrese respuesta: "))
    datos["diabetes"] = rango(0,1,datos["diabetes"])
    print("¿Sufre de hipertensión?")
    print("1. Sí.")
    print("0. No.")
    datos["hipertension"] = int(input("Ingrese respuesta: "))
    datos["hipertension"] = rango(0,1,datos["hipertension"])
    print("¿Sufre de algún problema cardiovascular?")
    print("1. Sí.")
    print("0. No.")
    datos["cardiovascular"] = int(input("Ingrese respuesta: "))
    datos["cardiovascular"] = rango(0,1,datos["cardiovascular"])
    datos["imc"] = float(input("IMC: "))
    
    if(datos["genero"]=='M'):
        contHombres += 1

    if(datos["edad"]<30):
        datos["costoGeneroEdad"] = 0        
    elif(datos["edad"]<61):
        if(datos["genero"]=='M'):
            datos["costoGeneroEdad"] = 50000
        else:
            datos["costoGeneroEdad"] = 55000
    elif(datos["edad"]<71):
        if(datos["genero"]=='M'):
            datos["costoGeneroEdad"] = 65000
        else:
            datos["costoGeneroEdad"] = 60000
    else:
        datos["costoGeneroEdad"] = 75000

    datos["costoEnfermedades"] = 0
    if(datos["diabetes"]):
        datos["costoEnfermedades"] += 25000
        contDiabetes += 1
    if(datos["hipertension"]):
        datos["costoEnfermedades"] += 32000
        contHipertension += 1
    if(datos["cardiovascular"]):
        datos["costoEnfermedades"] += 40000
        contCardiovascular += 1

    if(datos["imc"]<18.5):
        datos["costoImc"] = 15000
    elif(datos["imc"]<25):
        datos["costoImc"] = 0
    elif(datos["imc"]<27):
        datos["costoImc"] = 10000
    elif(datos["imc"]<30):
        datos["costoImc"] = 15000
    elif(datos["imc"]<35):
        datos["costoImc"] = 20000
        contObesidad += 1
        acumEdad += datos["edad"]
    elif(datos["imc"]<40):
        datos["costoImc"] = 35000
        contObesidad += 1
        acumEdad += datos["edad"]
    elif(datos["imc"]<50):
        datos["costoImc"] = 50000
        contObesidad += 1
        acumEdad += datos["edad"]
    else:
        datos["costoImc"] = 100000
        contObesidad += 1
        acumEdad += datos["edad"]

    datos["subtotal"] = 100000 + datos["costoGeneroEdad"] + datos["costoEnfermedades"] + datos["costoImc"]
    datos["iva"] = datos["subtotal"] * 0.19
    datos["total"] = datos["subtotal"] + datos["iva"]

    acumDinero += datos["total"]

    limpiarPantalla()

    imprimirCotizacion(datos,dia,mes,year)

    i += 1
    indice = datos["nombre"] + datos["apellidos"]
    return datos,i,indice,contHombres,contObesidad,acumEdad,acumDinero,contDiabetes,contHipertension,contCardiovascular

def verPorcentajes(i,contHombres):
    porcHombres = (contHombres / i) * 100
    contMujeres = i - contHombres
    porcMujeres = 100 - porcHombres
    print(f"Pacientes registrados: {i}")
    print(f"Cantidad de hombres: {contHombres} ({porcHombres:.2f}%)")
    print(f"Cantidad de mujeres: {contMujeres} ({porcMujeres:.2f}%)")
    input("\n\nIngrese Enter para continuar")

def verInfo(pacientes):
    for i in pacientes:
        print(f"Paciente: {pacientes[i]['nombre']} {pacientes[i]['apellidos']}")
        print(f"Género: {pacientes[i]['genero']}")
        print(f"Edad: {pacientes[i]['edad']}")
        if(pacientes[i]["diabetes"] or pacientes[i]["hipertension"] or pacientes[i]["cardiovascular"]):
            print("Enfermedades preexistentes: ")
            if(pacientes[i]["diabetes"]):
                print("- Diabetes")
            if(pacientes[i]["hipertension"]):
                print("- Hipertensión")
            if(pacientes[i]["cardiovascular"]):
                print("- Problema(s) Cardiovascular(es)")
        else:
            print("Enfermedades preexistentes: No presenta")    
        print(f"IMC: {pacientes[i]['imc']}")
        print(f"\nCostos financieros mensuales de {pacientes[i]['nombre']}:")
        print(f"Costos por género/edad: ${pacientes[i]['costoGeneroEdad']}")
        print(f"Costos por enfermedades preexistentes: ${pacientes[i]['costoEnfermedades']}")
        print(f"Costos por IMC: ${pacientes[i]['costoImc']}")
        print(f"IVA: ${pacientes[i]['iva']:.0f}")
        print(f"Total a pagar: ${pacientes[i]['total']:.0f}\n\n")
    input("Ingrese Enter para continuar")

def verObesidad(contObesidad,acumEdad,i):
    
    print(f"Pacientes registrados: {i}")
    print(f"Pacientes con obesidad: {contObesidad}")
    if(contObesidad):
        promEdad = acumEdad/contObesidad
        print(f"Edad promedio de pacientes con obesidad: {promEdad}")
    else:
        print("No hay pacientes con obesidad :)")
    input("\n\nIngrese Enter para continuar")

def verEnfermedades(contDiabetes,contHipertension,contCardiovascular,i):
    totalEnfermedades = contDiabetes + contHipertension + contCardiovascular
    print(f"Pacientes registrados: {i}")
    print(f"Cantidad de pacientes con enfermedades preexistentes: {totalEnfermedades}")

    if(contDiabetes>contHipertension):
        if(contDiabetes>contCardiovascular):
            print(f"La enfermedad más frecuente es la Diabetes, con un total de {contDiabetes} paciente(s) con esta condición")
        elif(contDiabetes<contCardiovascular):
            print(f"La enfermedad más frecuente son los Problemas Cardiovasculares, con un total de {contCardiovascular} paciente(s) con esta condición")
        else:
            print(f"Las enfermedades más frecuentes son la Diabetes y los Problemas Cardiovasculares, con un total de {contDiabetes} paciente(s) con estas condiciones")
    elif(contHipertension>contCardiovascular):
        if(contHipertension>contDiabetes):
            print(f"La enfermedad más frecuente es la Hipertensión, con un total de {contHipertension} paciente(s) con esta condición")
        elif(contHipertension<contDiabetes):
            print(f"La enfermedad más frecuente es la Diabetes, con un total de {contDiabetes} paciente(s) con esta condición")
        else:
            print(f"Las enfermedades más frecuentes son la Diabetes y la Hipertensión, con un total de {contHipertension} paciente(s) con estas condiciones")
    elif(contCardiovascular>contDiabetes):
        if(contCardiovascular>contHipertension):
            print(f"La enfermedad más frecuente son los Problemas Cardiovasculares, con un total de {contCardiovascular} paciente(s) con esta condición")
        elif(contCardiovascular<contHipertension):
            print(f"La enfermedad más frecuente es la Hipertensión, con un total de {contHipertension} paciente(s) con esta condición")
        else:
            print(f"Las enfermedades más frecuentes son la Hipertensión y los Problemas Cardiovasculares, con un total de {contCardiovascular} paciente(s) con estas condiciones")
    else:
        print(f"Las tres enfermedades se presentaron en igual magnitud en nuestros pacientes, con un total de {contDiabetes} paciente(s) por enfermedad")
    input("\n\nIngrese Enter para continuar")

def verDinero(acumDinero,i):
    print(f"Pacientes registrados: {i}")
    print(f"Total de dinero recaudado: ${acumDinero:.0f}")
    input("\n\nIngrese Enter para continuar")

def salir():
    print("¿Seguro que desea salir?")
    print("1. Sí.")
    print("0. No.")
    print("Ingrese opción: ")
    salir = int(input())
    salir = rango(0,1,salir)
    if(salir):
        limpiarPantalla()
        print("Gracias por usar nuestro programa, hasta luego")
        return 0
    else:
        limpiarPantalla()
        return 1
    
opcion = 1
i = 0
indice = ''
pacientes = {}
datos = {}
contHombres = contObesidad = acumEdad = acumDinero = contDiabetes = contHipertension = contCardiovascular = 0
while(opcion!=0):
    limpiarPantalla()
    opcion = menu(opcion)
    if(opcion==1):
        limpiarPantalla()
        datos,i,indice,contHombres,contObesidad,acumEdad,acumDinero,contDiabetes,contHipertension,contCardiovascular = registro(i,contHombres,contObesidad,acumEdad,acumDinero,contDiabetes,contHipertension,contCardiovascular)
        pacientes[indice] = datos
    elif(opcion==2):
        limpiarPantalla()
        verPorcentajes(i,contHombres)
    elif(opcion==3):
        limpiarPantalla()
        verInfo(pacientes)
    elif(opcion==4):
        limpiarPantalla()
        verObesidad(contObesidad,acumEdad,i)
    elif(opcion==5):
        limpiarPantalla()
        verEnfermedades(contDiabetes,contHipertension,contCardiovascular,i)
    elif(opcion==6):
        limpiarPantalla()
        verDinero(acumDinero,i)
    else:
        limpiarPantalla()
        opcion = salir()
         
