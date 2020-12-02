from Tabla import Tabla
import os
if __name__ == '__main__':
    while True:
        opc = int(input("1-Genarar Tabla\n2-Salir\n>"))
        if opc == 1:
            n1 = int(input("Digite un numero >"))
            tb = Tabla(n1)
            tb.Generar_tabla()
        elif opc == 2:
            print("**Gracias por usar mi probar mi programa***")
            break
        else:
         print("Opcion Invalida")
