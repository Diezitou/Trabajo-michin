#==== Aquí se definen algunas variables y constantes =====
DIAS = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
embarcaciones=[]
embarc_sin_repetir=[]
capturas=[]
cuota_diaria_kg=400
ultimo_registro=0

#======== Aquí Estan las funciones. Haz click en la flecha atrás de def para expandir ======
def validar_num(num):
    """""Valida que se haya ingresado un numero entero"""
    try:
        num=int(num)
        return num
    except:
        return ''

def Separar(n):
    """""Crea un titulo o una separacion en la terminal"""
    if n=='':
     print('='*50)
    else :
      return f'{'='*25} {n} {'='*25}'
  
def busqueda_lineal(lista, valor):
    """"Encuentra o no un valor dado"""
    for i in range(len(lista)):
        if lista[i]==valor:
            return i
    return -1

def suma_recursiva(lista):
    """Calcula recursivamente la suma de las capturas de una embarcación."""
    if len(lista) == 0:
        return 0
    return lista[0] + suma_recursiva(lista[1:])

def maximo_recursivo(lista):
    """Devuelve recursivamente la mayor captura diaria de una embarcación."""
    if len(lista) == 0:
        return 0
    if len(lista) == 1:
        return lista[0]
    mayor_resto = maximo_recursivo(lista[1:])
    return lista[0] if lista[0] > mayor_resto else mayor_resto

def contar_dias_sin_captura(lista):
    """Cuenta recursivamente cuántos días la embarcación registró 0 kg."""
    if len(lista) == 0:
        return 0
    dia_cero = 1 if lista[0] == 0 else 0
    return dia_cero + contar_dias_sin_captura(lista[1:])

    
def calcular_total_sem(embarcaciones, capturas):        # 10. calcular total semanal
    

    """calcula el total semanal de una embarcacion"""
    totales = []
    for i in range(len(embarcaciones)):
        suma = 0
        for j in range(len(DIAS)):

            suma = suma + capturas[i][j]
        totales.append(suma)

    return totales

def total_diario(embarcaciones, capturas):              # 11. calcular total de cada día (función recursiva btw, con la siguient)
    """calcula el total de cada dia"""
    total_dia = []
    for j in range(len(DIAS)):

        suma = 0
        for i in range(len(embarcaciones)):
            suma = suma + capturas[i][j]

        total_dia.append(suma)

    mejor_dia(total_dia)    # << Aquí es donde llama a la función.
    return total_dia

def mejor_dia(total_dia):                               # Esta es la siguient función, es la que identific el mejor día de pesca, yayyyy
    """Encuentra el mejor dia de pesca"""
    mayor = 0
    for j in range(1, len(DIAS)):

        if total_dia[j] > total_dia[mayor]:
            mayor = j

    print("\n==== MEJOR DÍA DE PESCA ====")
    print("Día:", DIAS[mayor])
    print("Total capturado:", total_dia[mayor], "KG")
    
def ranking_embarcaciones(lista_nombres, matriz_capturas):
    "Devuelve dos listas ordenadas de mayor a menor captura semanal: los nombres y sus totales y no modifica las listas originales"
    nombres_rank = []
    totales_rank = []
    for i in range(len(lista_nombres)):
        total = 0
        for kg in matriz_capturas[i]:
            total += kg
        nombres_rank.append(lista_nombres[i])
        totales_rank.append(total)
    n = len(totales_rank)
    for pasada in range(n - 1):                  #Ordenamiento burbuja
        for j in range(n - 1 - pasada):
            if totales_rank[j] < totales_rank[j + 1]:
                #Intercambiar totales
                temp = totales_rank[j]
                totales_rank[j] = totales_rank[j + 1]
                totales_rank[j + 1] = temp
                #Intercambiar nombres (para que sigan emparejados)
                temp = nombres_rank[j]
                nombres_rank[j] = nombres_rank[j + 1]
                nombres_rank[j + 1] = temp
    return nombres_rank, totales_rank

#================== Este es el menú de opciones. Aún falta agregar opciones =========================

