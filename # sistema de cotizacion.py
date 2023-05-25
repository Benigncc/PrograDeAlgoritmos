# sistema de cotizacion 
carillaPorcelana = 250000
implantesDentales = 475000
OrtodonciaBrakets = 800000

descuentoAuxiliar = 0.15
descuentoAdministrativo = 0.10
descuentoDoncente = 0.05

cantCarilla = 0
cantImplante = 0
cantBrackets = 0
opcMenuPrincipal = 1
while opcMenuPrincipal == 1:
    print("bienvenido a la clinica dental El Diente de oro")
    while True :
            try :
                opcMenu = int(input("seleccione una de las siguientes opc para continuar\n1-cotizacion\n2-salir\n"))
                if opcMenu>0 and opcMenu<3 :
                    break
                else : 
                    print("elecion invalida")
            except :
                    print("ingrese solo numeros!!")
    if opcMenu == 2:
        break
    
    while opcMenu == 1 :
        try :
            tipoAuxiliar = int(input("seleccione el tipo de trabajador\n1-Auxiliar\n2-Administrativo\n3-Docente\n"))
            if tipoAuxiliar>0 and tipoAuxiliar<4 :
                break
            else :
                print("eleccion invalida")
        except :
            print("ingrese solo numeros!!")

    if tipoAuxiliar == 1 :
        descuento = descuentoAuxiliar
    elif tipoAuxiliar == 2 :
        descuento = descuentoAdministrativo
    elif tipoAuxiliar == 3 :
        descuento = descuentoDoncente

    while opcMenu == 1 :
        while True :
            #carillas
            while True :
                try :
                    opcCarilla = int(input("desea hacer un tratamiento de carillas de porcelana\n1-si\n2-no\n"))
                    if opcCarilla>0 and opcCarilla<3 :
                        break
                    else : 
                        print("elecion invalida")
                except :
                    print("ingrese solo numeros!!")
            while opcCarilla == 1 :
                try :
                    cantCarilla = int(input("ingrese la cantidad de carillas de porcelana a realizar\n"))
                    if cantCarilla>0:
                        opcCarilla = 3
                    else : 
                        print("ingrese 0 o mas")
                except :
                    print("ingrese solo numeros!!")
            break

        while True :
            #implantes
            while True :
                try :
                    opcImplante = int(input("desea hacer un implante dental \n1-si\n2-no\n"))
                    if opcImplante>0 and opcImplante<3 :
                        break
                    else : 
                        print("elecion invalida")
                except :
                    print("ingrese solo numeros!!")
            while opcImplante == 1 :
                try :
                    cantImplante = int(input("ingrese la cantidad de implantes dentales a realizar\n"))
                    if cantImplante>0:
                        opcImplante = 3
                    else : 
                        print("ingrese 0 o mas")
                except :
                    print("ingrese solo numeros!!")
            break

        while True :
            #Brackets
            while True :
                try :
                    opcBrakets = int(input("desea hacer un tratamiento de orotdoncia de brakets\n1-si\n2-no\n"))
                    if opcBrakets>0 and opcBrakets<3 :
                        break
                    else : 
                        print("elecion invalida")
                except :
                    print("ingrese solo numeros!!")
            while opcBrakets == 1 :
                try :
                    cantBrackets = int(input("ingrese la cantidad de carillas de porcelana a realizar\n"))
                    if cantBrackets>0:
                        opcBrakets = 3
                    else : 
                        print("ingrese 0 o mas")
                except :
                    print("ingrese solo numeros!!")
            break 
        totalC = carillaPorcelana * cantCarilla 
        totalI = implantesDentales * cantImplante 
        totalO = OrtodonciaBrakets * cantBrackets
        
        subTotal = totalC + totalI + totalO
        desc = subTotal * descuento
        total = subTotal - desc
        cuotas = total / 12
        print(40*"*")
        print("       COTIZACIÓN:       ")
        print(40*"*")
        print(f"-->{cantCarilla} tratamiento(s) carilla porcelana ${totalC}")
        print(f"-->{cantImplante} tratamiento(s) implantes dentales ${totalI}")
        print(f"-->{cantBrackets} tratamiento(s) ortodoncia brakets ${totalO}")
        print(40*"*")
        print(f"subtotal ${subTotal}")
        print(f"descuento ${desc}")
        print(40*"*")
        print(f"total ${total}")
        print(40*"*")
        print(f"son 12 cuotas de ${cuotas}")
        print("sonria bonito!!!")
        while True:
            try:
                opcRenunciar = int(input("desea usar esta cotizacion?\n1-si\n2-no"))
                if opcRenunciar>0 and opcRenunciar<3:
                    if opcRenunciar == 1:
                        break
                    elif opcRenunciar ==2:
                        cantCarilla = 0
                        cantImplante = 0
                        cantBrackets = 0
                        opcMenuPrincipal = 2
                    else:
                        print("ingreso invalido")
            except:
                print("ingresa solo numeros")

