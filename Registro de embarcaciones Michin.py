#==== Aquí se definen algunas variables y constantes =====
DIAS = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
embarcaciones = []
embarc_sin_repetir= []
capturas = []
capturas=[]
cuota_diaria_kg=400

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
#================== Este es el menú de opciones. Aún falta agregar opciones =========================

while True:
    print(f'{Separar('Elija la opción')}')
    print("1- Registrar embarcaciones")
    print("2- Registrar capturas")
    print("3- Mostrar lista de embarcaciones")
    print("4- Modificar embarcación existente")
    print("5- Salir")
    eleccion_menu=input('Elección: ')
    match eleccion_menu:
        
        #================================INGRESO DE EMBARCACIONES===============================
        case '1':
            print('pepe1')
            
                #========Ingreso de la cantidad de embarcaciones que se van a ingresar======
            while True:
                    cantidad_de_embarcaciones=input('Ingrese cuántas embarcaciones desea registrar (Min: 3, Max: 10)')
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
                            embarcaciones.append(nombre)
                            cantidad_de_embarcaciones=0 #==== Reinicia la varible en caso de que se quiran agregar más
                            break
                        else:
                            print(Separar('Error: La embaracación ya se encuentra agregada'))
                    else:
                        print(Separar('Error: El nombre de la embarcación no puede estar vacío'))
            print(embarcaciones)
                            
                    
                    
        case '2':
            print('pepe2')
        case '3':
            print('pepe3')
        case '4':
            print('pepe4')
        case '5':
            print('pepe5')
            break
        case _:
            print('Exepcion jejejijijaja')