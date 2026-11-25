#==== Aquí se definen algunas variables y constantes =====
DIAS = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
embarcaciones = []
embarc_sin_repetir=[]
capturas=[]
cuota_diaria_kg=400
ultimo_registro=0
ingreso_embarcaciones=False

#======== Aquí Estan las funciones. Haz click en la flecha atrás de def para expandir ======
def validar_num(num):
    try:
        num=int(num)
        return num
    except:
        return ''

def Separar(n):
    if n=='':
     print('='*50)
    else :
      return f'{'='*25} {n} {'='*25}'
  
def busqueda_lineal(lista, valor):
    for i in range(len(lista)):
        if lista[i]==valor:
            return i
    return -1

#================== Este es el menú de opciones. Aún falta agregar opciones =========================

while True:
    print(f'{Separar('Menú principal')}')
    print("1- Registrar embarcaciones")
    print("2- Registrar capturas")
    print("3- Mostrar embarcaciones")
    print("4- Modificar embarcación existente")
    print("5- Salir")
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
                            nombre.lower
                            nombre.replace(" ", "")
                            embarcaciones.append(nombre)
                            ingreso_embarcaciones=True
                            #======== Aquí se crean los vectores para las capturas según cada embarcación =======
                            capturas.append([0,0,0,0,0,0,0])
                            break
                        else:
                            print(Separar('Error: La embaracación ya se encuentra agregada'))
                    else:
                        print(Separar('Error: El nombre de la embarcación no puede estar vacío'))
                        
        #========================== INGRESO DE CAPTURAS ====================================             
        case '2':
            if ingreso_embarcaciones:
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
                                indice_busqueda=busqueda_lineal(embarcaciones, eleccion_captura)
                                print("indice: ", indice_busqueda)
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
                                indice_busqueda=busqueda_lineal(embarcaciones, eleccion_captura)
                                print("indice: ", indice_busqueda)
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
                                            capturas[indice_busqueda][eleccion_captura_dia-1]=input(f"Ingrese las capturas de {embarcaciones[indice_busqueda]} el día {DIAS[eleccion_captura_dia-1]}:  ")
                                            print(capturas)
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
            if ingreso_embarcaciones:
                for i in range(len(embarcaciones)):
                    print(f"{embarcaciones[i]} se encuentra en el indice {i}")
                    
            else:
                print(Separar("Error: No se han registrado embarcaciones, por lo que no se pueden ingresar capturas"))
                
            
        case '5':
            print('pepe5')
            break
        case _:
            print('Exepcion jejejijijaja')
