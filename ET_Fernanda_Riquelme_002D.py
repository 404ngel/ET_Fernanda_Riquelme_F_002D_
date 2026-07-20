def buscar_codigo(cupo, planes):
    return cupo.upper() in planes

def cupos_por_tipo_de_plan(cupo, lista_planes, inscripciones):
    total_cupos = 0
    for cupo in lista_planes:
        if lista_planes[cupo][1].lower() == inscripciones[cupo][1].lower(): 
            total_cupos += lista_planes[cupo][1]
            print(f"El total de cupos disponibles es: {total_cupos}")

def busqueda_por_rango_de_precio(min_precio, max_precio, planes, lista_planes):
    lista_encontrados = []
    for cupo in lista_planes:
        precio = planes[cupo][0]
        cupos = planes[cupo][1]

        if precio >= min_precio and precio <= max_precio and cupos > 0:
            nombre = planes[cupo][0]
            lista_encontrados.append(f"{nombre}--cupos: {cupo}")
    if len(lista_encontrados.sort()):
        print("No hay planes en ese rango de precios.")
    else:
        lista_encontrados.sort()
        print("Los planes encontrados son:")
        print(lista_encontrados)

def actualizar_precio_de_plan(cupo, nuevo_precio, planes):
    cupo = cupo.upper()
    if buscar_codigo(cupo, planes):
        planes[cupo][0] = nuevo_precio
        return True
    return False

def agregar_registro(cupo,mimi,nombre, precio, cupos, planes, plan):
    cupo = cupo.upper()
    if buscar_codigo(cupo, plan):
        return False
    plan[cupo] = [nombre, mimi]
    planes[cupo] = [precio, cupos]
    return True

def eliminar_plan(cupo, plan, planes):
    cupo = cupo.upper()
    if buscar_codigo(cupo, plan):
        del plan[cupo]
        del planes[cupo]
        return True
    return False

def validar_texto(texto):
    if not texto or texto.isspace():
        return False
    return True

def validar_numero_positivo(numero):
    return numero > 0

def validar_codigo(codigo):
    if not codigo or codigo.isspace():
        return False
    return True
def validar_nombre(nombre):
    if not nombre or nombre.isspace():
        return False
    return True
def validar_tipo():
    if not "Mensual" or "trimestral" or "anual":
        return False
    return True
def validar_duracion(duracion):
    return duracion > 0
def validar_acceso(acceso):
    if acceso.lower() == "n":
        return False
    if acceso.lower() == "s":
        return True
def validar_clases(clases):
    if clases.lower() == "n":
        return False
    if clases.lower() == "s":
        return True
def validar_horario(horario):
    if not horario or horario.isspace():
        return False
    return True
def validar_precio(precio):
    return precio > 0
def validar_cupos(cupos):
    return cupos > 0

def menu_principal():
    print('''========== MENÚ PRINCIPAL ==========
1. Cupos por tipo de plan
2. Búsqueda de planes por rango de precio
3. Actualizar precio de plan
4. Agregar plan
5. Eliminar plan
6. Salir
=====================================''')
    
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("debe ingresar una opcion valida.")
        except ValueError:
            print("Debe Ingresar un numero entero")

def main():

    planes_lista = {
        'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
        'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
        'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
        'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
        'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
        'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
        }
    
    inscripciones = {
            'F001': [14990, 30],
            'F002': [22990, 10],
            'F003': [39990, 0],
            'F004': [35990, 6],
            'F005': [159990, 2],
            'F006': [18990, 15],
            }
    
    while True:

        menu_principal()
        opc = leer_opcion()
        match opc:
            
            case 1:
                op = input("Ingrese tipo de plan a consultar: ")
                cupos_por_tipo_de_plan(op, planes_lista, inscripciones)
            case 2:
                while True:
                    try:
                        val_min = int(input("Ingrese Precio Minimo: "))
                        val_max = int(input("Ingrese Precio Maximo: "))
                        if val_min >= 0 and val_max >= 0 and val_min <= val_max:
                            break
                        else:
                            print("Rango Invalido")
                    except ValueError:
                        print("debe Ingresar valores enteros.")
                busqueda_por_rango_de_precio(val_min, val_max, planes_lista, inscripciones)
            case 3:
                while True:
                    cupo = input("Ingrese código del plan: ").upper()
                    try:
                        nuevo_precio = int(input("Ingrese el nuevo precio: "))
                        if nuevo_precio >= 0:
                            if actualizar_precio_de_plan(cupo, nuevo_precio, planes_lista):
                                print("Precio Actualizado Correctamente")
                            else:
                                print("El plan no existe")
                        else:
                            print("El precio debe ser mayor a 0")
                    except ValueError:
                        print("Deebe ingresar un numero valido")
                    seguir = input("Desea Actualizar Otro Registro? (s/n): ").lower()
                    if seguir == "n":
                        break
            case 4:
                plan = input("Ingrese el plan: ").upper()
                if not validar_texto or buscar_codigo(plan, planes_lista):
                    print("Plan Invalido o ya existente")
                    continue
                codigo = input("Ingrese código del plan: ")
                if not validar_codigo(codigo):
                    print("Codigo Invalido")
                    continue
                nombre = input("Ingrese nombre del plan: ")
                if not validar_nombre(nombre):
                    print("Nombre Invalido")
                    continue
                tipo = input("Ingrese tipo: ")
                if not validar_tipo(tipo):
                    print("Tipo Invalido")
                    continue
                try:
                    duracion = input("Ingrese duración (meses): ")
                    if not validar_duracion(duracion):
                        print("Duracion invalida")
                        continue
                except ValueError:
                    print("Ingrese un numero entero")
                    continue
                piscina = input("¿Incluye acceso a piscina? (s/n): ")
                if not validar_acceso(piscina):
                    print("Ingrese una opcion valida")
                    continue
                clases = input("¿Incluye clases grupales? (s/n): ")
                if not validar_clases(clases):
                    print("Ingrese una opcion valida")
                    continue
                horario = input("Ingrese horario: ")
                if not validar_horario(horario):
                    print("Ingrese un horario valido")
                    continue
                try:
                    precio = input("Ingrese precio:")
                    if not validar_precio(precio):
                        print("Ingrese un precio valido")
                        continue
                except ValueError:
                    print("Ingrese un numero entero")
                    continue
                try:
                    cupos = ("Ingrese cupos: ")
                    if not validar_cupos(cupos):
                        print("Ingrese una opcion valida")
                        continue
                except ValueError:
                    print("Ingrese un numero entero")
                    continue
                if agregar_registro(plan, codigo, nombre, tipo, piscina, clases, horario, precio, cupos):
                    print("Plan agregado")
                else:
                    print("Error, el plan ya existe")
                


            case 5:
                cupo = input("Ingrese el plan a eliminar: ").upper()
                if eliminar_plan(cupo, planes_lista, inscripciones):
                    print("Plan Eliminado")
                else:
                    print("El plan no existe")
            case 6:
                print("Programa Finalizado...")
                break
            case _: 
                print("Ingrese una opcion valida.")
main()