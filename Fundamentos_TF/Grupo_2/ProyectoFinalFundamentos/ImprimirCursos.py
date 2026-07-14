from constantes import EST_NOMBRE, EST_CODIGO, EST_CICLO, EST_CURSOS, CUR_CREDITOS, CUR_EVALUACIONES, CUR_HORAS, EVA_NOMBRE, EVA_FECHA, EVA_NOTA, EVA_PESO

def MostrarDatosCurso(nombre_curso, info_curso):
    print(f"\n CURSO: {nombre_curso}")
    print(f"Créditos: {info_curso[CUR_CREDITOS]}")
    
    total_horas = sum(info_curso[CUR_HORAS])
    print(f"Total horas invertidas: {total_horas} horas")
    if info_curso[CUR_HORAS]:
        print(f"Sesiones de estudio individuales: {info_curso[CUR_HORAS]}")
    else:
        print("(Aún no se registran horas de estudio)")
        
    print("   --- Evaluaciones Registradas ---")
    if not info_curso[CUR_EVALUACIONES]:
        print("   (No hay evaluaciones o notas en este curso)")
    else:
        numero = 1
        
        for info_eva in info_curso[CUR_EVALUACIONES]:
            fecha_bonita = info_eva[EVA_FECHA].strftime("%d/%m/%Y")
            print(f"   {numero}. [{info_eva[EVA_NOMBRE]}] Fecha: {fecha_bonita} | Nota: {info_eva[EVA_NOTA]} | Peso: {int(info_eva[EVA_PESO] * 100)}%")
            numero = numero + 1

def ImprimirCursos(estudiante):
    print("\n--- IMPRIMIR DATOS DE CURSO(S) ---")
    if not estudiante:
        print("No hay ningún estudiante registrado en el sistema.")
        return
        
    print(f"Estudiante: {estudiante[EST_NOMBRE]} ({estudiante[EST_CODIGO]}) - Ciclo: {estudiante[EST_CICLO]}")
    if not estudiante[EST_CURSOS]:
        print("El estudiante no tiene cursos inscritos.")
        return

    print("\n¿Qué desea hacer?")
    print("1. Imprimir solo 1 curso")
    print("2. Imprimir varios cursos específicos")
    print("3. Imprimir TODOS los cursos inscritos")
    opc = input("Seleccione una opción: ").strip()

    if opc == "1":
        nombre = input("Ingrese el nombre del curso a buscar: ").strip().lower()
        curso_llave = None
        for curso in estudiante[EST_CURSOS]:
            if curso.lower() == nombre:
                curso_llave = curso
                break
        if curso_llave:
            print("\n=============================================")
            MostrarDatosCurso(curso_llave, estudiante[EST_CURSOS][curso_llave])
            print("=============================================")
        else:
            print(f"El curso '{nombre}' no se encuentra en el sistema.")

    elif opc == "2":
        print("Ingrese los nombres de los cursos separados por comas:")
        lista_nombres = input("Cursos a imprimir: ").split(",")
        print("\n=============================================")
        encontrados = False
        for nombre_crudo in lista_nombres:
            nombre_limpio = nombre_crudo.strip().lower()
            for curso in estudiante[EST_CURSOS]:
                if curso.lower() == nombre_limpio:
                    MostrarDatosCurso(curso, estudiante[EST_CURSOS][curso])
                    encontrados = True
        print("=============================================")
        if not encontrados:
            print("No se encontró ninguno de los cursos ingresados.")

    elif opc == "3":
        print("\n=============================================")
        print("        REPORTE COMPLETO DE CURSOS ACADÉMICOS ")
        print("=============================================")
        for curso_nombre, curso_info in estudiante[EST_CURSOS].items():
            MostrarDatosCurso(curso_nombre, curso_info)
        print("\n=============================================")
    else:
        print("Opción no válida. Operación cancelada.")