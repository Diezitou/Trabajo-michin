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
    """"Encuentra o no un valor dado sin distinguir mayúsculas ni minúsculas"""
    valor_buscado = str(valor).lower()
    for i in range(len(lista)):
        if str(lista[i]).lower()==valor_buscado:
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

def comparar_embar(embarcaciones, totales):             #12. identifca cual es la embarcacion con mayor y menor captur semanal y así
    """Identifica la embarcación con mayor y menor captura semanal"""
    mayor = 0
    menor = 0

    for i in range(1, len(embarcaciones)):

        if totales[i] > totales[mayor]:
            mayor = i
        if totales[i] < totales[menor]:
            menor = i

    print("Mayor captura:")
    print(embarcaciones[mayor], ":", totales[mayor], "KG")

    print("Menor captura:")
    print(embarcaciones[menor], ":", totales[menor], "KG")
    
def calcular_total_sem(embarcaciones, capturas):        # 10. calcular total semanal
    """calcula el total semanal de una embarcacion"""
    totales = []
    for i in range(len(embarcaciones)):
        suma = 0
        for j in range(len(DIAS)):

            suma = suma + capturas[i][j]
        totales.append(suma)

    return totales

def total_diario(embarcaciones, capturas):              # 11. calcular total de cada día
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

def verificar_cuota(embarcaciones, capturas):               # 13. la cosa de la cuota, la cual tuve ke cambiarle a la variable esta okiii
    """Lista los casos en que una embarcación superó la cuota diaria"""
    encontrado = False

    print("\n==== EMBARCACIONES QUE SUPERARON LA CUOTA ====")

    for i in range(len(embarcaciones)):
        for j in range(len(DIAS)):
            if capturas[i][j] > cuota_diaria_kg:

                print("Embarcación:", embarcaciones[i])
                print("Día:", DIAS[j])
                print("Captura:", capturas[i][j], "KG")
                print("---------------------------")

                encontrado = True

    if encontrado == False:
        print("Ninguna embarcación ha superado la cuota diaria.")

def mostrar_matriz(embarcaciones, capturas,             # 14. muestr la matriz alinead, el punto final, okei, todo listo cuate
                   totales, total_dia):
    """Muestra la matriz alineada con totales por fila y por columna"""
    enca = f"{'Embarcación':<15}"
    
    for j in range(len(DIAS)):
        enca = enca + f"{DIAS[j]:>8}"
    enca = enca + f"{'Total':>10}"
    print(enca)
    
    for i in range(len(embarcaciones)):
        fila = f"{embarcaciones[i]:<15}"
        
        for j in range(len(DIAS)):
            fila = fila + f"{capturas[i][j]:>8}"
        fila = fila + f"{totales[i]:>10}"
        print(fila)
    fila_total = f"{'TOTAL DIA':<15}"
    total_general = 0
    
    for j in range(len(DIAS)):
        fila_total = fila_total + f"{total_dia[j]:>8}"
        total_general = total_general + total_dia[j]
    fila_total = fila_total + f"{total_general:>10}"
    print(fila_total)
    return fila_total

def probar():
    """Verifica funciones de cálculo y recursión con casos normales y de borde"""
    assert suma_recursiva([]) == 0
    assert suma_recursiva([0, 0, 0]) == 0
    assert suma_recursiva([150, 200, 180]) == 530

    assert maximo_recursivo([]) == 0
    assert maximo_recursivo([0]) == 0
    assert maximo_recursivo([320, 410, 0, 450]) == 450

    assert contar_dias_sin_captura([]) == 0
    assert contar_dias_sin_captura([100, 200]) == 0
    assert contar_dias_sin_captura([320, 410, 0, 280, 390, 450, 0]) == 2

    assert busqueda_lineal(["Don Lucho", "Mar Azul"], "Inexistente") == -1
    assert busqueda_lineal(["Don Lucho", "Mar Azul"], "mar azul") == 1

    embs_prueba = ["Don Lucho", "Mar Azul", "La Manabita", "Estrella"]
    caps_prueba = [
        [320, 410, 0, 280, 390, 450, 0],
        [150, 200, 180, 0, 220, 300, 260],
        [500, 0, 350, 420, 380, 0, 310],
        [90, 120, 0, 0, 160, 140, 110]
    ]
    tot_iter = calcular_total_sem(embs_prueba, caps_prueba)
    assert tot_iter == [1850, 1310, 1960, 620]
    for i in range(len(embs_prueba)):
        assert suma_recursiva(caps_prueba[i]) == tot_iter[i]

#================== Este es el menú de opciones. Aún falta agregar opciones =========================

