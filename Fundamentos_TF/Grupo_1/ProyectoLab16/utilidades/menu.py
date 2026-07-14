def mostrar_menu():
    
    opciones = {
        1: "Registrar Estudiante",
        2: "Actualizar Datos del Estudiante",
        3: "Registrar Curso",
        4: "Actualizar Evaluaciones",
        5: "Actualizar Horas de Estudio",
        6: "Eliminar Curso(s)",
        7: "Imprimir Datos de Curso(s)",
        8: "Guardar Archivos",
        9: "Leer Archivos",
        10: "Generar Reporte Grafico",
        11: "Salir",
    }

    print("SISTEMA DE SEGUIMIENTO ACADEMICO")
    for numero, descripcion in opciones.items():
        print(f"{numero}. {descripcion}")
