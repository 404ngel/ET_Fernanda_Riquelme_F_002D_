def existe_codigo(cupo, planes):
    return cupo.upper() in planes

def cupos_por_tipo_de_plan(tipo, cupo, plan):
    total_cupos = 0
    for cupo in plan:
        if plan[cupo][1].lower == tipo.lower():
            total_cupos += plan[cupo][1]
            print(f"El total de cupos disponibles es: {total_cupos}")

def busqueda_por_rango_de_precio(min_precio, max_precio, planes, inscripciones):
    lista_encontrados = []
    for cupo in planes:
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

    planes = {
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
                continue
            case 2:
                continue
            case 3:
                continue
            case 4:
                continue
            case 5:
                continue
            case 6:
                print("Programa Finalizado...")
                break
            case _: 
                print("Ingrese una opcion valida.")
main()