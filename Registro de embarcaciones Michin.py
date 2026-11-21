DIAS = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
nombres = ["Don Lucho", "Mar Azul"]
capturas = [[320, 410, 0, 280, 390, 450, 0],
[150, 200, 180, 0, 220, 300, 260]]
def Separar(n):
    if n=='':
     print('='*50)
    else :
      return f'{'='*25} {n} {'='*25}'

while True:
    while True:
        print(f'{Separar('Elija la opción')}')
        print("1- Registrar embarcaciones")
        print("2- Registrar capturas")
        print("3- Mostrar lista de embarcaciones")
        print("4- Modificar embarcación existente")
        print("5- Salir")
        eleccion_menu=input('Elección: ')
        match eleccion_menu:
            case '1':
                print('pepe1')
            case '2':
                print('pepe2')
            case '3':
                print('pepe3')
            case '4':
                print('pepe4')
            case '5':
                print('pepe5')
            case _:
                print('Exepcion jejejijijaja')