while True:
    print(f'{Separar('Menú principal')}')
    print("1- Registrar embarcaciones")
    print("2- Registrar capturas")
    print("3- Mostrar embarcaciones")
    print("4- Eliminar registro de embarcación")
    print("5- Ranking de embarcaciones")
    print("6- Total semanal por embarcación")
    print("7- Total diario y mejor día de pesca")
    print("8- Mayor y menor captura semanal")
    print("9- Verificar cuota diaria")
    print("10- Mostrar matriz de capturas")
    print("11- Estadísticas recursivas por embarcación")
    print("12- Cargar datos de prueba")
    print("13- Ejecutar pruebas (probar)")
    print("14- Salir")
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
                        if busqueda_lineal(embarc_sin_repetir, nombre) == -1:
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
                                eleccion_captura=eleccion_captura.lower().replace(" ", "")
                                indice_busqueda=busqueda_lineal(embarcaciones, eleccion_captura)
                                if indice_busqueda!=-1:
                                    for i in range(len(DIAS)):
                                        while True:
                                            entrada_cap=input(f"Ingrese las capturas de {embarcaciones[indice_busqueda]} el día {DIAS[i]}:  ")
                                            if validar_num(entrada_cap) != '' and 0<=int(entrada_cap)<=2000:
                                                    capturas[indice_busqueda][i]=int(entrada_cap)
                                                    print(capturas[indice_busqueda][i])
                                                    break
                                            else:
                                                print(Separar("Error: Se debe ingresar un número entero entre 0 y 2000"))
                                else:
                                    print(Separar("Error: No se ha encontrado la embarcación ingresada"))
                                                        
                            case "2":
                                print(Separar("Elija en qué embarcación desea registrar capturas"))
                                eleccion_captura=input("Elección:  ")
                                eleccion_captura=eleccion_captura.lower().replace(" ", "")
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
                                            idx_dia = eleccion_captura_dia - 1
                                            if validar_num(capturas[indice_busqueda][idx_dia]) != '' and 0<=int(capturas[indice_busqueda][idx_dia])<=2000:
                                              nueva_cap = input(f"Ingrese las capturas de {embarcaciones[indice_busqueda]} el día {DIAS[idx_dia]}:  ")
                                              if validar_num(nueva_cap) != '' and 0<=int(nueva_cap)<=2000:
                                                  capturas[indice_busqueda][idx_dia]=int(nueva_cap)
                                              else:
                                                  print(Separar("Error: Se debe ingresar un número entero entre 0 y 2000"))
                                            else:
                                                print(Separar("Error: Se debe ingresar un número entero entre 0 y 2000"))
                                        else:
                                            print(Separar("Error: Se debe ingresar un día válido [1-7]"))
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
                
        case '4':
            if len(embarcaciones)!=0:
                print(Separar("Seleccione la embarcacion que desea eliminar"))
                eleccion_eliminar=input("Elección:  ")
                eleccion_eliminar=eleccion_eliminar.lower().replace(" ", "")
                indice_busqueda=busqueda_lineal(embarcaciones, eleccion_eliminar)
                if indice_busqueda!=-1:
                    del embarcaciones[indice_busqueda]
                    del capturas[indice_busqueda]
                    del embarc_sin_repetir[indice_busqueda]
            else:
                print(Separar("Error: No se han registrado embarcaciones, por lo que no se pueden ingresar capturas"))  
                
        case '5':
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
            if len(embarcaciones) == 0:
                print(Separar("Aún no hay embarcaciones registradas"))
            else:
                totales = calcular_total_sem(embarcaciones, capturas)
                print(Separar("Total semanal por embarcación"))
                for i in range(len(embarcaciones)):
                    print(f"{embarcaciones[i]}: {totales[i]} kg")

        case '7':
            if len(embarcaciones) == 0:
                print(Separar("Aún no hay embarcaciones registradas"))
            else:
                totales_dia = total_diario(embarcaciones, capturas)
                print(Separar("Total por día"))
                for j in range(len(DIAS)):
                    print(f"{DIAS[j]}: {totales_dia[j]} kg")

        case '8':
            if len(embarcaciones) == 0:
                print(Separar("Aún no hay embarcaciones registradas"))
            else:
                totales = calcular_total_sem(embarcaciones, capturas)
                comparar_embar(embarcaciones, totales)

        case '9':
            if len(embarcaciones) == 0:
                print(Separar("Aún no hay embarcaciones registradas"))
            else:
                verificar_cuota(embarcaciones, capturas)

        case '10':
            if len(embarcaciones) == 0:
                print(Separar("Aún no hay embarcaciones registradas"))
            else:
                totales = calcular_total_sem(embarcaciones, capturas)
                totales_dia = total_diario(embarcaciones, capturas)
                mostrar_matriz(embarcaciones, capturas, totales, totales_dia)

        case '11':
            if len(embarcaciones) == 0:
                print(Separar("Aún no hay embarcaciones registradas"))
            else:
                print(Separar("Estadísticas recursivas"))
                for i in range(len(embarcaciones)):
                    total_rec = suma_recursiva(capturas[i])
                    max_rec = maximo_recursivo(capturas[i])
                    dias_cero = contar_dias_sin_captura(capturas[i])
                    print(f"{embarcaciones[i]} -> Total: {total_rec} kg | Máximo diario: {max_rec} kg | Días sin captura: {dias_cero}")

        case '12':
            embarcaciones[:] = ["Don Lucho", "Mar Azul", "La Manabita", "Estrella"]
            embarc_sin_repetir[:] = ["Don Lucho", "Mar Azul", "La Manabita", "Estrella"]
            capturas[:] = [
                [320, 410, 0, 280, 390, 450, 0],
                [150, 200, 180, 0, 220, 300, 260],
                [500, 0, 350, 420, 380, 0, 310],
                [90, 120, 0, 0, 160, 140, 110]
            ]
            print(Separar("Datos de prueba cargados"))

        case '13':
            probar()
            print(Separar("Todas las pruebas pasaron correctamente"))
        
        case '14':
            print(Separar("Gracias por usar nuestro sistema"))
            break
        
        case _:
            print(Separar("Error: ingrese una opción válida"))