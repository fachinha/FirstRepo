def calc_clasica(opc,res,num):
    if opc == 1:
        while num != "=":
            res = res + int(num)
            num = input("Ingrese un número o = para finalizar\n")
    elif opc == 2:
        while num != "=":
            res = res - int(num)
            num = input("Ingrese un número o = para finalizar\n")
    elif opc == 3:
        while num != "=":
            res = res*int(num)
            num = input("Ingrese un número o = para finalizar\n")
    elif opc == 4:
        while num != "=":
            while num == "0":
                num = input("No se puede dividir por 0. Intente de nuevo\n")
            res = res/int(num)
            num = input("Ingrese un número o = para finalizar\n")
    return res

def calc_fracciones(opc,numerador_res,denominador_res,numerador,denominador):
    if opc == 1:
        if denominador_res != denominador:
            numerador_res = numerador_res*denominador
            numerador = numerador*denominador_res
            denominador_res = denominador_res*denominador
        numerador_res = numerador_res + numerador
    elif opc == 2:
        if denominador_res != denominador:
            numerador_res = numerador_res*denominador
            numerador = numerador*denominador_res
            denominador_res = denominador_res*denominador
        numerador_res = numerador_res - numerador
    elif opc == 3:
        numerador_res = numerador_res*numerador
        denominador_res = denominador_res*denominador
    elif opc == 4:
        numerador_res = numerador_res*denominador
        denominador_res = denominador_res*numerador
    print("\n")
    rta = print(f"{numerador_res}\n-----\n{denominador_res}")
    return rta

def calc_conversiones(decimal,conversor):
    if decimal == 0:
        print("Su numero es 0") 
    elif conversor == "bin":
        binario = ""
        while decimal > 0:
          res = decimal % 2
          binario = str(res) + binario
          decimal = decimal // 2 
        return binario
    elif conversor == "oct":
        octal = ""
        while decimal > 0:
            res = decimal % 8
            octal = str(res) + octal 
            decimal = decimal // 8
        return octal
    elif conversor == "hex":
        hexa = ""
        while decimal > 0:
            res = decimal % 16
            if res > 9:
                lista=["A","B","C","D","E","F"]
                res = res - 10
                res = lista[res]
            hexa = str(res) + hexa 
            decimal = decimal // 16
        return hexa

inicio = input("")
while inicio != "On":
    inicio = input("")
print("Menú de Opciones\n1 - Calculadora Clásica\n2 - Calculadora de Fracciones\n3 - Conversiones numéricas\n4 - Apagar la calculadora")
opcionelegida = int(input(""))
while opcionelegida != 4:
    if opcionelegida == 1:
        print("\n")
        print("Calculadora clásica")
        print("1-Suma\n2-Resta\n3-Multiplicación\n4-División")
        opc = int(input(""))
        while opc < 0 or opc > 4:
            opc = int(input("Opción no válida. Intente de nuevo\n"))
        print("\n")
        res = int(input("Ingrese un número\n"))
        num = input("Ingrese un número o = para finalizar\n")
        print(calc_clasica(opc,res,num))
        print("\n")
    elif opcionelegida == 2:
        print("\n")
        print("Calculadora de fracciones")
        print("1-Suma\n2-Resta\n3-Multiplicación\n4-División")
        opc = int(input(""))
        while opc < 0 or opc > 4:
            opc = int(input("Opción no válida. Intente de nuevo\n"))
        print("\n")
        numerador_res = int(input("Ingrese el numerador de la primer fracción\n"))
        denominador_res = int(input("Ingrese el denominador de la primer fracción\n"))
        while denominador_res == 0:
            denominador_res = int(input("El denominador no puede ser 0. Intente de nuevo\n"))
        numerador = int(input("Ingrese el numerador de la segunda fracción\n"))
        denominador = int(input("Ingrese el denominador de la segunda fracción\n"))
        while denominador == 0:
            denominador = int(input("El denominador no puede ser 0. Intente de nuevo\n"))
        calc_fracciones(opc,numerador_res,denominador_res,numerador,denominador)
        print("\n")
    elif opcionelegida == 3:
        print("\n")
        print("Calculadora de conversiones")
        decimal = int(input("Ingrese numero a convertir: \n"))
        conversor = str(input("Ingrese conversor (bin, oct, hex): \n"))
        print(calc_conversiones(decimal,conversor))
        print("\n")
    print("Menú de Opciones\n1 - Calculadora Clásica\n2 - Calculadora de Fracciones\n3 - Conversiones numéricas\n4 - Apagar la calculadora")
    opcionelegida = int(input(""))
