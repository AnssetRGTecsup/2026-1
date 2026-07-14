from constantes import EST_NOMBRE, EST_CODIGO, EST_CICLO, EST_CURSOS

def RegistrarEstudiante(lista_estudiantes):
    print("\n--- REGISTRAR ESTUDIANTE ---")
    
    codigo = input("Ingrese el código del estudiante (ejm: U20241A): ").strip().upper()
    
    
    for est in lista_estudiantes:
        if est[EST_CODIGO] == codigo:
            print(f"Error: Ya existe un estudiante registrado con el código {codigo}.")
            return

    nombre = input("Ingrese el nombre completo del estudiante: ").strip()
    
    while True:
        try:
            ciclo = int(input("Ingrese el ciclo actual (número entero): "))
            if ciclo > 0:
                break
            print("El ciclo debe ser un número mayor a 0.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    
    nuevo_estudiante = {
        EST_CODIGO: codigo,
        EST_NOMBRE: nombre,
        EST_CICLO: ciclo,
        EST_CURSOS: {}  
    }
    
    
    lista_estudiantes.append(nuevo_estudiante)
    print(f"\n¡Estudiante {nombre} ({codigo}) registrado con éxito!")