while True:
    print(f'{Separar('Menú principal')}')
    print("1- Registrar embarcaciones")
    print("2- Registrar capturas")
    print("3- Mostrar embarcaciones")
    print("4- Modificar embarcación existente")
    print("5- Eliminar registro de embarcación")
    print("6- Ranking de embarcaciones")
    print("7- Salir")
    eleccion_menu=input('Elección: ')
    match eleccion_menu:
        
        #================================INGRESO DE EMBARCACIONES===============================
        case '1':
            print('pepe1')
                #========Ingreso de la cantidad de embarcaciones que se van a ingresar======
            while True:
                    cantidad_de_embarcaciones=input('Ingrese cuántas embarcaciones desea registrar (Min: 3, Max: 10):  ')
                    if validar_num(cantidad_de_embarcaciones):
                        if 2<int(cantidad_de_embarcaciones)<11:
                            if int(cantidad_de_embarcaciones):
                                cantidad_de_embarcaciones=int(cantidad_de_embarcaciones)
                                break
                        else:
                            print(Separar('Error: Ingrese un valor entre 3 y 10'))
                    else:
                        print(Separar('Error: Ingrese un valor número entero'))           
            
            #=========Aquí se ingresan las embarcaciones una por una============
            for i in range(cantidad_de_embarcaciones):
                nombre=""
                while True:
                    nombre=input(f'Ingrese el nombre de la embarcación:  ')
                    if nombre!='':
                        if nombre not in embarc_sin_repetir:
                            embarc_sin_repetir.append(nombre)
                            nombre.lower().replace(" ", "")
                            embarcaciones.append(nombre)
                            #======== Aquí se crean los vectores para las capturas según cada embarcación =======
                            capturas.append([0,0,0,0,0,0,0])
                            break
                        else:
                            print(Separar('Error: La embaracación ya se encuentra agregada'))
                    else:
                        print(Separar('Error: El nombre de la embarcación no puede estar vacío'))
                        
        #========================== INGRESO DE CAPTURAS ====================================             
        case '2':
            if len(embarcaciones)!=0:
                    while True:
                        print(Separar("Elija una opción"))
                        print("1- Registrar captura")
                        print("2- Editar capturas por día")
                        print("3- Ver embarcaciones sin registros")
                        print("4- Volver al menú principal")
                        eleccion_captura_menu=input("Elección:  ")
                        match eleccion_captura_menu:
                            
                            case "1":
                                print(Separar("Elija en qué embarcación desea registrar capturas"))
                                eleccion_captura=input("Elección:  ")
                                eleccion_captura.lower().replace(" ", "")
                                indice_busqueda=busqueda_lineal(embarcaciones, eleccion_captura)
                                if indice_busqueda!=-1:
                                    for i in range(len(DIAS)):
                                        while True:
                                            capturas[indice_busqueda][i]=input(f"Ingrese las capturas de {embarcaciones[indice_busqueda]} el día {DIAS[i]}:  ")
                                            if validar_num(capturas[indice_busqueda][i]) and 0<int(capturas[indice_busqueda][i])<2001:
                                                    capturas[indice_busqueda][i]=int(capturas[indice_busqueda][i])
                                                    print(capturas[indice_busqueda][i])
                                                    break
                                            else:
                                                print(Separar("Error: Se debe ingresar un número entero entre 0 y 2000"))
                                else:
                                    print(Separar("Error: No se ha encontrado la embarcación ingresada"))
                                                        
                            case "2":
                                print(Separar("Elija en qué embarcación desea registrar capturas"))
                                eleccion_captura=input("Elección:  ")
                                eleccion_captura.lower().replace(" ", "")
                                indice_busqueda=busqueda_lineal(embarcaciones, eleccion_captura)
                                if indice_busqueda!=-1:
                                    print("Ingrese el día de la semana que desee editar")
                                    print("1-Lunes")
                                    print("2-Martes")
                                    print("3-Miercoles")
                                    print("4-Jueves")
                                    print("5-Viernes")
                                    print("6-Sábado")
                                    print("7-Domingo")        
                                    eleccion_captura_dia=input("Elección:  ")
                                    if validar_num(eleccion_captura_dia):
                                        eleccion_captura_dia=int(validar_num(eleccion_captura_dia))
                                        if 0<eleccion_captura_dia<8:
                                            if validar_num(capturas[indice_busqueda][eleccion_captura_dia]) and 0<int(capturas[indice_busqueda][eleccion_captura_dia])<2001:
                                              capturas[indice_busqueda][eleccion_captura_dia-1]=int(input(f"Ingrese las capturas de {embarcaciones[indice_busqueda]} el día {DIAS[eleccion_captura_dia-1]}:  "))
                                            else:
                                                print(Separar("Error: Se debe ingresar un número entero entre 0 y 2000"))
                                        else:
                                            print(Separar("Error: Se debe ingresar un día válido [1-8]"))
                                else:
                                    print(Separar("Error: No se ha encontrado la embarcación ingresada"))
                                    
                            case "3":
                                embarcaciones_vacias=[]
                                for i in range(len(embarcaciones)):
                                    if sum(capturas[i])==0:
                                        embarcaciones_vacias.append(embarcaciones[i])
                                    print(embarcaciones_vacias)
                                    
                            case "4":
                                break
                            
                            case _:
                                print(Separar("Error: introduzca una opción válida"))
            else:
                print(Separar("Error: No se han registrado embarcaciones, por lo que no se pueden ingresar capturas"))
                                

        case '3':
            if len(embarcaciones)!=0:
                for i in range(len(embarcaciones)):
                    print(f"{embarcaciones[i]} se encuentra en el indice {i}")    
            else:
                print(Separar("Error: No se han registrado embarcaciones, por lo que no se pueden ingresar capturas"))
                
        case '5':
            if len(embarcaciones)!=0:
                print(Separar("Seleccione la embarcacion que desea eliminar"))
                eleccion_eliminar=input("Elección:  ")
                eleccion_eliminar.lower().replace(" ", "")
                indice_busqueda=busqueda_lineal(embarcaciones, eleccion_eliminar)
                if indice_busqueda!=-1:
                    del embarcaciones[indice_busqueda]
                    del capturas[indice_busqueda]
                    del embarc_sin_repetir[indice_busqueda]
            else:
                print(Separar("Error: No se han registrado embarcaciones, por lo que no se pueden ingresar capturas"))  
                
        case '6':
            if len(embarcaciones) == 0:
                print(Separar("Aún no hay embarcaciones registradas"))
            elif len(capturas) != len(embarcaciones):
                print(Separar("Primero registre las capturas de todas las embarcaciones"))
            else:
                nombres_rank, totales_rank = ranking_embarcaciones(embarcaciones, capturas)
                print(Separar("Ranking semanal"))
                for i in range(len(nombres_rank)):
                    print(f"{i + 1}. {nombres_rank[i]} - {totales_rank[i]} kg")       
        
        case '6':
            print('pepe5')
            break
        
        
        case _:
            print('Exepcion jejejijijaja')
